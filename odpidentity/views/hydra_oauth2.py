from odpaccounts.db import session as db_session
from odpaccounts.models.user import User
from odpaccounts.models.oauth2_token import OAuth2Token
from hydra_client import HydraClientBlueprint

# Note: the blueprint name 'odpidentity' becomes the provider in the token model
bp = HydraClientBlueprint('odpidentity', __name__, db_session, User, OAuth2Token)
