# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# 既存のPDFファイル
input_pdf_path = "output.pdf"
# ページ番号付きの新しいPDFファイル
output_pdf_path = "output_with_page_numbers.pdf"

# 既存のPDFを読み込み
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# 各ページにページ番号を追加
for i, page in enumerate(reader.pages):
    # メモリ上に新しいPDFを作成
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page.mediabox)
    
    # ページの幅と高さを取得
    page_width = page.mediabox.upper_right[0]
    page_height = page.mediabox.upper_right[1]
    
    # ページ番号を右下に追加
    page_number_text = f"Page {i + 1}"
    can.drawString(page_width - 100, 20, page_number_text)  # 調整が必要な場合は数値を変更
    
    # キャンバスを閉じてPDFに保存
    can.save()
    
    # メモリ上のPDFを読み込み、ページに追加
    packet.seek(0)
    page_with_number = PdfReader(packet).pages[0]
    
    # 元のページと重ね合わせる
    page.merge_page(page_with_number)
    
    # ページを新しいPDFに追加
    writer.add_page(page)

# 新しいPDFファイルを保存
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"ページ番号付きのPDFが '{output_pdf_path}' に保存されました。")
