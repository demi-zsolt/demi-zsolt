import pandas as pd


class readExcelFile:
    def __init__(self, fileURL, sheet):
        self.fileURL = fileURL
        self.sheet = sheet

    def getColumnCells(self, columnName, callback):
        excelFile = pd.ExcelFile(self.fileURL)
        sheetData = excelFile.parse(self.sheet)

        for cell in sheetData[columnName]:
            callback(cell)

