from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class HalloAddLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: x.replace(u'\xa0', u'').replace('€', '').replace('.', ''))
    sqr_m_in = MapCompose(lambda x: x.replace(u'\xa0', u'').replace('m', '').replace(',', '.'))
    room_num_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    floor_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    ad_owner_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    city_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    municipality_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    suburb_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    street_in = MapCompose(lambda x: x.replace(u'\xa0', u''))
    url_link_in = MapCompose(lambda x: 'https://www.halooglasi.com' + x)