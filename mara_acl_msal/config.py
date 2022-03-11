import typing as t


def client_id() -> str:
    """Application (client) ID of app registration"""
    return None


def client_secret() -> str:
    """Application secret"""
    return None


def authority() -> str:
    """The authority URL"""
    return 'https://login.microsoftonline.com/common'


def scope() -> t.Union[t.List[str], None]:
    """Requested scopes on user login"""
    return None
