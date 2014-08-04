#-*- coding:utf-8 -*-
from application import app
from flask import render_template

student_list = [
	{"name" : "강지혜", "url" : "http://kangjekangje.appspot.com"},
	{"name" : "강현욱", "url" : "http://luis-kang-1205.appspot.com"},
	{"name" : "김다예", "url" : "http://daye10003.appspot.com"},
	{"name" : "김대홍", "url" : "http://grizzlyraccoon.appspot.com"},
	{"name" : "김민석", "url" : "http://korea-plan.appspot.com"},
	{"name" : "노승은", "url" : "http://i-am-jammanbo.appspot.com"},
	{"name" : "류기현", "url" : "http://rukeon07.appspot.com"},
	{"name" : "류재희", "url" : "http://uu-1025ryu.appspot.com"},
	{"name" : "백재현", "url" : "http://jhlikelion.appspot.com"},
	{"name" : "선재원", "url" : "http://whatssun-gatsby.appspot.com"},
	{"name" : "손보경", "url" : "http://pplafterwards.appspot.com"},
	{"name" : "이교영", "url" : "http://monicapackers.appspot.com"},
	{"name" : "이동우", "url" : "http://dongwoo.me"},
	{"name" : "이종복", "url" : "http://acejongbok.appspot.com"},
	{"name" : "이혜리", "url" : "http://gpfl7846.appspot.com"},
	{"name" : "정승완", "url" : "http://seungwanchung1234.appspot.com"},
	{"name" : "정우주", "url" : "http://lion-001.appspot.com"},
	{"name" : "조경욱", "url" : "http://cloud-9209.appspot.com"},
	{"name" : "천현정", "url" : "http://hyunjeongcheon.appspot.com"},
	{"name" : "현지인", "url" : "http://scenic-630.appspot.com"}
]

@app.route('/')
@app.route('/index')
def index() :
	return render_template('layout_sample.html')#, entries = student_list)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404