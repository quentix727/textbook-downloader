# -*- coding:utf-8 -*-
import os
import time as t
# import shutil
import random as r
import wget
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

bk = input('book number:')
pgnum = int(input('page number:'))
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#^()-_'
path = ''
start_t = t.time()
c = 'cls'

for i in range(r.randint(10,100)):
    path = path + string[r.randint(0, 58)]

tmp = os.path.expanduser("~") + '\\AppData\\Local\\Temp\\' + path
os.mkdir(tmp)

os.system(c)
for i in range(1, pgnum + 1):
    num = str(i).zfill(3)
    percent = int(i / pgnum * 100)

    wget.download('https://book.pep.com.cn/' + bk + '/files/mobile/' + str(i) + '.jpg', tmp + '\\' + bk + '_' + num + '.jpg')
    os.system(c)
    print(str(percent) + '% | ' + '#' * percent)

os.system(c)
end_t = t.time()
print('Time costs ' + str(end_t - start_t) + 's.')
t.sleep(0.5)
print('Please wait for a moment while we are merge the images to PDF...')

def images_to_pdf(image_folder, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    for filename in sorted([filename for filename in os.listdir(image_folder) if filename.endswith('.jpg')]):
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)
        c.setPageSize(image.size)
        c.drawImage(image_path, 0, 0)
        c.showPage()

    c.save()
    print(f"PDF file saved as : {output_pdf}")
    # 这里要删除临时文件

images_to_pdf(tmp, bk + ".pdf")

