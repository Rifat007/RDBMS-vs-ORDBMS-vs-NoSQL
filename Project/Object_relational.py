from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable

import logging


class User(BaseTable):
    __table_name__ = 'users'

    id = IntegerField(primary_key=True, auto_increment=True) #Р°РІС‚РѕРёРЅРєСЂРµРјРµРЅС‚ РЅР° int РїРѕР»Рµ
    name = TextField(not_null=True)
    active = BooleanField(not_null=True, default_value=1)


class Post(BaseTable):
    __table_name__ = 'posts'

    id = IntegerField(primary_key=True)
    name = TextField(not_null=True)
    id_user = IntegerField(foreign_key=User.id)


if __name__ == '__main__':

    #logger configure:
    logging.basicConfig(filename="sample.log", level=logging.DEBUG, format=('%(asctime)s: '
                                                                            '%(filename)s: '
                                                                            '%(levelname)s: '
                                                                            '%(funcName)s(): '
                                                                            '%(lineno)d: '
                                                                            '%(message)s'), datefmt="%Y-%m-%d %H:%M:%S")
    with Database("test.db") as db:
        # create table
        #db.query(Post, User).create().execute()

        user1 = User(id=1, name='User1')
        user2 = User(id=2, name='User2')
        user3 = User(id=3, name='User3')

        post1 = Post(id=1, name='Post1', id_user=user1.id)
        post2 = Post(id=2, name='Post2', id_user=user2.id)
        post3 = Post(id=3, name='Post3', id_user=user3.id)

        #insert data
        #db.query().insert(user1, user2, user3, post1, post2, post3).execute()

        # select with columns + autojoin with fk;
        print('\n=======SELECT + Auto Join=======')
        for row in db.query(User.name, Post.name).select().join(Post).execute():
            print(row)
##
##        # update
##        db.query(User).update(name='User3_UPDATED').filter(User.name == 'User3').execute()
##
##        print('\n=======SELECT after update=======')
##        for row in db.query(User, Post.name).select().join(Post).execute():
##            print(row)
##
##        db.query(User).delete().filter(User.name == 'User3_UPDATED').execute()
##
##        print('\n=======SELECT after delete=======')
##        for row in db.query(User, Post.name).select().join(Post).execute():
##            print(row)
##
##        # delete
##        db.query(User, Post).drop().execute()
