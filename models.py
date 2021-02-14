#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@author: 崔博凯
@contact: 2232652509@qq.com
@contact: dioxincreature@163.com
@file: models.py
@time: 2021/1/23/8:10
"""

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    identify_code = models.CharField(max_length=20)
    yanzheng_code = models.IntegerField(null=True)
    if_yanzheng = models.BooleanField(null=True)
    if_person_inform = models.BooleanField(null=True, default=False)
    if_person_pic = models.BooleanField(null=True, default=False)
    if_person_money = models.BooleanField(null=True, default=False)
    if_person = models.BooleanField(null=True, default=False)
    if_team_num = models.BooleanField(null=True, default=False)
    if_team_inform = models.BooleanField(null=True, default=False)
    if_team_money = models.BooleanField(null=True, default=False)
    if_team = models.BooleanField(null=True, default=False)
    if_team_fenpei = models.BooleanField(null=True,default=False)

class Student(models.Model):
    name = models.CharField(max_length=5)
    sex = models.IntegerField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    qq = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    school_name = models.CharField(max_length=30)
    school_name_in_english = models.CharField(max_length=100)
    place = models.IntegerField()
    identify_code = models.CharField(max_length=20)
    belongs_user = models.CharField(max_length=20)
    belongs_team = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    if_room = models.IntegerField(null=True)
    if_paid = models.BooleanField(null=True)

class Team(models.Model):
    school_name = models.CharField(max_length=20)
    school_name_in_english = models.CharField(max_length=100)
    first_name = models.CharField(max_length=10)
    first_sex = models.IntegerField(null=True)
    first_phone = models.CharField(max_length=20)
    first_mail = models.CharField(max_length=50)
    second_name = models.CharField(max_length=10)
    second_sex = models.IntegerField(null=True)
    second_phone = models.CharField(max_length=20)
    second_mail = models.CharField(max_length=50)
    teacher_num = models.IntegerField(null=True)
    all_number = models.IntegerField(null=True)
    xiqian_num = models.IntegerField(null=True)
    harry_num = models.IntegerField(null=True)
    anli_num = models.IntegerField(null=True)
    San_num = models.IntegerField(null=True)
    jingshe_num = models.IntegerField(null=True)
    news_num = models.IntegerField(null=True)
    shiwei_num = models.IntegerField(null=True)
    room_num = models.IntegerField(null=True)
    finished_num = models.IntegerField(null=True)
    identify_code=models.CharField(max_length=30)
    if_fenpei = models.BooleanField(null=True)
    if_paid = models.BooleanField(null=True)
