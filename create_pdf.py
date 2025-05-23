# -*- coding: utf-8 -*-
import pyautogui
import time
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# �X�N���[���V���b�g�ۑ��p�t�H���_
output_folder = "screenshots"
os.makedirs(output_folder, exist_ok=True)

# �X���[�v�^�C��
t1 = 6.0  # t1�b
t2 = 1.0  # t2�b
num_screenshots = 28  # �擾�������X�N���[���V���b�g�̐�

#�J�n�܂�t0�b
t0 = 20
time.sleep(t0)
print("start!!")

# �X�N���[���V���b�g�擾���[�v
#for i in range(num_screenshots):
 #   pyautogui.press("right")  # �E���L�[������
 #   time.sleep(t1)
    
    # �X�N���[���V���b�g���B�e���AJPEG�ŕۑ�
 #   screenshot = pyautogui.screenshot()
 #   screenshot_path = f"{output_folder}/screenshot_{i + 700}.jpg"
#    screenshot.save(screenshot_path, "JPEG")
#    
#    time.sleep(t2)

# PDF�o��
pdf_path = "output2.pdf"
pdf = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

for i in range(1,num_screenshots):
    screenshot_path = f"{output_folder}/screenshot_{i + 700}.jpg"
    img = Image.open(screenshot_path)
    img_width, img_height = img.size  # �摜�̃T�C�Y���擾

    # �y�[�W�T�C�Y���摜�T�C�Y�ɍ��킹��
    pdf.setPageSize((img_width, img_height))
    pdf.drawImage(screenshot_path, 0, 0, width=img_width, height=img_height)

     # �y�[�W�ԍ����E���ɕ\��
    page_number_text = f"Page {i + 700}"
    pdf.drawString(img_width - 100, 20, page_number_text)  # �E���Ƀy�[�W�ԍ���ǉ�

    pdf.showPage()  # �V�����y�[�W���쐬

pdf.save()  # PDF��ۑ�
