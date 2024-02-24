# -*- coding:utf-8 -*-
'''
This program is only for Windows system users.
'''
import os
import time as t
import random as r
import wget
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
TEMP_FOLDER = os.path.expanduser("~") + '\\AppData\\Local\\Temp\\'

def clear_screen():
    os.system('cls')

def download_images(bk, pgnum, tmp):
    clear_screen()
    start_t = t.time()
    
    for i in range(1, pgnum + 1):
        num = str(i).zfill(3)
        percent = int(i / pgnum * 100)

        wget.download('https://book.pep.com.cn/' + bk + '/files/mobile/' + str(i) + '.jpg', tmp + '\\' + bk + '_' + num + '.jpg')
        clear_screen()
        print(str(percent) + '% | ' + '#' * percent)

    clear_screen()
    end_t = t.time()
    print('Time costs ' + str(end_t - start_t) + 's.')
    t.sleep(0.5)
    print('Please wait for a moment while we are merging the images to PDF...')

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
    '''
    for filename in os.listdir(image_folder):
        file_path = os.path.join(image_folder, filename)
        os.remove(file_path)
    os.rmdir(image_folder)
    '''

if __name__ == "__main__":
    bk = input('book number:')
    pgnum = int(input('page number:'))
    
    path = ''
    for i in range(r.randint(10, 100)):
        path = path + ALPHABET[r.randint(0, len(ALPHABET) - 1)]

    tmp = os.path.join(TEMP_FOLDER, path)

    if not os.path.exists(tmp):
        os.mkdir(tmp)

    download_images(bk, pgnum, tmp)
    images_to_pdf(tmp, bk + ".pdf")
