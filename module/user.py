# -*- coding:utf-8 -*-
# Author:lixuecheng
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, TIMESTAMP
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

engine = create_engine("mysql+pymysql://test:AAAaaa1234@10.66.4.101:3308/ciic_project", max_overflow=5)
Base = declarative_base()


class MUsers(Base):
    __tablename__ = 'p_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    vid = Column(Integer, server_default='0')
    create_time = Column(TIMESTAMP, server_default=func.now())

    def __repr__(self):
        return '{"id": %s, "name": "%s","vid":%s}' % (self.id, self.name, self.vid)

    def toJson(self):
        return {"id": self.id, "name": self.name, "vid": self.vid}

    # def __str__(self):
    #     return '{"id": %s, "name": "%s","vid":%s}' % (self.id, self.name, self.vid)


Base.metadata.create_all(engine)
