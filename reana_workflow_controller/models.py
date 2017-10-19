# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

"""Models for REANA Workflow Controller."""

from __future__ import absolute_import

import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String
# move to factory
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy_utils.types import UUIDType

Base = declarative_base()


class User(Base):
    """User table"""

    __tablename__ = 'user'

    id_ = Column(UUIDType, primary_key=True)
    api_key = Column(String(length=120))
    create_date = Column(DateTime, default=func.now)
    email = Column(String(length=255))
    last_active_date = Column(DateTime, default=func.now)
    workflows = relationship("workflows", backref="user")

    def __repr__(self):
        """User string represetantion."""
        return '<User %r>' % self.id_


class WorkflowStatus(enum.Enum):
    running = 1
    finished = 2
    failed = 3


class Workflow(Base):
    """Workflow table."""

    __tablename__ = 'workflow'

    id_ = Column(UUIDType, primary_key=True)
    create_date = Column(DateTime, default=func.now)
    workspace_path = Column(String(255))
    status = Column(Enum(WorkflowStatus))
    owner_id = Column(UUIDType, ForeignKey('user.id_'))

    def __repr__(self):
        """Workflow string represetantion."""
        return '<Workflow %r>' % self.id_
