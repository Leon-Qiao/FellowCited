import re
import os
import json

PaperWithFellowCite = {}
# 打开fellow文件并保存到fellow列表
fellowFile = open('Fellows.txt', 'r')
fellowText = fellowFile.read()
fellowText = fellowText.lower()

fellowListLF = json.loads(fellowText)

# 把fellow名单换成姓在前
fellowListFL = fellowListLF.copy()
for i in range(len(fellowListFL)):
    lastName, FirstName = fellowListFL[i].split(', ')
    fellowListFL[i] = '{}, {}'.format(FirstName, lastName)

dirs = os.listdir('Papers')
# 逐个处理被引文章
# 被引文章名字
for item in range(len(dirs)):
    paperName = dirs[item][:-4]
    PaperWithFellowCite[paperName] = {'count': 0, 'detail': []}
    # 打开被引文章引用记录并保存到引用记录列表
    citeFile = open('Papers/' + dirs[item], 'r', encoding = 'utf-8')
    citeRawString = citeFile.read()
    citeFile.close()
    citeRawString = citeRawString[citeRawString.find('PT'):]
    citeList = citeRawString.split('ER\n\n')
    for i in range(len(citeList)):
        # 处理每篇施引
        eachCiteText = citeList[i]
        # 找到施引文章作者字段
        eachCiteAuthorText = eachCiteText[eachCiteText.find('AU ') + 2: eachCiteText.find('\nTI ')]
        # 去掉多余空格
        eachCiteAuthorText = re.sub(' +', ' ', eachCiteAuthorText)
        # 拆分到列表
        eachCiteAuthorList = eachCiteAuthorText.split('\n ')
        eachCiteAuthorList[0] = eachCiteAuthorList[0][1:]

        # 找到施引文章标题字段
        eachCiteTitleText = eachCiteText[eachCiteText.find('TI ') + 2: eachCiteText.find('\nSO ')]
        # 拍平成一行
        eachCiteTitleText = eachCiteTitleText.replace('\n', '')
        # 去掉多余空格
        eachCiteTitleText = re.sub(' +', ' ', eachCiteTitleText)[1:]

        for j in range(len(eachCiteAuthorList)):
            eachCiteAuthorItem = eachCiteAuthorList[j].lower()
            eachCiteDict = {}
            if eachCiteAuthorItem in fellowListLF: # or eachCiteAuthorItem in fellowListFL
                if 'Fellows' in eachCiteDict:
                    eachCiteDict['Fellows'].append(eachCiteAuthorList[j])
                else:
                    eachCiteDict['Fellows'] = [eachCiteAuthorList[j]]
        if 'Fellows' in eachCiteDict: 
            eachCiteDict['CitePaper'] = eachCiteTitleText
            eachCiteDict['Authors'] = eachCiteAuthorList
            PaperWithFellowCite[paperName]['detail'].append(eachCiteDict)
            PaperWithFellowCite[paperName]['count'] += 1

PaperWithFellowCiteText = json.dumps(PaperWithFellowCite)
PaperWithFellowCiteFile = open('Top38.txt', 'w')
PaperWithFellowCiteFile.write(PaperWithFellowCiteText)
PaperWithFellowCiteFile.close()
print(PaperWithFellowCite)