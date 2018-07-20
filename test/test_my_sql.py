# -*- coding:utf-8 -*-
# Author:lixuecheng

from sqlalchemy.orm import sessionmaker
from faker import Factory
from module import item, log, task, user, word_detail, work_log
import random
from module.database import engine,Base

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    faker = Factory.create()
    Session = sessionmaker(bind=engine)
    session = Session()
    faker_users = [user.MUser(name=faker.name(), password=faker.word(), auth_content=faker.sentence()) for i in
                   range(10)]
    session.add_all(faker_users)
    faker_items = [item.MItem(name=faker.sentence(),
                              des=' '.join(faker.sentences(nb=random.randint(10, 20))),
                              user=random.choice(faker_users)) for i in range[5]]
    session.add_all(faker_items)
    faker_task = [task.MTask(name=faker.sentence(),
                             plan_start_time=faker.date(),
                             plan_end_time=faker.date(),
                             level=1,
                             user=random.choice(faker_users),
                             item=random.choice(faker_items)
                             )]
    session.add_all(faker_task)
    faker_logs = [log.MLog(method=random.choice(['post', 'get', 'put', 'delete']),
                           path='\\' + faker.word(),
                           token=faker.word(),
                           get_info=faker.sentence(),
                           send_info=faker.sentence(),
                           user=random.choice(faker_users)
                           ) for i in range(50)]
    session.add_all(faker_logs)
    faker_w_logs = [work_log.MWorkLog(commit_date=faker.date(),
                                      all_hours=faker.month(),
                                      user=random.choice(faker_users)
                                      ) for i in range(20)]
    session.add_all(faker_w_logs)
    for i in range(50):
        faker_w_de = word_detail.MWorkDetail(commit_date=faker.date(),
                                             name=faker.sentence(),
                                             hours=faker.month(),
                                             user=random.choice(faker_users),
                                             item=random.choice(faker_items),
                                             task=random.choice(faker_task)

                                             )
        session.add(faker_w_de)

    session.commit()
