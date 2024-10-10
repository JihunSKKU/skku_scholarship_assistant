import scrapy

class SkkuNoticeSpider(scrapy.Spider):
    name = 'skku_notice'
    allowed_domains = ['skku.edu']
    start_urls = ['https://www.skku.edu/skku/campus/skk_comm/notice06.do']
    notice_count = 0  # Counter to track the number of notices processed
    max_notices = 30  # Limit the number of notices to crawl

    def parse(self, response):
        links = response.css('dt.board-list-content-title a::attr(href)').getall()
        for link in links:
            if self.notice_count < self.max_notices:
                full_link = response.urljoin(link)
                self.notice_count += 1
                yield response.follow(full_link, callback=self.parse_notice)
            else:
                break  # Stop further processing if the limit is reached

        # Handle pagination only if the max notices limit hasn't been reached
        if self.notice_count < self.max_notices:
            next_page = response.css('a.pg_next::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

    def parse_notice(self, response):
        title = response.css('em.ellipsis::text').get(default='Title not found').strip()
        content = response.css('pre.pre::text').get(default='Content not found').replace('\r\n', ' ').strip()
        yield {
            'title': title,
            'link': response.url,
            'content': content
        }
