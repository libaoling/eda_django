﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from polls.models import User
import logging

from EDA_TEST.response import r
import time


def index(req):
    return render(req, 'index.html')


def register(req):

    if req.method == 'GET':
        return render(req, 'register.html', {})
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        confirmpwd = req.POST.get('confirmpwd')
        name_bool = User.objects.filter(user_name=username)
        if not name_bool:
            if password == confirmpwd:
                # 计算当前时间
                createtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                User.objects.create(user_name=username,user_pwd=password,create_time=createtime)
                return render(req,'login.html',{"msg":"注册成功,请登录"})
        else:
            return render(req,'register.html',{"msg":"用户名已存在"})


def login(req):
    if req.method == 'GET':
        # return render(req,"login.html",{})
        return render(req, 'login.html', {})
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        # 验证用户名
        name_bool = User.objects.filter(user_name=username)
        # 验证用户密码
        # pwd_bool = User.objects.filter(user_pwd=password)
        # 计算当前时间
        logintime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            if name_bool:
                if name_bool[0].user_pwd == password:
                    # 更新用户登陆状态与时间
                    User.objects.filter(user_name=username).update(login_state=1, login_time=logintime)
                    # User.objects.filter(user_name=username).update(login_time=logintime)
                    return JsonResponse(r(success=True,result={'msg':'登陆成功'}),json_dumps_params={'ensure_ascii': False})
                else:
                    return JsonResponse(r(False,result={'msg':'密码输入错误'}),json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse(r(False,result={"msg": "用户名输入错误"}),json_dumps_params={'ensure_ascii': False})
        except Exception as e:
            logging.info(e)
            print(e)
            # return render(req, 'login.html')
    # if req.method == 'GET':
    #     # return render(req,"login.html",{})
    #     return JsonResponse(r(False))
    #
    # elif req.method == 'POST':
    #     username = req.POST.get('username')
    #     password = req.POST.get('password')
    #     #验证用户名
    #     name_bool = User.objects.filter(user_name=username)
    #     #验证用户密码
    #     pwd_bool = User.objects.filter(user_pwd=password)
    #     #计算当前时间
    #     logintime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #
    #     if name_bool:
    #         if pwd_bool:
    #             #更新用户登陆状态与时间
    #             User.objects.filter(user_name=username).update(login_state=1,login_time=logintime)
    #             # User.objects.filter(user_name=username).update(login_time=logintime)
    #             return render(req,'index.html',{})
    #         else:
    #             return render(req, 'login.html',{"msg":"密码输入错误"})
    #     else:
    #         return render(req, 'login.html',{"msg":"用户名输入错误"})

def logout(req):
    return render(req, 'login.html', {"msg": "账号已退出"})

