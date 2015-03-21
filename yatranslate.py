#/usr/bin/env python

__author__ = 'anders-lokans'

import requests
import json
import getopt
import sys


API_KEY = "trnsl.1.1.20150109T145728Z.5ec8c0f80c8a8268.c76dfca1d41563cb33088339e117182db43729e7"
TRANSLATE_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?"


def prepare_url(direction, text):
    key_str = "".join(["key=", API_KEY])
    text_str = "".join(["text=", text])
    lang = "".join(["lang=", direction])
    url = "&".join([TRANSLATE_URL, key_str, lang, text_str])
    return url


def translate(direction="en-ru", text="Some text",):
    url = prepare_url(direction, text)
    r = requests.get(url)
    if r.status_code == 200:
        d = json.loads(r.text)
        res_text = d["text"]
        if res_text == text:
            raise Exception("No such word!")
        return res_text[0]
    return None




if __name__ == "__main__":
    optlist, arglist = getopt.getopt(sys.argv[1:], "d:t:")
    # print(optlist)
    text = ""
    direction = ""
    for opt, arg in optlist:
        if opt == "-d":
            direction = arg
        if opt == "-t":
            text = arg

    if direction and text:
        print(translate(direction=direction, text=text))
    elif text:
        print(translate(text=text))
    else:
        print("No text supplied.")
