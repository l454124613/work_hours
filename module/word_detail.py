# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Date, Boolean, ForeignKeyConstraint

from sqlalchemy.sql import func
from module.database import Base


class MWorkDetail(Base):
    __tablename__ = 'p_Work_Detail'
    id = Column(Integer, primary_key=True, index=True)
    commit_date = Column(Date, index=True)
    name = Column(String(64))
    hours = Column(Integer, index=True)

    create_time = Column(TIMESTAMP, server_default=func.now())
    user_id = Column(Integer, ForeignKey('p_user.id'), index=True)
    user_name = Column(String(32))
    item_id = Column(Integer, ForeignKey('p_item.id'), index=True)
    task_id = Column(Integer, ForeignKey('p_task.id'), index=True)
    work_log_id = Column(Integer, ForeignKey('p_work_log.id'), index=True)
    status = Column(Integer, server_default="1")

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def toJson(self):
        return {"id": self.id, "name": self.name, "commit_date": self.commit_date, "hours": self.hours,
                "create_time": self.create_time,
                "user_id": self.user_id, "item_id": self.item_id, "task_id": self.task_id, "user_name": self.user_name}
