import os
import time
from datetime import date

import pytest
from openpyxl import load_workbook
from common import configpath

file_path = configpath.excel_path
file1_path = configpath.excel1_path


class ReadExcel:
    def __init__(self):
        self.file_path = file1_path
        self.wb = load_workbook(self.file_path)

    def get_column_value(self, sheet_name, col_num):
        sh = self.wb[sheet_name]
        case = []
        for i in range(2, sh.max_row + 1):
            value = sh.cell(i, col_num).value
            case.append(value)
        return case

    def get_row_value(self, sheet_name, row_num):
        sh = self.wb[sheet_name]
        case = []
        for i in range(2, sh.max_column + 1):
            value = sh.cell(row_num, i).value
            case.append(value)
        return case

    def get_cell_value(self, sheet_name, col_num, row_num):
        sh = self.wb[sheet_name]
        value = sh.cell(row_num, col_num).value
        return value

    def write_cell(self, sheet_name, col_num, row_num, value):
        sh = self.wb[sheet_name]
        sh.cell(row_num, col_num).value = value
        self.wb.save(self.file_path)


def get_data():
    read_excel = ReadExcel()
    case = []
    for idx, value in enumerate(read_excel.get_column_value(sheet_name='登录模块用例', col_num=configpath.isExecute)):
        if value == 'Y':
            data = read_excel.get_row_value(sheet_name='登录模块用例', row_num=idx + 2)
            username = data[configpath.Account - 2]
            password = data[configpath.Password - 2]
            case.append(username)
            case.append(password)
    return case

class Test_login:
    @pytest.mark.parametrize('account,password',get_data())
    def test_login(self,account,password):
        print('登录的账号密码为{}'.format(account))



