import scrapy


class FMMSpider(scrapy.Spider):
    name = "FMM"
    def start_requests(self):
        urls = ["https://www.mammarzenie.org/marzyciele?status=spelnione&branch=trojmiasto"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    async def parse(self, response):
        all_wishes = response.css('ul.dreamers-archive-loop li a::attr(href)').getall()

        for wish in all_wishes:
            yield scrapy.Request(wish, callback=self.parse_single_wish)

        # next page
        no_next_page = response.css('span.page-link[rel="next"]').get()
        if not no_next_page:
            next_page = response.css('a.page-link[rel="next"]::attr(href)').get()
            yield scrapy.Request(response.urljoin(next_page))

    async def parse_single_wish(self, response):
        wish_details = [d.rstrip().strip() for d in response.css('div.event p::text').getall()]
        wish_titles = [t.rstrip().strip() for t in response.css('div.event p.text-lg::text').getall()]
        wish = response.css('div.profile-title h2::text').get().rstrip().strip()
        child_details = response.css('div.profile-cover h3::text').get().rstrip().strip()
        # TODO: fix Lukasz with div case https://www.mammarzenie.org/marzyciele/10054-%C5%81ukasz

        if "spełnienie marzenia" not in wish_titles:
            pass
        wish_grant_index = wish_details.index("spełnienie marzenia")

        wish_grant_date = wish_details[wish_grant_index+1]
        wish_grant_text = " ".join(wish_details[wish_grant_index+2:])

        yield {
            'url': response.request.url,
            'wish': wish,
            'child_details': child_details,
            'title': wish_details[wish_grant_index],
            'date': wish_grant_date,
            'details': wish_grant_text
        }
