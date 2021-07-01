import xlrd
import xlsxwriter


readerbook = xlrd.open_workbook('t_department.xls')
readsheet = readerbook.get_sheet('t_department')

writerbook = xlsxwriter.Workbook('部门列表.xls')
writersheet = writerbook.add_worksheet('部门列表')

