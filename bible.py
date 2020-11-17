# This code is written by Jiali Liang to make Christians lives
# much eaiser when searching bible verses

import codecs
import pyperclip
import pandas as pd
import convert as cvt
import argparse
import numpy as np
import search_verse as sv

# function determines which version Simplified or Traditional to be used
def read_text_ZH(var):
    if var == "S":
        text = 'simplified.txt'
        form = "GBK"
    elif var == "T":
        text ='triditional.txt'
        form ='utf-8'
    #print(text)
    with codecs.open(text, 'U', form) as f:
        data = f.read()
        data = data.split("\n")
    return data

# Determine English version to be used or not
def read_text_EN(var):
    if var == "Y":
        ASV = np.array(pd.read_excel('bibles.xls',usecols="A,C"))
    elif var == "N":
        ASV = ""
    return ASV

# This function search the bible verses in both Chinese and English(optional)
# And this function combines the function below
def search(data,ASV,string):
    matching = [s for s in data if str(string) in s]
    ZHEN = ""
    #print("一共有%i条相关经文"%(len(matching)))
    if len(matching) == 0:
        print("\n不好意思，没有相关经文，请确认输入的格式是否正确\n")
        return ""
    for i in matching:
        # Printing the chinese verse
        print("\n"+i)
        # find the related english verse and print it
        EN_verse = ZH2ENG_verse(ASV,i)
        print(EN_verse)
        
        # combine chinese and english verses
        ZHEN += i+"\n"+EN_verse+"\n"
    return ZHEN

def search_EN(data,string):
    # If English search is not required
    if len(data) ==0:
        return
    # English verse is required
    else:
        ap = list(np.where(data[:,0]== string))[0]
        #print(string +" "+ data[ap,1][0])
        return data[ap,1][0]

# Given a chinese bible verse, find the related english verses
def ZH2ENG_verse(ASV,verse):
        ENG_book,ENG_verse = sv.sep_chapter(str.split(verse)[0])
        verse2search_EN = cvt.zh2EN(ENG_book) +" "+ENG_verse
        ENG = str(search_EN(ASV,verse2search_EN))
        
        if ENG == "None":
            return ""
        else:
            return verse2search_EN+" "+ENG

# this function copies the code to your clipboard
def copy_paste(verses):
    # Copy the verses to the clip board
    pyperclip.copy(str(verses))
    spam = pyperclip.paste()
    return spam
    
# Main function here
if __name__ == '__main__':
    # This code gathers the input from the terminal
    parser = argparse.ArgumentParser(description='请输入圣经查找章节,默认繁体字')
    parser.add_argument("book",
                        type=str,
                        nargs='?',
                        help="搜索经文格式：创 3 1 2 S（目录 章 起始节 最终节 簡or繁）\
                        \n 最終節和簡繁可以省略，默認繁體字")
    parser.add_argument("chapter",
                        type=str,
                        nargs='?',
                        help="章")
    parser.add_argument("begin_verse",
                        type=int,
                        nargs='?',
                        help="起始节")
   
    parser.add_argument("end_verse",
                        type=int,
                        default = 0,
                        nargs='?',
                        help="最终节")
    
    parser.add_argument("version",
                        type=str,
                        default = "T",
                        nargs = '?',
                        help="簡體(S) or 繁體(T) ")
    
    parser.add_argument("English",
                        type=str,
                        default = "N",
                        nargs = '?',
                        help="顯示英文(Y) or 不顯示英文(N) ")
    # Read in the arguements 
    args = parser.parse_args()
    
    # Set up if there is only one verse search
    # End verse = begin verse
    if args.end_verse == 0:
        args.end_verse = args.begin_verse
    
    # If it is not key word search, run follows
    verses="" 
    
    # determine which version to use, English or not
    ASV = read_text_EN(args.English)
    CHN = read_text_ZH(args.version)
    
    
    # find the verses from beginning to end
    for i in np.arange(args.begin_verse,args.end_verse+1):
        if i != 0:
            i = str(i) + " "
        # format the chinese verse to be searched
        verse2search_ZH = args.book + args.chapter + ":"+str(i)
        
        # Search the verse and add it to the string verses.
        searched_verse = str(search(CHN,ASV,verse2search_ZH))
        if len(searched_verse) >0:
            verses = verses + searched_verse + ""
    
    # this copy the verses to your clipboard so you can just paste it out
    spam = copy_paste(verses)

