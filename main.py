# -*- coding:utf-8 -*-
import os
import time as t
import shutil
import urllib.request
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

bk = input('book number:')
pgnum = int(input('page number:'))
tmp = os.path.expanduser("~") + '\\AppData\\Local\\Temp\\azwsexdrcftvgybhunjimexdrcftvgybhunj'
os.mkdir(tmp)

for i in range(1, pgnum + 1):
    num = str(i).zfill(3)
    urllib.request.urlretrieve('https://book.pep.com.cn/' + bk + '/files/mobile/' + str(i) + '.jpg', tmp + '\\' + bk + '_' + num + '.jpg')


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
    # 不知道为什么，总是下面的代码总被占用
    '''
    t.sleep(5)
    shutil.rmtree(tmp)
    '''

images_to_pdf(tmp, bk + ".pdf")

