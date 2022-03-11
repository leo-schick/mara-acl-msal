# Mara ACL MSAL

Implementation for Mara ACL to authenticate via the [Microsoft Authentication Library](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview).

&nbsp;

## Installation

1. Add the `mara-acl-msal` package to your mara environment
2. Create a App in the Azure Active Directory. You have to add `https://your-mara-domain.com/acl/get-msal-token` to the allowed redirect URLs.
3. Patch the mara_acl_msal.config properties accordingly, e.g.
``` python 
import mara_acl_msal.config

patch(mara_acl_msal.config.client_id)(lambda: '<application-id>')
patch(mara_acl_msal.config.client_secret)(lambda: '<client-secret>')
patch(mara_acl_msal.config.authority)(lambda: 'https://login.microsoftonline.com/<tenant-id>')
```
4. Change the MaraApp so that it supports flask sessions. This could be done by using the pip package `Flask-Session`:
``` python
from datetime import timedelta
from flask_session import Session
from mara_app.app import MaraApp

app = MaraApp()
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# The maximum number of items the session stores 
# before it starts deleting some, default 500
app.config['SESSION_FILE_THRESHOLD'] = 100  

Session(app)
```