from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    from .hydra_token import HydraToken
    from .user import User
    from .role import Role
    from .scope import Scope
    from .scoped_role import scoped_role
    from .assigned_role import assigned_role
    from .institution import Institution
    from .institution_registry import InstitutionRegistry
    from .institutional_user import institutional_user
    db.init_app(app)