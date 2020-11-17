#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 03:32:24 2019

@author: jiali
"""

# -*- coding: utf8 -*-
import opencc
cc = opencc.OpenCC('t2s')
a= cc.convert(u'Open Chinese Convert（OpenCC）「開放中文轉換」，是一個致力於中文簡繁轉換的項目，提供高質量詞庫和函數庫(libopencc)。')
print(a)