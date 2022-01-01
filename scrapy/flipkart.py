import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple',
    ]

    def parse(self, response):
        nodes = response.xpath("//div[@class='_2kHMtA']")
        for quote in nodes:
            yield {
                'Name': quote.xpath(".//div[@class='_4rR01T']/text()").get(),
                'Link': f"https://www.flipkart.com{quote.xpath('.//a/@href').get()}",
                'Rating': quote.xpath(".//div[@class='_3LWZlK']/text()").get(),
                'Rating Count': quote.xpath(".//span[@class='_2_R_DZ']/span/span[1]/text()").get(),
                'Review Count': quote.xpath(".//span[@class='_2_R_DZ']/span/span[3]/text()").get(),
                'Details': quote.xpath(".//ul[@class='_1xgFaf']/li/text()").getall(),
                'Images': quote.xpath(".//div[@class='CXW8mj']/img/@src").get(),
                'Sale Price': quote.xpath(".//div[@class='_30jeq3 _1_WHN1']/text()").get(),
                'List Price': quote.xpath(".//div[@class='_3I9_wc _27UcVY']/text()[2]").get(),
                'Discount': quote.xpath(".//div[@class='_3Ay6Sb']/span/text()").get(),
                'Delivery': quote.xpath(".//div[@class='_2Tpdn3']/text()").get(),
                'Exchange': quote.xpath(".//div[@class='_3xFhiH']/div[2]/text()").get(),
            }

        next_url = response.xpath("//a[@class='_1LKTO3'][last()]/@href").get()
        next_page = f"https://www.flipkart.com{next_url}"
        if next_page is not None:
            yield response.follow(next_page, self.parse)

