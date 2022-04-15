# FellowCited

## 下载ACM Fellow信息

https://awards.acm.org/fellows/award-winners

将网页源代码复制到文件Recipients.txt中

执行catchACMFellow.py创建ACMFellows.txt文件

## 下载IEEE Fellow信息

执行catchIEEEFellow.py创建IEEEFellows.txt文件

## 下载作者论文列表

打开webofscience.com

搜索作者名字

在论文列表中逐个点击被引频次查看引用列表

点击引文报告，点击导出完整的引文报告

如果选择Excel文件，所有Excel保存到PapersExcel文件夹

如果选择文本文件，所有txt保存到Papers文件夹

执行RenameExcel.py将所有Excel文件重命名为论文名

## 引用数据提取

根据刚才下载的文件类型选择执行


Demo_ExcelVersion.py

或者

Demo_TxtVersion.py

## 分析结果展示

执行show.py生成分析结果文件showCite.txt

## 注意

该方法只是基于引用作者的名字对比实现

需要手动根据单位、邮箱等信息确认是否是Fellow本人