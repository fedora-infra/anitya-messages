# Copyright (C) 2018-2023  Red Hat, Inc.
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
"""Unit tests for the base AnityaMessage message class."""

import unittest

from anitya_schema import ProjectCreated


class TestAnityaMessage(unittest.TestCase):
    """Tests for AnityaMessage class."""

    def setUp(self):
        """Set up the tests."""
        # We can't use AnityaMessage directly,
        # so we will use something that inherits it
        self.message = ProjectCreated()

    def test_app_name(self):
        """Assert that app_name is correct."""
        self.assertEqual(self.message.app_name, "anitya")
