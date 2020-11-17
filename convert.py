# This code is written by Jiali Liang to make Christians lives
# much eaiser when searching bible verses. This is part of the whole code
#



import pandas as pd
import numpy as np

# A(ZH) == 中文全稱， B(zh) == 中文簡稱， C(EN) == 英文全稱， D(en) == 英文簡稱
# For the simplicity of search engine, 1_kings -> 1_Kings,etc. 
# and Song of Songs = Song_of_Songs

A,B,C,D = np.genfromtxt('acronym.txt',usecols=(0,1,2,3),unpack=True,dtype=None,encoding=None)
  
# zh == 中文簡稱 --> EN == 英文全稱
def zh2EN(zh):  
    matching = np.where( B == zh )[0]
    
    # No matching case
    if len(matching) == 0:
        return 
    else :
        idx = list(np.where( B == zh ))[0]
        return str(C[idx][0])

# ZH == 中文全稱 --> zh == 中文簡稱
def ZH2zh(ZH):  
    matching = np.where( A == ZH )[0]
    
    # No matching case
    if len(matching) == 0:
        # Retun the original
        return ZH
    else :
        idx = list(np.where( A == ZH ))[0]
        return str(B[idx][0])
