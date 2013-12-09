#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Tuple(object):
	"""タプル：総理大臣の情報テーブルの中の各々のレコード。"""

	def __init__(self, attributes, values):
		"""属性リストと値リストからタプルを作るコンストラクタ。"""
		self._attributes = attributes
		self._values = values
		return

	def __str__(self):
		"""自分自身を文字列にして、それを応答する。"""
		return ','.join(self._values)

	def attributes(self):
		"""属性リストを応答する。"""
		return self._attributes

	def values(self):
		"""値リストを応答する。"""
		return self._values

	def set_values(self, values):
		"""値リストを設定する。"""
		self._values = values
		return
