import flask

from mara_app.monkey_patch import patch
from mara_acl.views import blueprint, _handle_login

from . import oauth, config

from mara_acl.views import blueprint


@patch(_handle_login)
def __():
    # whiltelist authorize request
    if flask.request.path.startswith('/acl/get-msal-token'):
        return None

    # if no cached login - perceed to azure login page
    if not flask.session.get("user"): 
        flask.session["flow"] = oauth._build_auth_code_flow(scopes=config.scope())
        return flask.redirect(flask.session["flow"]["auth_uri"])

    # get email from header
    email = flask.session["user"]["preferred_username"]
    if not email:
        flask.abort(400, f'Could not get user email from session object.')
    
    return email


# handle redirect from azure OAuth
@blueprint.route('get-msal-token')
def authorized():
    try:
        cache = oauth._load_cache()
        result = oauth._build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            flask.session.get("flow", {}), flask.request.args)
        if "error" in result:
            flask.abort(400, "Login Failure")
        flask.session["user"] = result.get("id_token_claims")
        oauth._save_cache(cache)
    except ValueError:  # Usually caused by CSRF
        pass  # Simply ignore them
    return flask.redirect(flask.url_for("start_page.start_page"))
