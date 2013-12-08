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
                self._base_directory = base_directory
                self.url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/CSV2HTML/PrimeMinisters'
		return

	def download_all(self):
		"""すべて（総理大臣の情報を記したCSVファイル・画像ファイル群・縮小画像ファイル群）をダウンロードし、テーブルを応答する。"""
                image_filenames = map((lambda n : '/0'+str(n)+'.jpg'),range(39, 63))
                self.download_csv()
                self.download_images(image_filenames)

		a_reader = reader.Reader(self._base_directory + '/PrimeMinisters.csv')
                a_table = a_reader.table()
                return a_table

	def download_csv(self):
		"""総理大臣の情報を記したCSVファイルをダウンロードする。"""
                urllib.urlretrieve(self.url + '/PrimeMinisters.csv', self._base_directory + '/PrimeMinisters.csv')
                
		return 

	def download_images(self, image_filenames):
		"""画像ファイル群または縮小画像ファイル群をダウンロードする。"""
                image_directory = self._base_directory+'/images'
                thumbnail_directory = self._base_directory+'/thumbnails'

                if os.path.isdir(image_directory):
                    shutil.rmtree(image_directory)   
                os.makedirs(image_directory)
                if os.path.isdir(thumbnail_directory):
                    shutil.rmtree(thumbnail_directory)
                os.makedirs(thumbnail_directory)

                for filename in image_filenames:
                    urllib.urlretrieve(self.url+'/images'+filename, image_directory+filename)
                    urllib.urlretrieve(self.url+'/thumbnails'+filename, thumbnail_directory+filename)
                    
		return
