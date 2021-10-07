import scrapy
import re

reviews_url = 'https://www.sosnc.gov/online_services/Search/Business_Registration_profile?Id={}'

asin_list = []

def cleanup(input_string):
    if input_string:
        return re.sub(r'[//]','',input_string).strip()

class RewiewsSpider(scrapy.Spider):
    name = 'rewiews'

    def start_requests(self):
        for asin in asin_list:
            url = reviews_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        Name = cleanup(response.xpath('//section/div/span[2]/text()').get())
        SosId = cleanup(response.xpath('//span[text()="SosId: "]/following-sibling::span[1]/text()').get())
        Status = cleanup(response.xpath('//span[text()="Status: "]/following-sibling::span[1]/text()').get())
        DateFormed = cleanup(response.xpath('//section[2]/div/span[7]/text()').get())
        Citizenship = cleanup(response.xpath('//section[2]/div/span[9]/text()').get())
        FiscalMonth = cleanup(response.xpath('//section[2]/div/span[11]/text()').get())
        AnnualReportDueDate = cleanup(response.xpath('//section[2]/div/span[13]/text()').get())
        OwnerPrincipal = cleanup(response.xpath('//span/a[@itemprop="url"]/text()').get())
        PrincipalAdress = cleanup(response.xpath('//section[3]/p/span[2]/text()').get())
        City = cleanup(response.xpath('//section[3]/p/span[2]/text()[2]').get())
        State = response.xpath('(//span[@style="margin-left: 3px;"])[1]/text()').get()
        ZipCode = response.xpath('(//span[@style="margin-left: 3px;"])[2]/text()').get()
        cl = cleanup(response.xpath('//section[5]/div/span[2]/text()').get())
        Shares = cleanup(response.xpath('//section[5]/div/span[4]/text()').get())
        NoParValue = cleanup(response.xpath('//section[5]/div/span[6]/text()').get())
        url = response.url  

        yield {
            'Name': Name,
            'SosId': SosId,
            'Status': Status,
            'DateFormed': DateFormed,
            'Citizenship': Citizenship,
            'FiscalMonth': FiscalMonth,
            'AnnualReportDueDate': AnnualReportDueDate,
            'OwnerPrincipal': OwnerPrincipal,
            'PrincipalAdress': PrincipalAdress,
            'City': City,
            'State': State,
            'ZipCode': ZipCode,
            'newClasss': cl,
            'Shares': Shares,
            'NoParValue': NoParValue,
            'URL': url
            }