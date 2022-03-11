import flask
from msal import ConfidentialClientApplication, SerializableTokenCache

from . import config


def _load_cache():
    cache = SerializableTokenCache()
    if flask.session.get("token_cache"):
        cache.deserialize(flask.session["token_cache"])
    return cache

def _save_cache(cache):
    if cache.has_state_changed:
        flask.session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return ConfidentialClientApplication(
        client_id=config.client_id(),
        authority=authority or config.authority(),
        client_credential=config.client_secret(),
        token_cache=cache)

def _build_auth_code_flow(authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=flask.url_for("mara_acl.authorized", _external=True))

def _get_token_from_cache(scope=None):
    cache = _load_cache()  # This web app maintains one cache per session
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result