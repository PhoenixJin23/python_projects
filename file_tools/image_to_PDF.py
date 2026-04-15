from PIL import Image
import os


def images_to_pdf(folder_path,output_name):
    files=[f for f in os.listdir(folder_path) if f.endswith(('.PNG','.JPG','.jpeg'))]
    files.sort()

    if not files:
        print("没找到图片！")
        return

    first_img=Image.open(os.path.join(folder_path,files[0])).convert('RGB')

    other_imgs=[]
    for file in files[1:]:
        img=Image.open(os.path.join(folder_path,file)).convert('RGB')
        other_imgs.append(img)

    output_path=os.path.join(folder_path,output_name)
    first_img.save(output_path,save_all=True,append_images=other_imgs)
    # Pillow的save()只能保存单张图片，须手动开save_all=True,并把剩下的图传给append_images
    # 1.选主体的第一张图；2.剩下的保存到列表中；3.save_all=True+append_images=列表

    print(f"电子书已生成！{output_path}")

images_to_pdf("C:/Users/g3472/Desktop/cutiemice/images","image_pdf.pdf")
