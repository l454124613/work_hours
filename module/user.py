# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, TIMESTAMP, Text
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.sql import func
from module.database import Base


class MUser(Base):
    __tablename__ = 'p_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    password = Column(String(64))
    vid = Column(Integer, server_default='0')
    auth_content = Column(Text)
    create_time = Column(TIMESTAMP, server_default=func.now())
    work_logs = relationship('MWorkLog', backref='users')
    work_details = relationship('MWorkDetail', backref='users')
    items = relationship('MItem', backref='users')
    tasks = relationship('MTask', backref='users')
    logs = relationship('MLog', backref='users')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def toJson(self):
        return {"id": self.id, "name": self.name, "vid": self.vid}

    # def __str__(self):
    #     return '{"id": %s, "name": "%s","vid":%s}' % (self.id, self.name, self.vid)
