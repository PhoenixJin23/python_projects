import os
from PIL import Image, ImageDraw, ImageFont #Python最流行的图像处理库


#创建/打开output_dir--->遍历input_dir--->检查后缀，只处理图片--->
#打开图片--->缩放图片--->添加水印（确定水印位置，设置字体、大小、颜色）--->
#绘制文字---->保存结果


def batch_process_images(input_dir, output_dir, watermark_text="evermore"):
    #创建输出文件夹
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #遍历文件夹
    for filename in os.listdir(input_dir):
        #检查后缀，只处理图片
        if filename.lower().endswith(('.png','.jpg','.jpeg','.bmp')):
            img_path=os.path.join(input_dir,filename)

            try:
                #打开图片
                with Image.open(img_path) as img:
                    #缩放图片（保持比例）
                    #设定目标宽度为1500像素
                    target_width=1500
                    #计算缩放比例：目标宽度/原始宽度
                    ratio=target_width/float(img.size[0])
                    #计算对应高度
                    target_height=int(float(img.size[1])*ratio)
                    #执行缩放
                    img=img.resize((target_width,target_height),Image.Resampling.LANCZOS) #缩小图片时保证清晰

                    #添加水印
                    draw=ImageDraw.Draw(img)

                    #加载字体
                    try:
                        font=ImageFont.truetype("simhei.tff",24)
                    except:
                        font=ImageFont.load_default() #如果找不到黑体，用默认

                    #确认水印位置
                    position=(img.size[0]-90,img.size[1]-80) #宽度，高度

                    #绘制文字（颜色为白色，RGBA格式）A是透明度（0-255）
                    draw.text(position,watermark_text,font=font,fill=(255,255,255,128))

                    #保存结果
                    save_path=os.path.join(output_dir,f"processed_{filename}")
                    img.save(save_path)
                    print(f"处理成功:{filename}")

            except Exception as e:
                print(f"处理{filename} 失败{e}")


batch_process_images("C:/Users/g3472/Desktop/cutiemice/images","C:/Users/g3472/Desktop/cutiemice/output")

