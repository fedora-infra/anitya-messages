# Copyright (C) 2018-2023 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import warnings

from fedora_messaging import message
from fedora_messaging.schema_utils import user_avatar_url

ANITYA_URL = "https://release-monitoring.org/"


class AnityaMessage(message.Message):
    """A base class for Anitya messages."""

    @property
    def app_name(self):
        """
        Return the name of the application that generated the message.

        Returns:
            the name of the application (anitya)
        """
        return "anitya"

    @property
    def agent(self):
        """Return the agent's username for this message.

        Returns:
            The agent's username
        """
        warnings.warn(
            "agent property is deprecated, please use agent_name instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.agent_name

    @property
    def agent_name(self):
        """Return the agent's username for this message.

        Returns:
            The agent's username
        """
        return self.body["message"]["agent"]

    @property
    def agent_avatar(self):
        """
        Return a URL to the avatar of the user who caused the action.

        Returns:
            The URL to the user's avatar, or None if username is None.
        """
        return user_avatar_url(self.agent_name)
