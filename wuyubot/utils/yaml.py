'''
Author: y68 yeqiu6080@outlook.my
Date: 2025-02-05 22:08:52
LastEditors: yeqiu6080
LastEditTime: 2025-02-05 22:21:37
Description: file content
'''
import yaml
import os
class yaml_util:
    def __init__(self,file_path = None):
        self.file_path = file_path 
    def check_file(self):
        if not self.file_path:
            raise ValueError("file_path is not set")
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("file not found")
        return True
    def read(self):
        self.check_file()
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    def write(self,data):    
        if not self.file_path:
            raise ValueError("file_path is not set")
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f)
        except Exception as e:
            return e
        else:
            return 0
    
    def open(self,file_path):
        self.file_path = file_path