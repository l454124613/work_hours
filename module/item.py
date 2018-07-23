# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Text, Boolean,ForeignKeyConstraint
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func
from module.database import Base


class MItem(Base):
    __tablename__ = 'p_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    des = Column(Text, nullable=True)
    status = Column(Integer, index=True, server_default='1')
    create_time = Column(TIMESTAMP, server_default=func.now())
    user_id = Column(Integer, ForeignKey('p_user.id'))
    user_name = Column(String(32))
    tasks = relationship('MTask', backref='item')
    work_details = relationship('MWorkDetail', backref='item')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def to_json(self):
        return {"id": self.id, "name": self.name, "des": self.des, "status": self.status,
                "create_time": self.create_time, "user_id": self.user_id, "user_name": self.user_name}
