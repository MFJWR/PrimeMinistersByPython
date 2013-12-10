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
		table_records = super(Reader, self).read_csv(self._csv_filename)
		a_table = table.Table('input')
		a_table.attributes().set_names(table_records.pop(0))

		for row in table_records:
			a_tuple = tuple.Tuple(a_table.attributes(), row)
			a_table.add(a_tuple)

		return a_table
