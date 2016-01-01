from __future__ import unicode_literals

from siriusxm import serialized

__all__ = [
    'user',
]


class user(object):

    """A Sirius XM internet radio API user."""

    def __init__(self, user):
        if user is None:
            raise AttributeError('user is required')

        self.username = user
        self.sessionID = None
        self.remainingLockoutMinutes = 0
        self.remainingLockoutSeconds = 0

    @property
    @serialized
    def display_name(self):
        """The user's displayable username."""
        return self.username

    @property
    @serialized
    def session_id(self):
        """The user's session id."""
        return self.sessionID

    @property
    def remaining_lockout_minutes(self):
        """The user's remaining lockout minutes."""
        return self.remainingLockoutMinutes

    @property
    def remaining_lockout_seconds(self):
        """The user's remaining lockout seconds."""
        return self.remainingLockoutSeconds
