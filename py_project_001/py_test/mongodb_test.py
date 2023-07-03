"""python的MongoDB"""
"""
目前最流行的非关系数据库
"""

import pymongo


def connect_mongo():
    """连接数据库"""
    myclient = pymongo.MongoClient('localhost',27017)
    print(myclient)
    return myclient
def creat_mongo(myclient:pymongo.MongoClient,basename,listname):
    """创建数据库"""
    mydb = myclient[basename]
    mycol = mydb[listname]
    """
    注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 
    就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
    """

def bool_mongo(myclient:pymongo.MongoClient,mongoname:str):
    """判断数据库是不是已经存在"""
    dblist = myclient.list_database_names()
    print(dblist)
    if mongoname in dblist:
        print("数据库存在")
        return True
    else:
        print("数据库不存在")
        return False
def add_mongo(myclient:pymongo.MongoClient):
    mydb = myclient['admin']
    mycol = mydb['sites']
    mydict={"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
    x=mycol.insert_one(mydict)
    print(x)





if __name__ == '__main__':
    basename = 'mydb'
    listname = 'sites'
    client=connect_mongo()
    creat_mongo(client,basename,listname)
    bool_base =bool_mongo(client,basename)
    add_mongo(client)
