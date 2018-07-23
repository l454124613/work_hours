# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, TIMESTAMP, Date, Boolean
from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.sql import func
from module.database import Base


class MTask(Base):
    __tablename__ = 'p_task'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    plan_start_time = Column(Date)
    plan_end_time = Column(Date)
    status = Column(Integer, index=True,server_default='1')
    level = Column(Integer)
    create_time = Column(TIMESTAMP, server_default=func.now())
    user_id = Column(Integer, ForeignKey('p_user.id'))
    user_name = Column(String(32))
    item_id = Column(Integer, ForeignKey('p_item.id'), index=True)
    work_details = relationship('MWorkDetail', backref='task')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def to_json(self):
        return {"id": self.id, "name": self.name, "plan_start_time": self.plan_start_time,
                "plan_end_time": self.plan_end_time,
                "status": self.status, "level": self.level, "create_time": self.create_time, "user_id": self.user_id,
                "item_id": self.item_id, "work_details": self.work_details, "user_name": self.user_name}
