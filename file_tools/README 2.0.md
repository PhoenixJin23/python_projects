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

  