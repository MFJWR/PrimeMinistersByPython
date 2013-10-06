#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import urllib

import io
import reader

class Downloader(io.IO):
	"""ダウンローダ：総理大臣のCSVファイル・画像ファイル・サムネイル画像ファイルをダウンロードする。"""

	def __init__(self, base_directory):
		"""ダウンローダのコンストラクタ。"""
		return

	def download_all(self):
		"""すべて（総理大臣の情報を記したCSVファイル・画像ファイル群・縮小画像ファイル群）をダウンロードし、テーブルを応答する。"""
		return None

	def download_csv(self):
		"""総理大臣の情報を記したCSVファイルをダウンロードする。"""
		return None

	def download_images(self, image_filenames):
		"""画像ファイル群または縮小画像ファイル群をダウンロードする。"""
		return
