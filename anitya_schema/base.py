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

from fedora_messaging import message

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
