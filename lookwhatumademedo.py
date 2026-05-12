"""🎯 核心问题复盘：为什么会混乱？
最开始的核心矛盾就是：项目虚拟环境 venv 和系统全局 Python 混在一起了。
现象：
在 VSCode 里终端会自动显示 (venv)，但 PyCharm 里没有
用 where python 看到的一直是 C:\Users\...\AppData\... 这个系统路径
pip install 的库都跑到系统里了，项目 venv 却空空如也
换个电脑 / 换个项目，库就 “不见了”，代码爆红报错
根本原因：
PyCharm 默认不会自动激活终端里的 venv
你之前一直没给项目指定专属的 venv 解释器，导致所有操作都默认用了系统 Python
系统 Python 和项目 venv 是两个完全独立的 “房间”，东西不能共用"""


"""🛠️ 关键解决步骤：一步步从混乱到规范
1. 认识并激活 venv
关键操作：venv\Scripts\activate
作用：在终端里切换到项目专属环境，看到 (venv) 前缀就是激活成功了
本质：告诉电脑 “接下来所有的 python 和 pip 操作，都用这个项目自己的 Python”
2. 给 PyCharm 绑定 venv 解释器
关键操作：设置 → Python 解释器 → 添加 → 选择项目里的 venv\Scripts\python.exe
作用：让 PyCharm 本身（编辑器、运行、调试）都用项目专属的 venv，不再依赖系统 Python
验证方法：设置后，下拉列表里会出现带 virtualenv 字样的选项，选中它即可
3. 让 PyCharm 终端自动激活 venv
关键操作：设置 → Tools → Terminal → 勾选 Activate virtualenv
解决的问题：以后新开终端，会自动带 (venv)，再也不用手动敲命令了
额外设置：PowerShell 执行策略 Set-ExecutionPolicy RemoteSigned，解决激活脚本被拦截的问题
4. 在 venv 里重新安装项目依赖
关键操作：在带 (venv) 的终端里，运行 pip install 所有需要的库
常见的 “坑”：
from PIL import Image → 安装要写 pip install pillow
from bs4 import BeautifulSoup → 安装要写 pip install beautifulsoup4
结果：项目里的爆红报错全部消失，代码能正常运行了
"""