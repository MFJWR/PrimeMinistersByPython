#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class IO(object):
	"""入出力：リーダ・ダウンローダ・ライタを抽象する。"""

	def read_csv(self, filename):
		"""指定されたファイルをCSVとして読み込む。"""
		return None

	def write_csv(self, filename, rows):
		"""指定されたファイルにCSVとして行たち(rows)を書き出す。"""
		return
