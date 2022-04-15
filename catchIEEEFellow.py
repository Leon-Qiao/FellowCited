import requests
from urllib.parse import urlencode
from lxml import etree
import json
import time
import random

fellowList = []
url = "https://services27.ieee.org/fellowsdirectory/getpageresultsdesk.html"

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

for i in range(1, 646):
    time.sleep(random.randint(1,3))
    datas = {
        "selectedJSON": (None, '{"alpha":"ALL","menu":"ALPHABETICAL","gender":"All","currPageNum":1,"breadCrumbs":[{"breadCrumb":"Alphabetical+Listing+"}],"helpText":"Click+on+any+of+the+alphabet+letters+to+view+a+list+of+Fellows."}'),
        "inputFilterJSON": (None, '{"sortOnList":[{"sortByField":"fellow.lastName","sortType":"ASC"}],"requestedPageNumber":"1","typeAhead":False}'),
        "pageNum": (None, str(i))
    }
    page_html = requests.request("POST", url, files=datas) 
    page_text = page_html.text
    xPathHtml = etree.HTML(page_text)
    html_data = xPathHtml.xpath('//div[@class="td name"]/a/span/text()')
    fellowList = fellowList + html_data
    print(i, html_data)

fellowJson = json.dumps(fellowList)
fellowFile = open('IEEEFellows.txt', 'w')
fellowFile.write(fellowJson)
fellowFile.close()