# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# ������PDF�t�@�C��
input_pdf_path = "output.pdf"
# �y�[�W�ԍ��t���̐V����PDF�t�@�C��
output_pdf_path = "output_with_page_numbers.pdf"

# ������PDF��ǂݍ���
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# �e�y�[�W�Ƀy�[�W�ԍ���ǉ�
for i, page in enumerate(reader.pages):
    # ��������ɐV����PDF���쐬
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page.mediabox)
    
    # �y�[�W�̕��ƍ������擾
    page_width = page.mediabox.upper_right[0]
    page_height = page.mediabox.upper_right[1]
    
    # �y�[�W�ԍ����E���ɒǉ�
    page_number_text = f"Page {i + 1}"
    can.drawString(page_width - 100, 20, page_number_text)  # �������K�v�ȏꍇ�͐��l��ύX
    
    # �L�����o�X�����PDF�ɕۑ�
    can.save()
    
    # ���������PDF��ǂݍ��݁A�y�[�W�ɒǉ�
    packet.seek(0)
    page_with_number = PdfReader(packet).pages[0]
    
    # ���̃y�[�W�Əd�ˍ��킹��
    page.merge_page(page_with_number)
    
    # �y�[�W��V����PDF�ɒǉ�
    writer.add_page(page)

# �V����PDF�t�@�C����ۑ�
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"�y�[�W�ԍ��t����PDF�� '{output_pdf_path}' �ɕۑ�����܂����B")
