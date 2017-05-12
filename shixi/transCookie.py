#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''转化cookie到dict'''

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "left-show=0; main[XWJOKE]=hoho; NFORUM=ak4njd9s73hkqd487brrkfd8u6; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1493100709,1493624270,1494404344; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1494552866; main[UTMPUSERID]=ethanww; main[UTMPKEY]=60686729; main[UTMPNUM]=13826; main[PASSWORD]=TsrjVL%2506O%25044r%2522%2505f%255C%25193%2503%2502V%2525p%250D%255E; left-index=00000100000"
    trans = transCookie(cookie)
    print(trans.stringToDict())
