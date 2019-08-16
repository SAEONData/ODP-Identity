from . import db
from .static_data_mixin import StaticDataMixin


class Role(StaticDataMixin, db.Model):
    """
    Model representing a generic role.
    """

    # many-to-many scopes-roles relationship
    scopes = db.relationship('Scope',
                             secondary='scoped_role',
                             back_populates='roles',
                             passive_deletes=True)
