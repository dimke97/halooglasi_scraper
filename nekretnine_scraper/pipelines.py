# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from datetime import datetime


class PriceConvertPipeline:
    """Konvertuje cenu u float"""
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
            adapter['price'] = float(adapter['price'])
            return item
        else:
            raise DropItem(f"Missing price in {item}")
        
        
class SqrMConvertPipeline:
    """Konvertuje kvadraturu u float"""
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('sqr_m'):
            adapter['sqr_m'] = float(adapter['sqr_m'])
            return item
        else:
            raise DropItem(f"Missing sqr_m in {item}")
        
        
class RoomNumConvertPipeline:
    """Konvertuje broj soba u float"""
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('room_num'):
            adapter['room_num'] = float(adapter['room_num'])
            return item
        else:
            raise DropItem(f"Missing room number in {item}")


class PublishDateConvertPipeline:
    """Konvertuje datum objave u adekvatan format"""
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('publish_date'):
            adapter['publish_date'] = datetime.strptime(adapter['publish_date'], '%d.%m.%Y.').date()
            return item
        else:
            raise DropItem(f"Missing Publish date in {item}")