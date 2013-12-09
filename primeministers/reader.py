#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
import table
import tuple

class Reader(io.IO):
	"""リーダ：総理大臣の情報を記したCSVファイルを読み込んでテーブルに仕立て上げる。"""

	def __init__(self, csv_filename):
		"""リーダのコンストラクタ。"""
                self._csv_filename = csv_filename
		return

	def table(self):
		"""ダウンロードしたCSVファイルを読み込んでテーブルを応答する。"""
                with open(self._csv_filename,"rU") as a_csv_file:
                    while True:
                        a_string = a_csv_file.readline()
                        if len(a_string) == 0: 
                            break;
                        
                        a_list = a_string.split(',')
                        if a_list[0] == '人目':
                            a_table = table.Table(a_list)

                        while len(a_string) != 0:
                            a_string = a_csv_file.readline()
                            values = a_string.split(',')
                            a_tuple = tuple.Tuple(a_table.attributes, values)
                            a_table.add(a_tuple)
		return a_table
