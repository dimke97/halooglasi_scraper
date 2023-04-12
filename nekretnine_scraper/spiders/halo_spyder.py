import scrapy
from .. items import NekretnineScraperItem
from .. itemloaders import HalloAddLoader


class HaloSpyderSpider(scrapy.Spider):
    name = "halo_spyder"
    page_number = 2
    start_urls = [
        "https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd"]

    def parse(self, response):
        for apartment in response.css('.my-product-placeholder'):
            halo_loader = HalloAddLoader(item=NekretnineScraperItem(), selector=apartment)
            halo_loader.add_css('title', '.product-title a::text')
            halo_loader.add_css('price', '.central-feature i::text')
            halo_loader.add_css('sqr_m', '.col-p-1-3:nth-child(1) .value-wrapper::text')
            halo_loader.add_css('room_num', '.col-p-1-3:nth-child(2) .value-wrapper::text')
            halo_loader.add_css('floor', '.col-p-1-3~ .col-p-1-3+ .col-p-1-3 .value-wrapper::text')
            halo_loader.add_css('description', '.short-desc::text')
            halo_loader.add_css('publish_date', '.publish-date::text')
            halo_loader.add_css('ad_owner', '.basic-info span::text')
            halo_loader.add_css('city', '.subtitle-places li:nth-child(1)::text')
            halo_loader.add_css('municipality', '.subtitle-places li:nth-child(2)::text')
            halo_loader.add_css('suburb', '.subtitle-places li:nth-child(3)::text')
            halo_loader.add_css('street', '.subtitle-places li:nth-child(4)::text')
            halo_loader.add_css('url_link', '.product-title a::attr(href)')
            
            yield halo_loader.load_item()

            next_page = f'https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd?page={str(HaloSpyderSpider.page_number)}'
            if HaloSpyderSpider.page_number <= 284:
                HaloSpyderSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse) 