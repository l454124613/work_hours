# -*- coding:utf-8 -*-
# Author:lixuecheng
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://test:AAAaaa1234@10.66.4.101:3308/ciic_project", max_overflow=5)
Base = declarative_base()


