#! /usr/bin/env python
# -*- coding: utf-8 -*-

import attributes

class Table(object):
	"""表：総理大臣の情報テーブル。"""

	def __init__(self, kind_string):
		"""テーブルのコンストラクタ。"""
		self._attributes = attributes.Attributes(kind_string)
		self._tuples = []
		return

	def __str__(self):
		"""自分自身を文字列にして、それを応答する。"""
		tuple_string = map((lambda a_tuple:str(a_tuple)),self._tuples)
		return '\n'.join(tuple_string)

	def add(self, tuple):
		"""タプルを追加する。"""
		self._tuples.append(tuple)
		return

	def attributes(self):
		"""属性リストを応答する。"""
		return self._attributes

	def image_filenames(self):
		"""画像ファイル群をリストにして応答する。"""
		return 

	def thumbnail_filenames(self):
		"""縮小画像ファイル群をリストにして応答する。"""
		return None
	
	def tuples(self):
		"""タプル群を応答する。"""
		return self._tuples
