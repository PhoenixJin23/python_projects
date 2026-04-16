import os
from PyPDF2 import PdfReader


def extract_pdf_to_txt(pdf_path,txt_path):
    try:
        reader=PdfReader(pdf_path)
        all_texts=[]

        print(f"正在读取{pdf_path},共{len(reader.pages)}页")

        for i,page in enumerate(reader.pages): #一页一页遍历PDF
            text=page.extract_text() #提取这一页的文字
            if text:
                cleaned_text=text.strip() #去掉每行前后的空格
                all_texts.append(cleaned_text) #把一整页当做一个“元素”放进列表

        final_content="\n\n".join(all_texts) #每一页之间会空一行 \n\n表示换两行，也就是隔一行

        with open(txt_path,"w",encoding="UTF-8") as f:
            f.write(final_content)
        print(f"提取完成，文字已保存到{txt_path}")

    except Exception as e:
        print(f"提取失败{e}")


extract_pdf_to_txt("C:/Users/g3472/Desktop/cutiemice/digital_hoarding.pdf","C:/Users/g3472/Desktop/cutiemice/digital_hoarding.txt")





