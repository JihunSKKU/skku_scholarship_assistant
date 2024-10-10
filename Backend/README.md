# BackEnd README

## How to Use Scrapy in This Project

1. Open `.\skku_notice\skku_notice\spiders\skku_notice_spider.py`.
2. Set the `start_urls` variable to the domain you want to scrape.
3. Adjust `max_notices` to control the number of notices to scrape.
4. Run the following command to start scraping:
    ```bash
    cd skku_notice
    scrapy crawl skku_notice -o notices.json
    ```
5. The scraped results will be stored in notices.json.

## ETC

TBD
