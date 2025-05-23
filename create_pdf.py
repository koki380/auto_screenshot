# -*- coding: utf-8 -*-
import pyautogui
import time
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# スクリーンショット保存用フォルダ
output_folder = "screenshots"
os.makedirs(output_folder, exist_ok=True)

# スリープタイム
t1 = 6.0  # t1秒
t2 = 1.0  # t2秒
num_screenshots = 28  # 取得したいスクリーンショットの数

#開始までt0秒
t0 = 20
time.sleep(t0)
print("start!!")

# スクリーンショット取得ループ
#for i in range(num_screenshots):
 #   pyautogui.press("right")  # 右矢印キーを押す
 #   time.sleep(t1)
    
    # スクリーンショットを撮影し、JPEGで保存
 #   screenshot = pyautogui.screenshot()
 #   screenshot_path = f"{output_folder}/screenshot_{i + 700}.jpg"
#    screenshot.save(screenshot_path, "JPEG")
#    
#    time.sleep(t2)

# PDF出力
pdf_path = "output2.pdf"
pdf = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

for i in range(1,num_screenshots):
    screenshot_path = f"{output_folder}/screenshot_{i + 700}.jpg"
    img = Image.open(screenshot_path)
    img_width, img_height = img.size  # 画像のサイズを取得

    # ページサイズを画像サイズに合わせる
    pdf.setPageSize((img_width, img_height))
    pdf.drawImage(screenshot_path, 0, 0, width=img_width, height=img_height)

     # ページ番号を右下に表示
    page_number_text = f"Page {i + 700}"
    pdf.drawString(img_width - 100, 20, page_number_text)  # 右下にページ番号を追加

    pdf.showPage()  # 新しいページを作成

pdf.save()  # PDFを保存
