#!/usr/bin/env python
import urllib, urllib2
import json
import sys
URL="http://ws.audioscrobbler.com/2.0/"
KEY="053c665cb61bf209d442c5a36fb71f9a"
periods=["overall","7day", "1month", "6month", "12month"]
limit="5"
period="overall"
user=""


def is_user(**kwargs):
    kwargs.update({
        "method": "user.getInfo",
        "api_key": KEY,
        "user": user,
        "format": "json"
        })

    url_send=URL+"?"+urllib.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.load(data)
    if 'message' in res:
        if res['message']=="User not found":
            return False
        else:
            True
    return True

def generate(**kwargs):
    kwargs.update({
        "method": "user.getTopArtists",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"
        })

    url_send=URL+"?"+urllib.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.load(data)
    s="Top artysci:\n"
    for item in res['topartists']['artist']:
        print item['name']
        print item['playcount']
        s="".join((s,"Nazwa: "+item['name'],"\nOdtworzenia: ",item['playcount'],"\n***\n"))
    data.close()
    return s

def generate_albums(**kwargs):
    kwargs.update({
        "method": "user.getTopAlbums",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"
        })

    url_send=URL+"?"+urllib.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.load(data)
    s="Top albumy:\n"
    for item in res['topalbums']['album']:
        print item['name']
        print item['artist']['name']
        print item['playcount']
        s="".join((s,"Nazwa: ",item['name'],"\nArtysta: ",item['artist']['name']," \nOdtworzenia: ", item['playcount'],"\n *** \n"))
    data.close()
    return s

def generate_tracks(**kwargs):
    kwargs.update({
        "method": "user.getTopTracks",
        "api_key": KEY,
        "user": user,
        "limit": limit,
        "period" : period,
        "format": "json"
        })

    url_send=URL+"?"+urllib.urlencode(kwargs)
    data=urllib2.urlopen(url_send)
    res=json.load(data)
    s="Top utwory:\n"
    for item in res['toptracks']['track']:
        print item['name']
        print item['artist']['name']
        print item['playcount']
        s="".join((s, "\nTytul: ", item['name'], " Wykonawca: ", item['artist']['name'], "\nOdtworzenia: ", item['playcount'], "\n***\n"))
    data.close()
    return s
