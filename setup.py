#!/usr/bin/env python
#
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
import os
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.rst")) as fd:
    README = fd.read()


def get_project_version():
    """Read the declared version of the project from the source code"""
    version_file = "anitya_schema/__init__.py"
    with open(version_file, "rb") as f:
        version_pattern = b'^__version__ = "(.+)"$'
        match = re.search(version_pattern, f.read(), re.MULTILINE)
    if match is None:
        err_msg = "No line matching  %r found in %r"
        raise ValueError(err_msg % (version_pattern, version_file))
    return match.groups()[0].decode("utf-8")


def get_requirements(requirements_file="requirements.txt"):
    """Get the contents of a file listing the requirements.

    :arg requirements_file: path to a requirements file
    :type requirements_file: string
    :returns: the list of requirements, or an empty list if
              `requirements_file` could not be opened or read
    :return type: list
    """

    lines = open(requirements_file).readlines()
    dependencies = []
    for line in lines:
        maybe_dep = line.strip()
        if maybe_dep.startswith("#"):
            # Skip pure comment lines
            continue
        if maybe_dep.startswith("git+"):
            # VCS reference for dev purposes, expect a trailing comment
            # with the normal requirement
            __, __, maybe_dep = maybe_dep.rpartition("#")
        else:
            # Ignore any trailing comment
            maybe_dep, __, __ = maybe_dep.partition("#")
        # Remove any whitespace and assume non-empty results are dependencies
        maybe_dep = maybe_dep.strip()
        if maybe_dep:
            dependencies.append(maybe_dep)
    return dependencies


setup(
    name="anitya_schema",
    version=get_project_version(),
    description="JSON schema definitions for messages published by Anitya",
    long_description=README,
    url="https://github.com/fedora-infra/anitya/",
    # Possible options are at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
    ],
    license="GPLv2+",
    maintainer="Fedora Infrastructure Team",
    maintainer_email="infrastructure@lists.fedoraproject.org",
    platforms=["Fedora", "GNU/Linux"],
    keywords="fedora",
    packages=find_packages(exclude=("anitya_schema.tests", "anitya_schema.tests.*")),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements(),
    test_suite="anitya_schema.tests",
    entry_points={
        "fedora.messages": [
            "anitya.distro.add=anitya_schema:DistroCreated",
            "anitya.distro.edit=anitya_schema:DistroEdited",
            "anitya.distro.remove=anitya_schema:DistroDeleted",
            "anitya.project.add=anitya_schema:ProjectCreated",
            "anitya.project.edit=anitya_schema:ProjectEdited",
            "anitya.project.remove=anitya_schema:ProjectDeleted",
            "anitya.project.flag=anitya_schema:ProjectFlag",
            "anitya.project.flag.set=anitya_schema:ProjectFlagSet",
            "anitya.project.map.new=anitya_schema:ProjectMapCreated",
            "anitya.project.map.update=anitya_schema:ProjectMapEdited",
            "anitya.project.map.remove=anitya_schema:ProjectMapDeleted",
            "anitya.project.version.update=anitya_schema:ProjectVersionUpdated",
            "anitya.project.version.update.v2=anitya_schema:ProjectVersionUpdatedV2",
            "anitya.project.version.remove=anitya_schema:ProjectVersionDeleted",
        ]
    },
)
