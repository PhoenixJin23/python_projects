import os
from PyPDF2 import PdfReader,PdfWriter


def pdf_tool(folder_path,output_name,password=None):
    writer=PdfWriter()

    #获取目标文件夹下的所有PDF文件
    files=[f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    files.sort()

    if not files:
        print("文件夹里没有PDF哦！")
        return

    print(f"发现{len(files)}个PDF文件，准备合并...")

    #逐个读取并加入合并器
    for file in files:
        file_path=os.path.join(folder_path,file)
        reader=PdfReader(file_path)

        #将每一页都添加到writer里
        for page in reader.pages:
            writer.add_page(page)
        print(f"已加入：{file}")

    #如果设置了密码，进行加密
    if password:
        writer.encrypt(password)
        print(f"已设置访问密码：{password}")

    #保存最终文件
    output_path=os.path.join(folder_path,output_name)
    with open(output_path,"wb") as f:
        writer.write(f)

    print(f"\n大功告成！")
    print(f"合并后的文件保存在{output_path}中")


pdf_tool("C:/Users/g3472/Desktop/cutiemice","new_pdf","feminist")