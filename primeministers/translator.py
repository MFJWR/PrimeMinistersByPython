#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import locale

import table
import tuple

class Translator(object):
	"""トランスレータ：総理大臣のCSVファイルをHTMLページへと変換するプログラム。"""

	def __init__(self, input_table):
		"""トランスレータのコンストラクタ。"""
		self._input_table = input_table
		locale.setlocale(locale.LC_NUMERIC, 'ja_JP')
		return

	def compute_string_of_days(self, period):
		"""在位日数を計算して、それを文字列にして応答する。"""
		dayString = re.findall(r'[0-9]+', period)
		daylist = map((lambda str:int(str)), dayString)

		appointedday = datetime.date(*daylist[0:3])

		if len(daylist) < 6:
			retiredday = datetime.date.today()
		else:
			retiredday = datetime.date(*daylist[3:6])

		return str(locale.format('%d',((retiredday - appointedday).days + 1), True))

	def compute_string_of_image(self, tuple):
		"""サムネイル画像から画像へ飛ぶためのHTML文字列を作成して、それを応答する。"""
		keys = self._input_table.attributes().keys()
		values = tuple.values()
		return '<a name="'+values[keys['no']]+'" href="'+values[keys['image']]+'"><img class="borderless" src="'+values[keys['thumbnail']]+'" width="25" height="32" alt="0'+values[keys['no']]+'.jpg"></a>'

	def table(self):
		"""総理大臣のCSVファイルを基にしたテーブルから、HTMLページを基にするテーブルに変換して、それを応答する。"""
		output_table = table.Table('output')
		input_keys = self._input_table.attributes().keys()

		output_names = self._input_table.attributes().names()
		output_names.pop(input_keys['thumbnail'])
		output_names.insert(input_keys['period']+1,'在位日数')
		output_names = map((lambda name:'<td class="center-pink"><strong>'+name+'</strong></td>'), output_names)
		output_table.attributes().set_names(output_names)
		
		count = 0
		output_keys = output_table.attributes().keys()
		for a_tuple in self._input_table.tuples():
			values = a_tuple.values()
			string_of_image = self.compute_string_of_image(a_tuple)
			string_of_days = self.compute_string_of_days(values[input_keys['period']])
			
			values.insert(output_keys['days'],string_of_days)
			values[output_keys['image']] = string_of_image
			values.pop(output_keys['image']+1)
			
			color = 'blue' if count % 2 == 0 else 'yellow'
			values = map((lambda value:'<td class="center-'+color+'">'+value+'</td>'),values)
			
			output_tuple = tuple.Tuple(output_table.attributes(), values)
			output_table.add(output_tuple)
			count+=1
		return output_table
