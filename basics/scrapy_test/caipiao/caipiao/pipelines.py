# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo
from caipiao.settings import MYSQL


# csv
class CaipiaoPipeline:
    def open_spider(self, spider):
        self.f = open("./双色球.csv", mode="a", encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        self.f.write(f"{item['qihao']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")
        return item


# mysql
class CaipiaoMySQLPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=MYSQL['host'],
            port=MYSQL['port'],
            user=MYSQL['user'],
            password=MYSQL['password'],
            database=MYSQL['database']
        )

    def close_spider(self, spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao (qihao,red_ball,blue_ball) values (%s,%s,%s)"
            cursor.execute(sql, (item['qihao'], "_".join(item['red_ball']), item['blue_ball']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item


# mongodb
class CaipiaoMongoDBPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="", port=27017)
        db = self.client['']  # 库
        db.authenticate = ["", ""]  # 用户名密码
        self.collection = db['']  # 集合

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.inert(
            {"qihao": item['qihao'], "red_ball": "_".join(item['red_ball']), "blue_ball": item['blue_ball']})
        return item
