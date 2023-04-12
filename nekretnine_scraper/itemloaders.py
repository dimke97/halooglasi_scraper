from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class HalloAddLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: x.split("\\")[0])
