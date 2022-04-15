import re
import os
import json
import pandas as pd

def IsIn(name):
    flag = False
    status = []
    if name in IEEEFellowListLF:
        flag = True
        status.append('IEEE LF')
    if name in IEEEFellowListFL:
        flag = True
        status.append('IEEE FL')
    if name in ACMFellowListLF:
        flag = True
        status.append('ACM LF')
    if name in ACMFellowListFL:
        flag = True
        status.append('ACM FL')
    return flag, status


PaperWithFellowCite = {}
# 打开IEEEFellow文件并保存到IEEEFellow列表
IEEEFellowFile = open('IEEEFellows.txt', 'r')
IEEEFellowText = IEEEFellowFile.read()
IEEEFellowText = IEEEFellowText.lower()

IEEEFellowListLF = json.loads(IEEEFellowText)

# 把IEEEFellow名单换成姓在前
IEEEFellowListFL = IEEEFellowListLF.copy()
for i in range(len(IEEEFellowListFL)):
    lastName, FirstName = IEEEFellowListFL[i].split(', ')
    IEEEFellowListFL[i] = '{}, {}'.format(FirstName, lastName)

# 打开ACMFellow文件并保存到ACMFellow列表
ACMFellowFile = open('ACMFellows.txt', 'r')
ACMFellowText = ACMFellowFile.read()
ACMFellowText = ACMFellowText.lower()

ACMFellowListLF = json.loads(ACMFellowText)

# 把ACMFellow名单换成姓在前
ACMFellowListFL = ACMFellowListLF.copy()
for i in range(len(ACMFellowListFL)):
    lastName, FirstName = ACMFellowListFL[i].split(', ')
    ACMFellowListFL[i] = '{}, {}'.format(FirstName, lastName)

dirs = os.listdir('PapersExcel')
# 逐个处理被引文章
# 被引文章名字
for item in range(len(dirs)):
    paperName = dirs[item][:-4]
    PaperWithFellowCite[paperName] = {'count': 0, 'detail': []}
    # 打开被引文章引用记录并保存到引用记录列表
    citeDF = pd.read_excel('PapersExcel/' + dirs[item], header = None)
    citeDF.columns = citeDF.iloc[27]
    citeDF = citeDF[28:]
    for i in range(len(citeDF)):
        # 处理每篇施引
        # 找到施引文章作者字段
        eachCiteAuthorText = citeDF.iloc[i]['作者']
        # 拆分到列表
        eachCiteAuthorList = eachCiteAuthorText.split('; ')
        # 找到施引文章标题字段
        eachCiteTitleText = citeDF.iloc[i]['标题']
        eachCiteDict = {}
        eachCiteDict['Fellows'] = []
        for j in range(len(eachCiteAuthorList)):
            eachCiteAuthorItem = eachCiteAuthorList[j].lower()
            isFound, whereFound = IsIn(eachCiteAuthorItem)
            if isFound:
                    eachCiteDict['Fellows'].append("{}({})".format(eachCiteAuthorList[j], " ".join(whereFound)))
        if len(eachCiteDict['Fellows']) > 0: 
            eachCiteDict['CitePaper'] = eachCiteTitleText
            eachCiteDict['Authors'] = eachCiteAuthorList
            PaperWithFellowCite[paperName]['detail'].append(eachCiteDict)
            PaperWithFellowCite[paperName]['count'] += 1

PaperWithFellowCiteText = json.dumps(PaperWithFellowCite)
PaperWithFellowCiteFile = open('Top131Excel.txt', 'w')
PaperWithFellowCiteFile.write(PaperWithFellowCiteText)
PaperWithFellowCiteFile.close()
print(PaperWithFellowCite)