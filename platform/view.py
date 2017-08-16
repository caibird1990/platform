#!/usr/bin/python
#coding: utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from yhd_monitor.models import *
import json
import os
import re
import time
import MySQLdb
import commands
import urllib
import urllib2
import decimal
import sys
import subprocess
import requests
import parse_test
import redis
from subprocess import Popen, PIPE, STDOUT
import mods

reload(sys)
sys.setdefaultencoding('utf-8')

def getjson(result):
	return HttpResponse(json.dumps(result, encoding='utf-8', ensure_ascii=False))

def test_ops(request):
	return render(request, 'testing.html')

def testing(request):
	con = MySQLdb.connect(user='root', db='django', passwd='biao_123', host='10.4.42.103', charset='utf8')
	cur = con.cursor()
	result = {}
	results = []
	datastore = []
	selectcmd = "select id,icon,name,levelCode,url from tbl_function order by levelCode asc;"
	linetitle = ['id', 'icon', 'name', 'levelCode', 'url']
	cur.execute(selectcmd)
	for eachline in cur.fetchall():
		eachdir = dict(zip(linetitle, eachline))
		results.append(eachdir)
	return getjson(results)
