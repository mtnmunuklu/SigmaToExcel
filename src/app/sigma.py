
import os
import glob
from yaml import safe_load_all
import logging
from src.app.logger import Logger
from src.config import Config
from xlwt import Workbook, XFStyle, Font, Borders, Alignment

class SigmaConverter:
    """
    Used for sigma converter operations
    """
    rules = list()


    def __init__(self):
        """
        Constructor Method
        :param: none
        :return: none
        """
        self.file_directory = Config.FILE_DIRECTORY
        self.file_format = Config.FILE_FORMAT
        self.output = Config.OUTPUT
        self.logger = Logger('SigmaConverter')

    def read_from_file(self):
        """
        Used for read packets in given directory
        :param: none
        :return: none
        """
        try:
            for file_path in glob.iglob(self.file_directory + self.file_format, recursive=True):
                if os.path.exists(file_path):
                    self.parse_yml(file_path)
        except Exception as e:
            self.logger.log(logging.WARNING, "File read error")
            self.logger.log(logging.ERROR, e)

    def parse_yml(self, file_path):
        """
        Used for parse xml file
        :param file_path: yaml file path
        :type file_path: str
        :return: none
        """
        try:
            with open(file_path, encoding="utf8") as file:
                docs = safe_load_all(file)
                rule = dict()
                for doc in docs:
                     for key, value in doc.items():
                         rule.setdefault(key, []).append(value)
                self.rules.append(rule)
        except Exception as e:
                self.logger.log(logging.WARNING, "YML parse error")
                self.logger.log(logging.ERROR, e)

    def write_to_excel(self):
        """
        Used for write sigma rules to excel
        :param: none
        :return: none
        """
        try:
        # Workbook is created 
            wb = Workbook()
            column_style = self.set_style_column("Arial", 200, True)

            sheet1 = wb.add_sheet('Rules')
            sheet1.write(0, 0, "Title", column_style) #title
            sheet1.write(0, 1, "Status", column_style) #status
            sheet1.write(0, 2, "Description", column_style) #description
            sheet1.write(0, 3, "References", column_style) #references
            sheet1.write(0, 4, "Category-Product-Service", column_style) #logsource:category
            sheet1.write(0, 5, "Falsepositives", column_style) #falsepositives
            sheet1.write(0, 6, "Level", column_style) #level
            sheet1.write(0, 7, "Tags", column_style) #tags
            sheet1.write(0, 8, "Modified", column_style) #Modified

            index = 1
            for rule in self.rules:
                print(str(rule))
                if rule.get("title") and rule.get("title")[0] != None:
                    title = ", ".join(filter(None, rule.get("title")))
                    sheet1.write(index, 0, str(title))
                if rule.get("status") and rule.get("status")[0] != None:
                    status = ", ".join(filter(None, rule.get("status")))
                    sheet1.write(index, 1, str(status))
                if rule.get("description") and rule.get("description")[0] != None:
                    description =  ", ".join(filter(None, rule.get("description")))
                    sheet1.write(index, 2, str(description))
                if rule.get("references") and rule.get("references")[0] != None:
                    references = ", ".join( ", ". join(filter(None, references)) for references in rule.get("references") if references)
                    sheet1.write(index, 3, str(references))
                if rule.get("logsource") and rule.get("logsource")[0] != None:
                    logsource = ", ".join("Category: {}".format(logsource.get("category")) +
                " - " + "Product: {}".format(logsource.get("product")) +
                " - " +"Service: {}".format(logsource.get("service")) for logsource in rule.get("logsource"))
                    sheet1.write(index, 4, str(logsource))
                if rule.get("falsepositives") and rule.get("falsepositives")[0] != None:
                    falsepositives = ", ".join( ", ". join(filter(None, falsepositives)) for falsepositives in rule.get("falsepositives"))
                    sheet1.write(index, 5, str(falsepositives))
                if rule.get("level") and rule.get("level")[0] != None:
                    level = ", ".join(filter(None, rule.get("level")))
                    sheet1.write(index, 6, str(level))
                if rule.get("tags") and rule.get("tags")[0] != None:
                    tags = ", ".join( ", ". join(filter(None, tags)) for tags in rule.get("tags"))
                    sheet1.write(index, 7, str(tags))
                if rule.get("modified") and rule.get("modified")[0] != None:
                    modified = ", ".join(filter(None, rule.get("modified")))
                    sheet1.write(index, 8, str(modified))
                index += 1

            wb.save(self.output)
        except Exception as e:
                self.logger.log(logging.WARNING, "Excel create error")
                self.logger.log(logging.ERROR, e)

        
    def set_style_column(self, name, height, bold=False):
        """
        Used to set style of excel
        :param name: font name
        :type name: str
        :param height: font height
        :type height: str
        :return: excel style
        :rtype: XFStyle
        """
        style = XFStyle()
        font = Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

