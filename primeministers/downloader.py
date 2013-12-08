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
                self.download_csv()
                image_filenames = map((lambda n : '/0'+str(n)+'.jpg'),range(39, 63))
                self.download_images(image_filenames)
		return None

	def download_csv(self):
		"""総理大臣の情報を記したCSVファイルをダウンロードする。"""
                urllib.urlretrieve(self.url + '/PrimeMinisters.csv', self._base_directory + '/PrimeMinisters.csv')
		return None

	def download_images(self, image_filenames):
		"""画像ファイル群または縮小画像ファイル群をダウンロードする。"""
                if os.path.isdir(self._base_directory+'/images'):
                    shutil.rmtree(self._base_directory+'/images')   
                os.makedirs(self._base_directory+'/images')
                if os.path.isdir(self._base_directory+'/thumbnails'):
                    shutil.rmtree(self._base_directory+'/thumbnails')
                os.makedirs(self._base_directory+'/thumbnails')            
                for filename in image_filenames:
                    urllib.urlretrieve(self.url+'/images'+filename, self._base_directory+'/images'+filename)
                    urllib.urlretrieve(self.url+'/thumbnails'+filename, self._base_directory+'/thumbnails'+filename)
                    
		return
