import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    allowed_domains = ['https://www.nytimes.com']
    start_urls = [
        # 'http://https://www.nytimes.com/',
        'https://www.nytimes.com/2021/03/29/us/politics/transgender-girls-sports.html',
        # 'https://www.nytimes.com/2021/03/28/us/politics/patty-murray-rosa-delauro-stimulus.html',
        ]

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        paragraphs=response.css('.css-53u6y8 > p::text').getall()
        author=response.css('.css-1sowyjy a::text').extract()
        # #Extract data using xpath
        category=response.css('.css-1wr3we4 a::text').extract()
        pub_date=response.css('time .css-1sbuyqj::text').extract()
        pub_tim=response.css('.css-epvm6::text').extract()

        # row_data=zip(paragraphs,author,category,pub_date,pub_tim)
        row_data=zip(paragraphs, category)

        print('paragraphs'+ str(len(paragraphs)))
        print(paragraphs[1])


        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'paragraphs' : paragraphs, #item[0] means product in the list and so on, index tells what value to assign
                'author' : author,
                'category' : category,
                'pub_date' : pub_date,
                'pub_tim' : pub_tim,
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
