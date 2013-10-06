#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys

import io
import table
import tuple

class Writer(io.IO):
	"""ライタ：総理大臣の情報のテーブルをHTMLページとして書き出す。"""

	def __init__(self, base_directory, output_table):
		"""ライタのコンストラクタ。HTMLページを基にするテーブルを受け取る。"""
		self._base_directory = base_directory
		self._table = output_table
		return

	def write(self):
		"""HTMLページを基にするテーブルから、インデックスファイル(index.html)に書き出す。"""
		html_filename = os.path.join(self._base_directory, 'index.html')
		with open(html_filename, 'wb') as a_file:
			self.write_header(a_file)
			self.write_body(a_file)
			self.write_footer(a_file)
		return

	def write_body(self, file):
		"""ボディを書き出す。つまり、属性リストを書き出し、タプル群を書き出す。"""
		return

	def write_footer(self, file):
		"""フッタを書き出す。"""
		name_string = "PrimeMinisters written by Python"
		date_string = datetime.date.today().strftime("%Y/%m/%d")
		time_string = datetime.datetime.now().strftime("%H:%M:%S")
		file.write("\t\t\t\t\t</tbody>\n\t\t\t\t</table>\n\t\t\t</td>\n\t\t</tr>\n\t</tbody>\n</table>\n<hr>\n<div class=\"right-small\">Created using " + name_string + " " + date_string + " " + time_string + "</div>\n</body>\n</html>\n")
		return
	
	def write_header(self, file):
		"""ヘッダを書き出す。"""
		file.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\n<html lang=\"ja\">\n<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n<meta http-equiv=\"Content-Style-Type\" content=\"text/css\">\n<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\">\n<meta name=\"keywords\" content=\"Smalltalk,Oriented,Programming\">\n<meta name=\"description\" content=\"Prime Ministers\">\n<meta name=\"author\" content=\"AOKI Atsushi\">\n<link rev=\"made\" href=\"http://www.cc.kyoto-su.ac.jp/~atsushi/\">\n<link rel=\"index\" href=\"index.html\">\n<style type=\"text/css\">\n<!--\nbody {\n\tbackground-color : #ffffff;\n\tmargin : 20px;\n\tpadding : 10px;\n\tfont-family : serif;\n\tfont-size : 10pt;\n}\na {\n\ttext-decoration : underline;\n\tcolor : #000000;\n}\na:link {\n\tbackground-color : #ffddbb;\n}\na:visited {\n\tbackground-color : #ccffcc;\n}\na:hover {\n\tbackground-color : #dddddd;\n}\na:active {\n\tbackground-color : #dddddd;\n}\ndiv.belt {\n\tbackground-color : #eeeeee;\n\tpadding : 0px 4px;\n}\ndiv.right-small {\n\ttext-align : right;\n\tfont-size : 8pt;\n}\nimg.borderless {\n\tborder-width : 0px;\n\tvertical-align : middle;\n}\ntable.belt {\n\tborder-style : solid;\n\tborder-width : 0px;\n\tborder-color : #000000;\n\tbackground-color : #ffffff;\n\tpadding : 0px 0px;\n\twidth : 100%;\n}\ntable.content {\n\tborder-style : solid;\n\tborder-width : 0px;\n\tborder-color : #000000;\n\tpadding : 2px 2px;\n}\ntd.center-blue {\n\tpadding : 2px 2px;\n\ttext-align : center;\n\tbackground-color : #ddeeff;\n}\ntd.center-pink {\n\tpadding : 2px 2px;\n\ttext-align : center;\n\tbackground-color : #ffddee;\n}\ntd.center-yellow {\n\tpadding : 2px 2px;\n\ttext-align : center;\n\tbackground-color : #ffffcc;\n}\n-->\n</style>\n<title>Prime Ministers</title>\n</head>\n<body>\n<div class=\"belt\">\n<h2>Prime Ministers</h2>\n</div>\n<table class=\"belt\" summary=\"table\">\n\t<tbody>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\t<table class=\"content\" summary=\"table\">\n\t\t\t\t\t<tbody>\n")
		return
