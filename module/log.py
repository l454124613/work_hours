# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, TIMESTAMP, Text


from sqlalchemy.sql import func
from module.database import Base


class MLog(Base):
    __tablename__ = 'p_log'
    id = Column(Integer, primary_key=True)
    method = Column(String(6))
    path = Column(String(32))
    token = Column(String(255))
    create_time = Column(TIMESTAMP, server_default=func.now(), index=True)
    get_info = Column(Text)
    send_info = Column(Text)
    user_id = Column(Integer, ForeignKey('p_user.id'), index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

    def to_json(self):
        return {"id": self.id, "method": self.method, "path": self.path, "token": self.token,
                "create_time": self.create_time, "get_info": self.get_info, "send_info": self.send_info,
                "vid": self.user_id}
