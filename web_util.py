from bs4 import BeautifulSoup as bs
from requests import get as get_raw
from hashlib import md5 as hash_
from time import sleep 
import os
import pandas as pd
from random import randint
import pickle

cachedir = ".hash-cache";
fetch_slowdown = 0.1

if not os.path.isdir(cachedir):
    os.mkdir(cachedir);

def hash(x):
    return hash_(x.encode("utf-8")).hexdigest();

def hash_loc(x):
    return cachedir + "/" + hash(x)

def read_file(f):
    with open(f,'r') as fd:
        return fd.read();

def write_file(f,content):
    with open(f,'w') as fd:
        fd.write(content);
    return f;

def get(url):
    hl = hash_loc(url);
    if os.path.isfile(hl):
        print("Cache hit. {}".format(url))
        return read_file(hl);
    else:
        print("Cache miss. {}".format(url))
        sleep(fetch_slowdown+randint(0,3));
        content = get_raw(url).content.decode();
        write_file(hl,content);
        return content;

def head(s):
    return s[:10]

def get_bs(url):
    content = get(url);
    return bs(content);
