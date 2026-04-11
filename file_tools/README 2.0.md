# README 2.0

## file_tools

### pdf_tool.py 自动化办公——PDF 合并与加密工具

#### 目标：批量合并多个 PDF 文件，并统一加上访问密码。

1. 读取目标文件夹，并提取所有PDF文件
2. 逐个读取PDF文件的每一页，并添加到新的writer文件中实现多个PDF文件的合并
3. 加密
4. 保存文件

* os

* from PyPDF2 import Pdfreader, Pdfwriter

* files=[f for f in os.listdir(folder_path) if endswith(".pdf")] 筛选PDF文件

  
  
  

### rename.py 入门级加密与解密——文件名的混淆与还原

#### 目标：混淆器：把文件夹所有文件改名，并用.json文件记录原名；还原器：读取.json文件把文件名还原。

1. <u>构造.json文件的路径，并检查是否存在.json文件（文件可能已处于混淆状态）</u>
2. 读取目标文件夹中的所有文件
3. 修改文件名字和类型（可自定义）
4. 把新-旧名字对应关系存入.json文件中（严格意义上它不应该放在目标文件夹里）
5. 读取.json文件，由键（新名）找到对应的值（旧名）
6. 删除.json文件

* os

* <u>import json 用来储存键值对（新名-旧名）</u>

* path.exists() 检查路径是否存在，path.join() 构造完整路径，path.isfile() 检查是否为文件

* <u>json.dump() 把python数据写入json文件</u>

  

  

### classify.py 文件自动分类器

#### 目标：根据文件后缀名，自动移动到指定文件夹

1. 自定义文件夹的设定规则（图片、视频、文档......）
2. 读取目标文件夹中的所有文件（不包括下属文件夹），把文件名拆分提取后缀名
3. 根据后缀名把文件放进新的文件夹

* os
* path.splitext() 拆分文件名得到后缀名
* makedirs() 创建新文件夹





### duplicate.py

#### 目标：扫描一个文件夹，找出内容完全一模一样的文件（即使名字不同），并把多余的删掉。