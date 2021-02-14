#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, reverse, redirect
from django.views.decorators import csrf
from django.http import HttpResponse
from .models import *
import random
from django.core.mail import send_mail
import re
import json
import os
import time

"""
@author: 崔博凯
@contact: 2232652509@qq.com
@contact: dioxincreature@163.com
@file: views.py
@time: 2021/1/7/0:17
"""


def index(request):
    return render(request, "index.html")


def download(request):
    return render(request, "download.html")


def hi_index(request):
    if request.POST:
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        if 'login' in request.POST:
            try:
                stu = User.objects.filter(email=email, if_yanzheng=1)[0]
            except:
                return render(request,"no_zhuce.html")
            else:
                if stu.password == password:
                    new_url = '/get_data_index?identify_code=' + stu.identify_code
                    return redirect(new_url)
                else:
                    return render(request,"wrong_mima.html")
        elif 'signup' in request.POST:
            if_go_on = True
            try:
                stu_list = User.objects.filter(email=email)
            except:
                if_go_on = True
            else:
                for stu in stu_list:
                    if stu.if_yanzheng:
                        if_go_on = False
                        break
            if if_go_on:
                base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
                random_str = ''
                length = len(base_str) - 1
                for i in range(20):
                    random_str += base_str[random.randint(0, length)]
                stu = User(email=email, password=password, identify_code=random_str, if_yanzheng=False)
                stu.save()
                new_url = '/yanzhengma?identify_code=' + random_str
                return redirect(new_url)
            else:
                return render(request, 'hi_index.html', {'if_zhuce': True})
    else:
        return render(request, "hi_index.html", {'if_zhuce': False})


def yanzhegnma(request):
    if request.GET:
        identify_code = request.GET['identify_code']
        random_int = random.randint(100000, 999999)
        stu = User.objects.get(identify_code=identify_code)
        stu.yanzheng_code = random_int
        send_mail('您正在注册WesMun', '您的验证码为' + str(random_int), '2232652509@qq.com', [stu.email], fail_silently=False)
        stu.save()
        print("at_get")
        return render(request, 'yanzheng_code.html', {'if_not_ok': False})
    if request.POST:
        referrer = request.META['HTTP_REFERER']
        identify_code = re.search('(identify_code=)([^&])*', referrer).group().split('=')[1]
        stu = User.objects.filter(identify_code=identify_code).order_by('-id')[0]
        if str(stu.yanzheng_code) == request.POST['yanzhengma']:
            stu.if_yanzheng = True
            stu.save()
            new_url = '/get_data_index?identify_code=' + identify_code
            return redirect(new_url)
        else:
            new_url = '/wrong_yanzheng?identify_code=' + identify_code
            return redirect(new_url)


def wrong_yanzheng(request):
    return render(request, 'yanzheng_code.html',
                  {'if_not_ok': True, "url": json.dumps("/yanzhengma?identify_code=" + request.GET['identify_code'])})


def get_data_index(request):
    identify_code = request.GET['identify_code']
    team = "/team?identify_code=" + identify_code
    person = "/person?identify_code=" + identify_code
    data = {
        'team': json.dumps(team),
        'person': json.dumps(person),
    }
    return render(request, 'get_data_index.html', data)


def team(request):
    identify_code = request.GET['identify_code']
    peoples = "/people?identify_code=" + identify_code
    information = "/information?identify_code=" + identify_code
    back_url = "/get_data_index?identify_code=" + identify_code
    data = {
        'peoples': json.dumps(peoples),
        'information': json.dumps(information),
        'back_url':json.dumps(back_url)
    }
    return render(request, 'team.html', data)


def person(request):
    identify_code = request.GET['identify_code']
    data_url = "/get_data?identify_code=" + identify_code
    img_url = "/get_img?identify_code=" + identify_code
    back_url = "/get_data_index?identify_code=" + identify_code
    data = {
        'data_url': json.dumps(data_url),
        'img_url': json.dumps(img_url),
        'back_url':json.dumps(back_url)
    }
    return render(request, 'person.html', data)


def people(request):
    if request.POST:
        referrer = request.META['HTTP_REFERER']
        identify_code = re.search('(identify_code=)([^&])*', referrer).group().split('=')[1]
        school_name = request.POST['school_name']
        school_name_in_english = request.POST['school_name_in_english']
        first_name = request.POST['first_name']
        first_sex = request.POST['first_sex']
        first_phone = request.POST['first_phone']
        first_mail = request.POST['first_mail']
        second_name = request.POST['second_name']
        second_sex = request.POST['second_sex']
        second_phone = request.POST['second_phone']
        second_mail = request.POST['second_mail']
        teacher_num = int(request.POST['teacher_num'])
        xiqian_num = int(request.POST['xiqian_num'])
        harry_num = int(request.POST['harry_num'])
        anli_num = int(request.POST['anli_num'])
        San_num = int(request.POST['San_num'])
        jingshe_num = int(request.POST['jingshe_num'])
        news_num = int(request.POST['news_num'])
        shiwei_num = int(request.POST['shiwei_num'])
        room_num = int(request.POST['room_num'])

        new_url = '/team?identify_code=' + identify_code
        all_number = xiqian_num + harry_num + anli_num + San_num + jingshe_num + news_num + shiwei_num
        the_team = Team(school_name=school_name, school_name_in_english=school_name_in_english,
                        first_name=first_name, first_sex=first_sex, first_mail=first_mail, first_phone=first_phone,
                        second_sex=second_sex, second_mail=second_mail, second_name=second_name,
                        second_phone=second_phone,
                        teacher_num=teacher_num, xiqian_num=xiqian_num, harry_num=harry_num,
                        anli_num=anli_num,
                        San_num=San_num, jingshe_num=jingshe_num, news_num=news_num, shiwei_num=shiwei_num,
                        room_num=room_num, finished_num=0, identify_code=identify_code, all_number=all_number)
        the_team.save()
        the_user = User.objects.filter(identify_code=identify_code, if_yanzheng=True)[0]
        the_user.if_team_num = True
        the_user.if_team = True
        the_user.save()
        return redirect(new_url)
    if request.GET:
        identify_code = request.GET['identify_code']
        the_user = User.objects.filter(identify_code=identify_code, if_yanzheng=True)[0]
        print(the_user.if_team_num)
        if the_user.if_person or the_user.if_team_num:
            new_url = '/only_one?identify_code=' + identify_code
            return redirect(new_url)
        else:
            return render(request, 'people.html')


def information(request):
    if request.GET:

        identify_code = request.GET['identify_code']
        user = User.objects.filter(identify_code=identify_code,if_yanzheng=True)[0]
        if user.if_person:
            new_url = '/only_one?identify_code=' + identify_code
            return redirect(new_url)
        if not user.if_team_num:
            new_url = '/no_num?identify_code=' + identify_code
            return redirect(new_url)

        if user.if_team_inform:
            new_url = '/already_inform?identify_code=' + identify_code
            return redirect(new_url)
        if not user.if_team_fenpei:
            new_url = '/no_fenpei?identify_code=' + identify_code
            return redirect(new_url)

        the_team = Team.objects.filter(identify_code=identify_code)[0]
        all_number = the_team.all_number
        finished_number = the_team.finished_num

        data = {
            "all": all_number,
            "finished": finished_number + 1,
        }

        return render(request, 'information.html', data)
    if request.POST:
        referrer = request.META['HTTP_REFERER']
        identify_code = re.search('(identify_code=)([^&])*', referrer).group().split('=')[1]
        the_data = request.POST
        name = the_data['name']
        sex = the_data['sex']
        phone = the_data['phone']
        email = the_data['email']
        qq = the_data['qq']
        id_number = the_data['id_number']
        if_room = the_data['zhusu']
        place = the_data['place']
        the_team = Team.objects.filter(identify_code=identify_code)[0]
        school = the_team.school_name
        school_in_english = the_team.school_name_in_english
        new_url = '/information?identify_code=' + identify_code
        the_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + "\\wesmun\\WesMun\\static\\user_img\\"
        path_name = str(int(time.time())) + "." + request.FILES['file'].name.split(".")[-1]
        with open(the_path + path_name, "wb") as file:
            for k in request.FILES['file'].chunks():
                file.write(k)
        stu = Student(name=name, sex=sex, telephone=phone, email=email, qq=qq, id_number=id_number, school_name=school,
                      school_name_in_english=school_in_english, identify_code=identify_code, place=place,
                      belongs_team="No", belongs_user=identify_code, if_room=if_room, state=path_name)
        stu.save()
        the_team.finished_num += 1
        the_team.save()
        finished_url = '/money?identify_code=' + identify_code

        if the_team.finished_num == the_team.all_number:
            the_user = User.objects.filter(identify_code=identify_code,if_yanzheng=True)[0]
            the_user.if_team_inform=True
            the_user.save()
            return redirect(finished_url)
        else:

            return redirect(new_url)
def no_num(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "no_num.html", data)

def already_inform(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "already_inform.html", data)
def no_fenpei(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "no_fenpei.html", data)


def get_data(request):
    if request.POST:
        the_data = request.POST
        name = the_data['name']
        sex = the_data['sex']
        phone = the_data['phone']
        email = the_data['email']
        qq = the_data['qq']
        id_number = the_data['id_number']
        school = the_data['school']
        school_in_english = the_data['school_in_english']
        place = the_data['place']
        if_room = the_data['zhusu']
        referrer = request.META['HTTP_REFERER']
        identify_code = re.search('(identify_code=)([^&])*', referrer).group().split('=')[1]
        stu = Student(name=name, sex=sex, telephone=phone, email=email, qq=qq, id_number=id_number, school_name=school,
                      school_name_in_english=school_in_english, identify_code=identify_code, place=place,
                      belongs_team="No", belongs_user=identify_code, if_room=if_room, if_paid=False)
        stu.save()
        user = User.objects.filter(identify_code=identify_code, if_yanzheng=True)[0]
        user.if_person = True
        user.if_person_inform=True
        user.save()
        new_url = '/get_data_index?identify_code=' + identify_code
        return redirect(new_url)
    if request.GET:
        identify_code=request.GET['identify_code']
        user = User.objects.filter(identify_code=identify_code,if_yanzheng=True)[0]
        if user.if_team or user.if_person_inform:
            new_url = '/only_one?identify_code=' + identify_code
            return redirect(new_url)
        else:
            return render(request, "get_data.html")


def get_img(request):
    if request.FILES:
        path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + "\\wesmun\\WesMun\\static\\user_img\\"
        name = str(int(time.time())) + "." + request.FILES['file'].name.split(".")[-1]
        with open(path + name, "wb") as file:
            for k in request.FILES['file'].chunks():
                file.write(k)
        referrer = request.META['HTTP_REFERER']
        identify_code = re.search('(identify_code=)([^&])*', referrer).group().split('=')[1]
        stu = Student.objects.filter(identify_code=identify_code)[0]
        stu.state = name
        stu.save()
        new_url = '/money?identify_code=' + identify_code
        the_user = User.objects.filter(identify_code=identify_code,if_yanzheng=True)[0]
        the_user.if_person_pic = True
        the_user.save()
        return redirect(new_url)
    else:
        identify_code = request.GET['identify_code']
        user = User.objects.filter(identify_code=identify_code, if_yanzheng=True)[0]
        if not user.if_person_inform:
            new_url = '/no_inform?identify_code=' + identify_code
            return redirect(new_url)
        if user.if_team:
            new_url = '/only_one?identify_code=' + identify_code
            return redirect(new_url)
        if user.if_person_pic:
            new_url = '/already_pic?identify_code=' + identify_code
            return redirect(new_url)
        return render(request, 'get_img.html')
def already_pic(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "already_pic.html", data)
def no_inform(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "no_inform.html", data)
def get_test(request):
    return render(request, "get_test.html")


def contact(request):
    return render(request, "contact.html")


def tutorial(request):
    return render(request, "tutorial.html")


def get_one(request):
    return render(request, "get_one.html")


def money(request):
    return render(request, "money.html")

def only_one(request):
    data = {"url": json.dumps("/get_data_index?identify_code=" + request.GET['identify_code'])}
    return render(request, "only_one.html",data)