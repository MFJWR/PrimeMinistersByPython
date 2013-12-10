#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re

import table
import tuple

class Translator(object):
	"""トランスレータ：総理大臣のCSVファイルをHTMLページへと変換するプログラム。"""

	def __init__(self, input_table):
		"""トランスレータのコンストラクタ。"""
		self._input_table = input_table
		return

	def compute_string_of_days(self, period):
		"""在位日数を計算して、それを文字列にして応答する。"""
		return "n"

	def compute_string_of_image(self, tuple):
		"""サムネイル画像から画像へ飛ぶためのHTML文字列を作成して、それを応答する。"""
		values = tuple.values()
		return '<a name="'+values[0]+'" href="'+values[8]+'"><img class="borderless" src="'+values[9]+'" width="25" height="32" alt="0'+values[0]+'.jpg"></a>'

	def table(self):
		"""総理大臣のCSVファイルを基にしたテーブルから、HTMLページを基にするテーブルに変換して、それを応答する。"""
		output_table = table.Table('output')
		output_names = self._input_table.attributes().names()
		output_names.pop(-1)
		output_names.insert(5,'在位日数')
		output_names = map((lambda name:'<td class="center-pink"><strong>'+name+'</strong></td>'), output_names)
		output_table.attributes().set_names(output_names)
		
		count = 0
		for a_tuple in self._input_table.tuples():
			string_of_image = self.compute_string_of_image(a_tuple)
			values = a_tuple.values()
			string_of_days = self.compute_string_of_days(values[4])
			
			values.insert(5,string_of_days)
			values[9] = string_of_image
			values.pop(-1)
			
			color = 'blue' if count % 2 == 0 else 'yellow'
			values = map((lambda value:'<td class="center-'+color+'">'+value+'</td>'),values)
			
			output_tuple = tuple.Tuple(output_table.attributes(), values)
			output_table.add(output_tuple)
			count+=1
		return output_table
