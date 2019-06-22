# -*- coding: utf-8 -*-
"""
Python Notebook (ipnb) to plain Python convertor
@author: Alexandre Poisson
"""
import json

def ipynb2py(file_path, out_file_path):
    with open(file_path, encoding="utf8", errors='ignore') as json_file, open(out_file_path, 'w') as out_file:
        data = json.load(json_file)
        for __cell in data['cells']:
            if __cell['cell_type'] =='code':
                out_file.writelines(__cell['source'])
                out_file.write("\n")
    return 0


def test():
    ret = ipynb2py(r'gtsd.ipynb','test.py')


if __name__=="__main__":
    test()
