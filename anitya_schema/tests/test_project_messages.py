# Copyright (C) 2018  Red Hat, Inc.
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
"""Unit tests for the project related message schema."""

import mock

import pytest

from anitya_schema import (
    ProjectCreated,
    ProjectDeleted,
    ProjectEdited,
    ProjectFlag,
    ProjectFlagSet,
    ProjectMapCreated,
    ProjectMapDeleted,
    ProjectMapEdited,
    ProjectVersionDeleted,
    ProjectVersionDeletedV2,
    ProjectVersionUpdated,
    ProjectVersionUpdatedV2,
)


class TestProjectMessage:
    """Tests for anitya_schema.project_messages.ProjectMessage class."""

    def setup_method(self):
        """Set up the tests."""
        # We can't use ProjectMessage directly,
        # so we will use something that inherits it
        self.message = ProjectCreated()

    def test_project_backend(self):
        """Assert that backend is returned."""
        self.message.body = {"project": {"backend": "Dummy"}}

        assert self.message.project_backend == "Dummy"

    def test_project_ecosystem(self):
        """Assert that ecosystem is returned."""
        self.message.body = {"project": {"ecosystem": "Dummy"}}

        assert self.message.project_ecosystem == "Dummy"

    def test_project_homepage(self):
        """Assert that homepage is returned."""
        self.message.body = {"project": {"homepage": "Dummy"}}

        assert self.message.project_homepage == "Dummy"

    def test_project_id(self):
        """Assert that id is returned."""
        self.message.body = {"project": {"id": 0}}

        assert self.message.project_id == 0

    def test_project_name(self):
        """Assert that name is returned."""
        self.message.body = {"project": {"name": "Dummy"}}

        assert self.message.project_name == "Dummy"

    def test_project_version(self):
        """Assert that version is returned."""
        self.message.body = {"project": {"version": "Dummy"}}

        assert self.message.project_version == "Dummy"

    def test_project_versions(self):
        """Assert that list of versions is returned."""
        self.message.body = {"project": {"versions": ["1.00", "0.99"]}}

        assert self.message.project_versions, ["1.00" == "0.99"]

    def test_project_url(self):
        """Assert that correct url to Anitya is returned."""
        self.message.body = {"project": {"id": 0}}
        assert self.message.project_url == "https://release-monitoring.org/projects/0/"


class TestProjectCreated:
    """Tests for anitya_schema.project_messages.ProjectCreated class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectCreated()

    @mock.patch(
        "anitya_schema.project_messages.ProjectCreated.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectCreated.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A new project, Dummy, was added to release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"


class TestProjectEdited:
    """Tests for anitya_schema.project_messages.ProjectEdited class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectEdited()

    @mock.patch(
        "anitya_schema.project_messages.ProjectEdited.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectEdited.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A project, Dummy, was edited in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"


class TestProjectDeleted:
    """Tests for anitya_schema.project_messages.ProjectDeleted class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectDeleted()

    @mock.patch(
        "anitya_schema.project_messages.ProjectDeleted.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectDeleted.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A project, Dummy, was deleted in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"


class TestProjectFlag:
    """Tests for anitya_schema.project_messages.ProjectFlag class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectFlag()

    @mock.patch(
        "anitya_schema.project_messages.ProjectFlag.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectFlag.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A flag was created on project Dummy in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_mappings(self):
        """Assert that array of mappings is returned."""
        self.message.body = {
            "message": {
                "packages": [
                    {"distro": "Fedora", "package_name": "package_fedora"},
                    {"distro": "CentOS", "package_name": "package_centos"},
                ]
            }
        }

        exp = [
            {"distro": "Fedora", "package_name": "package_fedora"},
            {"distro": "CentOS", "package_name": "package_centos"},
        ]

        assert self.message.mappings == exp

    def test_flag_url(self):
        """Assert that correct url is returned."""
        assert self.message.flag_url == "https://release-monitoring.org/flags/"

    def test_reason(self):
        """Assert that reason is returned."""
        self.message.body = {"message": {"reason": "Dummy"}}

        assert self.message.reason == "Dummy"


class TestProjectFlagSet:
    """Tests for anitya_schema.project_messages.ProjectFlagSet class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectFlagSet()

    @mock.patch(
        "anitya_schema.project_messages.ProjectFlagSet.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectFlagSet.flag",
        new_callable=mock.PropertyMock,
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectFlagSet.state",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_state, mock_flag):
        """Assert that correct summary string is returned."""
        mock_flag.return_value = "007"
        mock_state.return_value = "closed"

        exp = "A flag '007' was closed in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_flag(self):
        """Assert that flag string is returned."""
        self.message.body = {"message": {"flag": "Dummy"}}

        assert self.message.flag == "Dummy"

    def test_flag_url(self):
        """Assert that correct url is returned."""
        assert self.message.flag_url == "https://release-monitoring.org/flags/"

    def test_state(self):
        """Assert that state string is returned."""
        self.message.body = {"message": {"state": "Dummy"}}

        assert self.message.state == "Dummy"


class TestProjectMapCreated:
    """Tests for anitya_schema.project_messages.ProjectMapCreated class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectMapCreated()

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapCreated.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapCreated.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A new mapping was created for project Dummy in release-monitoring."
        assert self.message.summary == exp

    def test_distro(self):
        """Assert that distro name string is returned."""
        self.message.body = {"distro": {"name": "Dummy"}}

        assert self.message.distro == "Dummy"

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_package_name(self):
        """Assert that package name string is returned."""
        self.message.body = {"message": {"new": "Dummy"}}

        assert self.message.package_name == "Dummy"

    @pytest.mark.parametrize("distro,packages", [("Fedora", ["dummy"]), ("CentOS", [])])
    def test_packages_fedora(self, distro, packages):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {"distro": {"name": distro}, "message": {"new": "dummy"}}

        assert self.message.packages == packages


class TestProjectMapEdited:
    """Tests for anitya_schema.project_messages.ProjectMapEdited class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectMapEdited()

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapEdited.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapEdited.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A mapping for project Dummy was edited in release-monitoring."
        assert self.message.summary == exp

    def test_distro(self):
        """Assert that distro name string is returned."""
        self.message.body = {"distro": {"name": "Dummy"}}

        assert self.message.distro == "Dummy"

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_edited(self):
        """Assert that list of edited fields is returned."""
        self.message.body = {"message": {"edited": ["Dummy"]}}

        assert self.message.edited == ["Dummy"]

    def test_package_name_new(self):
        """Assert that new package name string is returned."""
        self.message.body = {"message": {"new": "Dummy"}}

        assert self.message.package_name_new == "Dummy"

    def test_package_name_prev(self):
        """Assert that previous package name string is returned."""
        self.message.body = {"message": {"prev": "Dummy"}}

        assert self.message.package_name_prev == "Dummy"

    @pytest.mark.parametrize(
        "distro,packages", [("Fedora", ["dummy", "dummy_prev"]), ("CentOS", [])]
    )
    def test_packages_fedora(self, distro, packages):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {
            "distro": {"name": distro},
            "message": {"prev": "dummy_prev", "new": "dummy"},
        }
        assert self.message.packages == packages

    @pytest.mark.parametrize("distro,packages", [("Fedora", ["dummy"]), ("CentOS", [])])
    def test_packages_fedora_same_package(self, distro, packages):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {
            "distro": {"name": distro},
            "message": {"prev": "dummy", "new": "dummy"},
        }
        assert self.message.packages == packages


class TestProjectMapDeleted:
    """Tests for anitya_schema.project_messages.ProjectMapDeleted class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectMapDeleted()

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapDeleted.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectMapDeleted.project_name",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_property):
        """Assert that correct summary string is returned."""
        mock_property.return_value = "Dummy"

        exp = "A mapping for project Dummy was deleted in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_distro(self):
        """Assert that distro name string is returned."""
        self.message.body = {"message": {"distro": "Dummy"}}

        assert self.message.distro == "Dummy"

    @pytest.mark.skip("The package name is not part of the message")
    @pytest.mark.parametrize("distro,packages", [("Fedora", ["dummy"]), ("CentOS", [])])
    def test_packages_fedora(self, distro, packages):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {"distro": {"name": distro}, "message": {"old": "dummy"}}

        assert self.message.packages == packages


class TestProjectVersionUpdated:
    """Tests for anitya_schema.project_messages.ProjectVersionUpdated class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectVersionUpdated()

    def testDeprecationWarning(self):
        """Assert that deprecation message is printed."""
        with pytest.warns() as record:
            ProjectVersionUpdated()

            assert r"class is deprecated" in str(record[0].message)

        with pytest.warns() as record:
            ProjectVersionUpdated(
                topic="org.release-monitoring.prod.anitya.project.version.update",
                body={},
            )

            assert r"class is deprecated" in str(record[0].message)

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdated.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdated.project_name",
        new_callable=mock.PropertyMock,
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdated.version",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_version, mock_name):
        """Assert that correct summary string is returned."""
        mock_name.return_value = "Dummy"
        mock_version.return_value = "1.0.0"

        exp = "A new version '1.0.0' was found for project Dummy in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_old_version(self):
        """Assert that old version is returned."""
        self.message.body = {"message": {"old_version": "Dummy"}}

        assert self.message.old_version == "Dummy"

    def test_mappings(self):
        """Assert that array of mappings is returned."""
        self.message.body = {
            "message": {
                "packages": [
                    {"distro": "Fedora", "package_name": "package_fedora"},
                    {"distro": "CentOS", "package_name": "package_centos"},
                ]
            }
        }

        exp = [
            {"distro": "Fedora", "package_name": "package_fedora"},
            {"distro": "CentOS", "package_name": "package_centos"},
        ]

        assert self.message.mappings == exp

    def test_distros(self):
        """Assert that array of distros is returned."""
        self.message.body = {
            "message": {"packages": [{"distro": "Fedora"}, {"distro": "CentOS"}]}
        }

        assert self.message.distros, ["Fedora" == "CentOS"]

    def test_version(self):
        """Assert that version string is returned."""
        self.message.body = {"message": {"upstream_version": "1.0.0"}}

        assert self.message.version == "1.0.0"

    def test_versions(self):
        """Assert that versions list is returned."""
        self.message.body = {"message": {"versions": ["1.0.0", "0.9.0"]}}

        assert self.message.versions, ["1.0.0" == "0.9.0"]

    def test_stable_versions(self):
        """Assert that stable versions list is returned."""
        self.message.body = {"message": {"stable_versions": ["1.0.0", "0.9.0"]}}

        assert self.message.stable_versions, ["1.0.0" == "0.9.0"]


class TestProjectVersionUpdatedV2:
    """Tests for anitya_schema.project_messages.ProjectVersionUpdatedV2 class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectVersionUpdatedV2()

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdatedV2.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdatedV2.project_name",
        new_callable=mock.PropertyMock,
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionUpdatedV2.upstream_versions",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_versions, mock_name):
        """Assert that correct summary string is returned."""
        mock_name.return_value = "Dummy"
        mock_versions.return_value = ["1.0.0", "0.9.0"]

        exp = "A new versions '1.0.0, 0.9.0' were found for project Dummy in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_old_version(self):
        """Assert that old version is returned."""
        self.message.body = {"message": {"old_version": "Dummy"}}

        assert self.message.old_version == "Dummy"

    def test_mappings(self):
        """Assert that array of mappings is returned."""
        self.message.body = {
            "message": {
                "packages": [
                    {"distro": "Fedora", "package_name": "package_fedora"},
                    {"distro": "CentOS", "package_name": "package_centos"},
                ]
            }
        }

        exp = [
            {"distro": "Fedora", "package_name": "package_fedora"},
            {"distro": "CentOS", "package_name": "package_centos"},
        ]

        assert self.message.mappings == exp

    def test_distros(self):
        """Assert that array of distros is returned."""
        self.message.body = {
            "message": {"packages": [{"distro": "Fedora"}, {"distro": "CentOS"}]}
        }

        assert self.message.distros == ["Fedora", "CentOS"]

    def test_upstream_versions(self):
        """Assert that list of versions is returned."""
        self.message.body = {"message": {"upstream_versions": ["1.0.0", "0.9.0"]}}

        assert self.message.upstream_versions == ["1.0.0", "0.9.0"]

    def test_versions(self):
        """Assert that versions list is returned."""
        self.message.body = {"message": {"versions": ["1.0.0", "0.9.0"]}}

        assert self.message.versions == ["1.0.0", "0.9.0"]

    def test_stable_versions(self):
        """Assert that stable versions list is returned."""
        self.message.body = {"message": {"stable_versions": ["1.0.0", "0.9.0"]}}

        assert self.message.stable_versions == ["1.0.0", "0.9.0"]

    def test_packages_fedora(self):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {
            "message": {
                "packages": [
                    {"distro": "Fedora", "package_name": "package_fedora"},
                    {"distro": "CentOS", "package_name": "package_centos"},
                ]
            }
        }
        assert self.message.packages == ["package_fedora"]


class TestProjectVersionDeleted:
    """Tests for anitya_schema.project_messages.ProjectVersionDeleted class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectVersionDeleted()

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeleted.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeleted.project_name",
        new_callable=mock.PropertyMock,
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeleted.version",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_version, mock_name):
        """Assert that correct summary string is returned."""
        mock_name.return_value = "Dummy"
        mock_version.return_value = "1.0.0"

        exp = "A version '1.0.0' was deleted in project Dummy in release-monitoring."
        assert self.message.summary == exp

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_version(self):
        """Assert that version string is returned."""
        self.message.body = {"message": {"version": "1.0.0"}}

        assert self.message.version == "1.0.0"


class TestProjectVersionDeletedV2:
    """Tests for anitya_schema.project_messages.ProjectVersionDeletedV2 class."""

    def setup_method(self):
        """Set up the tests."""
        self.message = ProjectVersionDeletedV2()

    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeletedV2.summary",
        new_callable=mock.PropertyMock,
    )
    def test__str__(self, mock_property):
        """Assert that correct string is returned."""
        mock_property.return_value = "Dummy"

        assert self.message.__str__() == "Dummy"

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                ["1.0.0"],
                "A version '1.0.0' was deleted in project Dummy in release-monitoring.",
            ),
            (
                ["1.0.0", "1.0.1"],
                "A versions '1.0.0, 1.0.1' were deleted in project Dummy in release-monitoring.",
            ),
            (
                ["1.0.0", "1.0.1", "1.0.2", "1.0.3", "1.0.4"],
                "A versions '1.0.0, 1.0.1, 1.0.2, 1.0.3, 1.0.4' were deleted in project Dummy in release-monitoring.",  # noqa: E501
            ),
            (
                ["1.0.0", "1.0.1", "1.0.2", "1.0.3", "1.0.4", "1.0.5"],
                "6 versions entries were deleted in project Dummy in release-monitoring.",
            ),
        ],
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeletedV2.project_name",
        new_callable=mock.PropertyMock,
    )
    @mock.patch(
        "anitya_schema.project_messages.ProjectVersionDeletedV2.versions",
        new_callable=mock.PropertyMock,
    )
    def test_summary(self, mock_versions, mock_name, test_input, expected):
        """Assert that correct summary string is returned."""
        mock_name.return_value = "Dummy"
        mock_versions.return_value = test_input

        assert self.message.summary == expected

    def test_agent_name(self):
        """Assert that agent_name is returned."""
        self.message.body = {"message": {"agent": "Dummy"}}

        assert self.message.agent_name == "Dummy"

    def test_versions(self):
        """Assert that version string is returned."""
        self.message.body = {"message": {"versions": ["1.0.0"]}}

        assert self.message.versions == ["1.0.0"]

    @pytest.mark.skip("The package name is not part of the message")
    @pytest.mark.parametrize("distro,packages", [("Fedora", ["dummy"]), ("CentOS", [])])
    def test_packages_fedora(self, distro, packages):
        """Assert that packages list is filled only when it's on Fedora"""
        self.message.body = {"message": {"distro": distro, "package": "dummy"}}

        assert self.message.packages == packages
