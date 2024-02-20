# -*- coding:utf-8 -*-
import os
import urllib.request
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

bk = input('book number:')          # 官网二级目录的名称，如 https://book.pep.com.cn/1443001112191/mobile/index.html
pgnum = int(input('page number:'))  # 页数
user_dir = os.path.expanduser("~")  # 获取用户目录
os.mkdir(user_dir + '\\AppData\\Local\\Temp\\azwsexdrcftvgybhunjimexdrcftvgybhunj')

for i in range(1, pgnum + 1):
    if len(str(i)) == 1:
        num = '00' + str(i)
    elif len(str(i)) == 2:
        num = '0' + str(i)
    else:
        num = str(i)

    urllib.request.urlretrieve('https://book.pep.com.cn/' + bk + '/files/mobile/' + str(i) + '.jpg', user_dir + '\\AppData\\Local\\Temp\\azwsexdrcftvgybhunjimexdrcftvgybhunj\\' + bk + '_' + num + '.jpg')


def images_to_pdf(image_folder, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    for filename in sorted([filename for filename in os.listdir(image_folder) if filename.endswith('.jpg')]):
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)
        image_width, image_height = image.size
        c.setPageSize((image_width, image_height))
        c.drawImage(image_path, 0, 0)
        c.showPage()

    c.save()
    print(f"PDF file saved as : {output_pdf}")
    # 注释下面代码，因为目录不是空的
    # os.rmdir(user_dir + '\\AppData\\Local\\Temp\\azwsexdrcftvgybhunjimexdrcftvgybhunj')

images_to_pdf(user_dir + '\\AppData\\Local\\Temp\\azwsexdrcftvgybhunjimexdrcftvgybhunj', bk + ".pdf")

