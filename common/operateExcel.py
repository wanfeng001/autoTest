import datetime
import os
import time
from datetime import date

import pytest
from openpyxl import load_workbook
from openpyxl.styles import Font, colors
from common import configPath


# 操作Excel数据
class OperateExcel:
    def __init__(self):
        self.file_path = configPath.excel_path
        self.wb = load_workbook(self.file_path)

    # 获取某一列数据(不包括标题)
    def get_column_value(self, sheet_name, col_num):
        sh = self.wb[sheet_name]
        case = []
        for i in range(1, sh.max_row + 1):
            value = sh.cell(i, col_num).value
            case.append(value)
        return case

    # 获取对应id行的序列
    def get_rowId_index(self, sheet_name, id):
        idx = configPath.id
        allIdList = self.get_column_value(sheet_name, col_num=idx)
        if id not in allIdList:
            raise TypeError('编号：{},不存在!'.format(id))
        else:
            idIndex = allIdList.index(id)
            return idIndex

    # 获取某一行数据
    def get_row_value(self, sheet_name, row_num):
        sh = self.wb[sheet_name]
        case = []
        for i in range(1, sh.max_column + 1):
            value = sh.cell(row_num, i).value
            case.append(value)
        return case

    # 获取单元格数据
    def get_cell_value(self, sheet_name, col_num, row_num):
        sh = self.wb[sheet_name]
        value = sh.cell(row_num, col_num).value
        return value

    # 写入单元格数据
    def write_result(self, sheet_name, id, value):
        """
        @param sheet_name: Sheet表名称
        @param id:用例编号
        @param value: fail or pass
        """

        sh = self.wb[sheet_name]
        # 设置时间格式
        curTime = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
        # 横,纵坐标
        y = self.get_rowId_index(sheet_name, id) + 1
        x = configPath.test_result
        # 写入
        sh.cell(y, x).value = curTime + "->" + value
        # 设置字体样式
        if value.lower() == 'fail':
            v = sh.cell(y, x)
            v.font = Font(name='Arial', color=colors.RED, size=10)
        elif value.lower() == 'pass':
            v = sh.cell(y, x)
            v.font = Font(name='Arial', color="00B050",size=10)
        else:
            raise TypeError('请传入fail,pass,不区分大小写')
        # 保存
        print('保存数据,执行成功')
        self.wb.save(self.file_path)


# 获取执行为Y的数据
def get_data():
    read_excel = OperateExcel()
    case = []
    for idx, value in enumerate(read_excel.get_column_value(sheet_name='登录模块用例', col_num=configPath.isExecute)):
        if value == 'Y':
            data = read_excel.get_row_value(sheet_name='登录模块用例', row_num=idx + 2)
            # 继续添加想要的数据
            username = data[configPath.Account - 2]
            password = data[configPath.Password - 2]
            info = [username, password]
            for i in range(len(info)):
                if info[i] == None:
                    info[i] = ''
            case.append(info)
    return case


if __name__ == '__main__':
    r = OperateExcel()
    r.write_result(sheet_name='Sheet2',id=1,value='pass')
    r.write_result(sheet_name='Sheet2',id=2,value='fail')
    r.write_result(sheet_name='Sheet2',id=3,value='pass')
    r.write_result(sheet_name='Sheet2',id=4,value='fail')
    r.write_result(sheet_name='Sheet2',id=5,value='pass')
    r.write_result(sheet_name='Sheet2',id=6,value='fail')
    r.write_result(sheet_name='Sheet2',id=7,value='pass')
    r.write_result(sheet_name='Sheet2',id=8,value='fail')
    r.write_result(sheet_name='Sheet2',id=9,value='pass')
    r.write_result(sheet_name='Sheet2',id=10,value='fail')
    r.write_result(sheet_name='Sheet2',id=11,value='pass')
    r.write_result(sheet_name='Sheet2',id=12,value='fail')
    r.write_result(sheet_name='Sheet2',id=13,value='pass')
    r.write_result(sheet_name='Sheet2',id=14,value='fail')
    r.write_result(sheet_name='Sheet2',id=15,value='pass')
    r.write_result(sheet_name='Sheet2',id=16,value='fail')


