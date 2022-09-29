import scrapy
from scrapy.http import Response
import json


class NewsroomSpider(scrapy.Spider):
    name = "newsroom"
    allowed_domains = ["railroads.dot.gov"]
    start_urls = ["https://railroads.dot.gov/newsroom/press-releases"]

    def parse(self, response: Response):
        selectors: scrapy.SelectorList = response.css(".title--news-item").css("a")
        for selector in selectors:
            title = selector.css("::text").get()
            path = selector.attrib["href"]
            print(
                json.dumps({"title": title, "link": f"https://railroads.dot.gov{path}"})
            )
