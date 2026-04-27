# Python Practice Projects

这是一个记录我 Python 学习与实践过程的项目仓库，内容包括文件自动化、图像处理、数据分析、教程练习项目和基础网络爬虫。

这个仓库不仅用于练习 Python 语法，也用于尝试把学到的知识逐步做成可复用的小工具，并持续维护到 GitHub 上。

![Python](https://img.shields.io/badge/Python-3.11-blue)![Status](https://img.shields.io/badge/status-updating-brightgreen)![GitHub last commit](https://img.shields.io/github/last-commit/PhoenixJin23/python_projects)



## 目录

\- [仓库简介](#1-仓库简介) - [目录结构](#2-目录结构) - [项目概览](#3-项目概览) - [技术栈](#4-技术栈) - [学习收获](#5-学习收获) - [后续计划](#6-后续计划)

* #### **📌仓库简介**

* #### **🗂️目录结构**

* #### **🚀项目概览**

* #### **🛠️技术栈**

* #### 🌱学习收获

* #### **📍后续计划**





#### 1. 仓库简介

这个仓库记录了我的Python学习和练习项目，包括书本/网课练习项目、文件自动化、图像处理、数据分析和基本的爬虫项目。  建这个仓库不光是为了练习Python语法，也是为了记录整个Python学习与实践过程，核心是为了锻炼用Python解决日常实际问题的能力。





#### 2. 目录结构

```md
Python_projects/
├── data_analysis/ bill_merger, ledger_analyzer, bill_dashboard, Streamlit_demo 
├── file_tools/ rename, classify, duplicate, folder_analyzer, pdf_tool, image_to_PDF, PDF_to_txt
├── image_tools/ image_processor
├── tutorial_projects/ alien_invasion_demo_new, data_visualization
└── web_scraper/ scrape_douban, scrape_gold, web_crawler_2
```





#### 3. 项目概览

| Category      | Project            | Description                                                  |
| ------------- | ------------------ | ------------------------------------------------------------ |
| file_tools    | rename.py          | Batch rename files in a folder                               |
| file_tools    | classify.py        | Automatically classify files by type                         |
| file_tools    | duplicate.py       | Detect duplicate files                                       |
| file_tools    | folder_analyzer.py | Analyze folder structure and visualize subfolder statistics  |
| file_tools    | pdf_tool.py        | A simple PDF merging and encryption tool                     |
| file_tools    | image_to_PDF.py    | Convert images to PDF e-books                                |
| file_tools    | PDF_to_txt.py      | PDF text extractor                                           |
| Image Tools   | image_processor.py | Batch resize images and add watermark                        |
| Data Analysis | bill_merger.py     | Merge WeChat and Alipay bills into one CSV                   |
| Data Analysis | ledger_analyzer.py | Analyze expenses and visualize daily/category spending       |
| Web Scraper   | books scraper      | Scrape book titles, prices, and ratings from a static website |





#### 4. 技术栈

- Python
- os / pathlib
- pandas
- matplotlib
- Pillow
- requests
- BeautifulSoup
- PyPDF2
- PIL
- Streamlit





#### 5. 学习收获

通过这些项目，我逐步练习并熟悉了： 

- Python 基础语法在真实任务中的使用 
- 文件与文件夹的批量处理 
- 使用 pandas 处理 CSV 数据
- 使用 matplotlib 进行基础数据可视化
- 使用 Pillow 进行图像批处理
- 使用 requests 和 BeautifulSoup 进行静态网页抓取
- 在实际项目中调试、修复错误并迭代代码





#### 6. 后续计划

接下来我计划继续完善这个仓库，包括：

- 为各个子文件夹补充更详细的 README 

- 优化已有脚本的结构和复用性
- 将部分命令行脚本升级为更完整的小工具 
- 继续尝试 API 数据获取与可视化
- 学习使用 Streamlit 展示部分分析结果
- 持续更新和维护 GitHub 项目记录



