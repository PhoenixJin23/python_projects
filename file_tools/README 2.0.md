# README 2.0

## file_tools

### pdf_tool.py PDF 合并与加密工具

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







### folder_analyzer.py 文件夹大小可视化分析仪

#### 目标：扫描一个文件夹，计算每个子文件夹的大小，并画出一个饼图。

1. 先构造计算文件夹大小的工具函数
2. <u>打开文件夹，找到目标文件夹下的文件夹，对它们调用计算文件夹大小的函数</u>
3. 绘制饼状图

* import matplotlib.pyplot as plt
* os
* <u>os.walk() 递归的深度搜索，可以得到目标文件夹所有（每一层）下属的文件（夹），而 os.listdir() 只能看到第一层</u>
* path.getsize() 返回的是Byte单位 1KB=1024Byte, 1MB=1024KB
* get_folder_size(folder_path)是被analyze_disk_usage(target_dir)调用的工具函数，folder_path是target_dir目标文件夹下属的文件夹路径
* plt.rcParams['font.sans-serif']=['SimHei'] 设置中文字体防止绘图时乱码





### image_processor.py 图片批量缩放与水印工具

#### 目标：自动读取文件夹里的图片，统一缩小尺寸并打上你的名字水印。

1. 创建/打开输出文件夹
2. 打开目标文件夹，检查后缀，只处理图片
3. 打开图片，缩放图片，为图片加上滤镜
4. 保存图片到输出文件夹

* from PIL import Image, ImageDraw, ImageFont
* os
* img.resize((width,height))
* draw.text() 实质是在图片上绘制文字