import json
resultFile = open('Top131Excel.txt', 'r')
resultText = resultFile.read()
resultDic = json.loads(resultText)
S = ""
for k,v in resultDic.items():
    if v['count'] == 0:
        continue
    S += k + '\n'
    S += "count: {}".format(v['count']) + '\n'

    for i in range(len(v['detail'])):
        S += "[{}]\n Fellows: {}\n Authors: {}".format(i + 1, "、".join(v['detail'][i]['Fellows']), "、".join(v['detail'][i]['Authors'])) + '\n'
        S += " Title: {}".format(v['detail'][i]['CitePaper']) + '\n'
    S += '\n--------------------------------------------------------------------------\n'
showCiteFile = open('showCite.txt', 'w', encoding='utf-8')
showCiteFile.write(S)
showCiteFile.close()