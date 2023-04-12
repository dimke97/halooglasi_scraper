import scrapy
from .. items import NekretnineScraperItem


class HaloSpyderSpider(scrapy.Spider):
    name = "halo_spyder"
    page_number = 2
    start_urls = [
        "https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd"]

    def parse(self, response):
        items = NekretnineScraperItem()

        for apartment in response.css('.my-product-placeholder'):
            title = apartment.css('.product-title a').css('::text').get()
            price = apartment.css('.central-feature i::text').get().replace(u'\xa0', u'')
            sqr_m = apartment.css('.col-p-1-3:nth-child(1) .value-wrapper::text').get().replace(u'\xa0m', u'')
            room_num = apartment.css('.col-p-1-3:nth-child(2) .value-wrapper::text').get().replace(u'\xa0', u'')
            floor = apartment.css('.col-p-1-3~ .col-p-1-3+ .col-p-1-3 .value-wrapper::text').get()
            if floor is not None:
                floor = floor.replace(u'\xa0', u'')
            description = apartment.css('.short-desc::text').get()
            publish_date = apartment.css('.publish-date::text').get()
            ad_owner = apartment.css('.basic-info span::text').get()
            city = apartment.css('.subtitle-places li:nth-child(1)').css('li::text').get()
            municipality = apartment.css('.subtitle-places li:nth-child(2)').css('li::text').get()
            suburb = apartment.css('.subtitle-places li:nth-child(3)').css('li::text').get()
            street = apartment.css('.subtitle-places li:nth-child(4)').css('li::text').get()
            
            items['title'] = title
            items['price'] = price
            items['sqr_m'] = sqr_m
            items['room_num'] = room_num
            items['floor'] = floor
            items['description'] = description
            items['publish_date'] = publish_date
            items['ad_owner'] = ad_owner
            items['city'] = city
            items['municipality'] = municipality
            items['suburb'] = suburb
            items['street'] = street
            
            yield items

            next_page = f'https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd?page={str(HaloSpyderSpider.page_number)}'
            if HaloSpyderSpider.page_number <= 285:
                HaloSpyderSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse) 