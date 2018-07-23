# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, TIMESTAMP, Date, Boolean
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.sql import func
from module.database import Base


class MWorkLog(Base):
    __tablename__ = 'p_work_log'
    id = Column(Integer, primary_key=True)
    commit_date = Column(Date, index=True)
    all_hours = Column(Integer, index=True)
    create_time = Column(TIMESTAMP, server_default=func.now())
    user_id = Column(Integer, ForeignKey('p_user.id'), index=True)
    user_name = Column(String(32))
    work_details = relationship('MWorkDetail', backref='Work_logs')
    status = Column(Integer, server_default="1")

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def to_json(self):
        return {"id": self.id, "commit_date": self.commit_date, "all_hours": self.all_hours,
                "create_time": self.create_time, "user_id": self.user_id, "user_name": self.user_name}
