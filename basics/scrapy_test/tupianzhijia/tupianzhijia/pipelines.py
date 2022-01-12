# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class TupianzhijiaPipeline:
    def process_item(self, item, spider):
        return item


class MeinvSavePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split("/")[-1]
        return f"meinv/{file_name}"

    def item_completed(self, results, item, info):
        print(results)
