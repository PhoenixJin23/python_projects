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