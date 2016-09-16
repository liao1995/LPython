import urllib2
import json

def read_text():
    words = open("words_to_you")
    contents_of_file = words.read()
#    word_list = contents_of_file.split(" ")
#    for word in word_list:
    translate_word(contents_of_file)
    words.close()

def translate_word(word):
    
    f = urllib2.urlopen("http://fanyi.youdao.com/openapi.do?keyfrom=translateIt123&key=1031676807&type=data&doctype=json&version=1.1&q="+word)
    output = f.read()
    output = output.decode('utf-8')
    res = json.loads(output)
    print(res['translation'][0])
    f.close()

read_text()
