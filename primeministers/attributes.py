#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Attributes(object):
	"""属性リスト：総理大臣の情報テーブルを入出力する際の属性情報を記憶。"""

	def __init__(self, kind_string):
            """入力用("input")または出力用("output")で属性リストを作成するコンストラクタ。"""           
            if kind_string == "input":
                self._keys = ['no','order','name','kana','period','school','party','place','image','thumbnail']
            elif kind_string == "output":
                self._keys = ['no','order','name','kana','period','days','school','party','place','image']
            return

	def __str__(self):
	    """自分自身を文字列にして、それを応答する。"""
            return ','.join(self._names)

	def keys(self):
	    """キー群を応答する。"""
            return self._keys 

	def names(self):
	    """名前群を応答する。"""
	    return self._names

	def set_names(self, names):
	    """名前群を設定する。"""
            self._names = names
	    return
