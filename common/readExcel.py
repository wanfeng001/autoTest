import os

from openpyxl import load_workbook
from common import  configpath

file_path = configpath.excel_path
class ReadExcel:
    def __init__(self):
        self.file_path = file_path
        self.wb = load_workbook(self.file_path)

    def get_column_value(self, sheet_name, col_num):
        sh = self.wb[sheet_name]
        column_value_list = []
        for i in range(2, sh.max_row + 1):
            value = sh.cell(i, col_num).value
            column_value_list.append(value)
        return column_value_list

    def get_row_value(self, sheet_name, row_num):
        sh = self.wb[sheet_name]
        column_value_list = []
        for i in range(2, sh.max_column + 1):
            value = sh.cell(row_num, i).value
            column_value_list.append(value)
        return column_value_list

    def get_cell_value(self, sheet_name, row_num, col_num):
        sh = self.wb[sheet_name]
        value = sh.cell(row_num, col_num).value
        return value

    def write_cell(self, sheet_name, row_num, col_num, value):
        sh = self.wb[sheet_name]
        sh.cell(row_num, col_num).value = value
        self.wb.save(self.file_path)


if __name__ == '__main__':
    read_excel = ReadExcel()
    sheet_name = read_excel.wb.sheetnames
    print(sheet_name)
    print(read_excel.get_row_value(sheet_name[0], 2))
    print(read_excel.get_column_value(sheet_name[0], 2))
