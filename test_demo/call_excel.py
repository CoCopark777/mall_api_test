"""
读取excel内容
"""

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

def read_excel_dict(file_path, sheet_name):
    """
    得到的每一行都是字典
    """
    wb = openpyxl.load_workbook(file_path)
    sheet: Worksheet = wb[sheet_name]
    rows = list(sheet.values)
    # 第一行，一般是表头
    title = rows[0] # id	title	url	method	json	expected
    # 第二行开始一直取内容
    rows = rows[1:]
    new_rows = [dict(zip(title, row)) for row in rows]
    return new_rows
