from lxml import etree
import re
import json

page_file = open('Recipients.txt', 'r', encoding='utf-8')
page_text = page_file.read()
xPathHtml = etree.HTML(page_text)
fellowList = xPathHtml.xpath('//tr/td/a/text()')
while 'ACM Fellows' in fellowList:
    fellowList.remove('ACM Fellows')
for i in range(len(fellowList)):
    fellowList[i] = fellowList[i].replace('\xa0', ' ')

fellowJson = json.dumps(fellowList)
fellowFile = open('ACMFellows.txt', 'w')
fellowFile.write(fellowJson)
fellowFile.close()
print(fellowList)