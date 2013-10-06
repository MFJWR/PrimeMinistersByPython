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
		return

	def compute_string_of_days(self, period):
		"""在位日数を計算して、それを文字列にして応答する。"""
		return None

	def compute_string_of_image(self, tuple):
		"""サムネイル画像から画像へ飛ぶためのHTML文字列を作成して、それを応答する。"""
		return None

	def table(self):
		"""総理大臣のCSVファイルを基にしたテーブルから、HTMLページを基にするテーブルに変換して、それを応答する。"""
		return None
