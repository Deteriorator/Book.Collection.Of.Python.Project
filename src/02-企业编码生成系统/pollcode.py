#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    pollcode.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.06.30   10:13
-------------------------------------------------------------------------------
   @Change:   2020.07.06
-------------------------------------------------------------------------------
"""

import os
import random
import time
import string
import qrcode
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from  tkinter import *
from string import digits

root = tkinter.Tk()

number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.mkdir(path)


def openfile(filename):
    f = open(filename)
    flist = f.read()
    f.close()
    return flist


def inputbox(showstr, showorder, length):
    instr = input(showstr)
    if len(instr) != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == 0:
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print(
                        "\033[1;31;40m 必须输入" + str(length) + "个字母，"
                                                             "请重新输入！！\033[0m"
                    )
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print(
                        "\033[1;31;40m 必须输入" + str(length) + "个数字，"
                                                             "请重新输入！！\033[0m"
                    )
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"

    else:
        print("\033[1;31;40m 输入为空，请重新输入！！\033[0m")
        return "0"


def wfile(sstr, sfile, typeis, smsg, datapath):
    mkdir(datapath)
    datafile = datapath + "\\" + sfile
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')
        wdata = wdata.replace("'''", '').replace("'''", '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print("\033[1;31m" + pdata + "\033[0m")
    if typeis != "no":
        tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) +
                                    "\n 防伪码文件存放位置: " + datafile)
        root.withdraw()


def mainmenu():
    print("""\033[1;35m
      ***************************************************************
                         企业编码生成系统
      ***************************************************************
          1.生成6位数字防伪编码 (213563型)
          2.生成9位系列产品数字防伪编码 (879-335439型)
          3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE35O-DW2K4)    
          4.生成含数据分析功能的防伪编码(5A61M0583D2)
          5.智能批量生成带数据分析功能的防伪码
          6.后续补加生成防伪码(5A61M0583D2)
          7.EAN-13条形码批量生成
          8.二维码批量输出
          9.企业粉丝防伪码抽奖
          0.退出系统
      ===============================================================
      说明: 通过数字键选择菜单
      ===============================================================
    \033[0m""")

    while i < 9:
        mainmenu()
        choice = input("\033[1;32m    请输入您要操作的菜单选项:\033[0m")
        if len(choice) != 0:
            choice = input_validation(choice)
            if choice == 1:
                scode1(str(choice))
            if choice == 2:
                scode2(str(choice))
            if choice == 3:
                scode3(str(choice))
            if choice == 4:
                scode4(str(choice))
            if choice == 5:
                scode5(str(choice))
            if choice == 6:
                scode6(str(choice))
            if choice == 7:
                scode7(str(choice))
            if choice == 8:
                scode8(str(choice))
            if choice == 9:
                scode9(str(choice))
            if choice == 0:
                i = 0
                print("正在退出系统!!")
        else:
            print("\033[1;31;40m    输入非法，请重新输入!!\033[0m")
            time.sleep(2)


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m    输入非法，请重新输入!!\033[0m")
            return 0
        else:
            return insel
    else:
        print("\033[1;31;40m    输入非法，请重新输入!!\033[0m")
        return 0


def scode1(schoice):
    incount = inputbox("\033[1;32m    请输入您要生成防伪码的数量:\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入您要生成防伪码的数量:\033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ''
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    wfile(randstr, 'scode' + str(schoice) + ".txt", "", "已生成6位防伪码共计: ", "codepath")


def scode2(schoice):
    ordstart = inputbox("\033[1;32m    请输入系列产品的数字七十号(3位):\33[0m", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m    请输入系列产品的数字七十号(3位):\33[0m", 1, 0)
    ordcount = inputbox("\033[1;32m    请输入产品系列的数量:\33[0m", 1, 0)
    while int(ordcount) < 1 or int(ordcount) > 9999:
        ordcount = inputbox("\033[1;32m    请输入产品系列的数量: ", 1, 0)
    incount = inputbox('\033[1;32m    请输入要生成的每个系列产品的防伪码数量:\033[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m    请输入您要生成防伪码的数量:\033[0m', 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m)+ randfir + '\n')
    wfile(randstr, "scode" + str(schoice) + ".txt", '', "已生成9位系列产品防伪码共计:", 'codepath')


def scode3(schoice):
    incount = inputbox("\033[1;32m    请输入要生成的25位混合产品序列号数量:\33[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m    请输入要生成的25位混合产品序列号数量:\33[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ''
        for i in range(25):
            strone = strone + random.choice(letter)
        strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + \
                 '-' + strone[15:20] + '-' + strone[20:25] + '\n'
        randstr.append(strtwo)
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成25位混合防伪序列码攻击:', 'codepath')


def scode4(schoice):
    intype = inputbox("\033[1;32m    请输入数据分析编号(3位字母):\033[0m", 2, 3)
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox('\33[1;32m    请输入数据分析编号(3位字母):\33[0m', 2, 3)
    incount = inputbox('\033[1; 32m    输入要生成的带数据分析功能的防伪码数量:\033[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1; 32m    输入要生成的带数据分析功能的防伪码数量:\033[0m', 1, 0)
    ffcode(incount, intype, '', schoice)


def scode5(schoice):
    default_dir = r'codeauto.mri'
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=[('Text file', '*.mri')],
        title="请选择智能批处理文件: ",
        initialdir=(os.path.expanduser(default_dir))
    )
    codelist = openfile(file_path)
    codelist = codelist.split("\n")
    print(codelist)
    for item in codelist:
        codea = item.split(',')[0]
        codeb = item.split(',')[1]
        ffcode(codeb, codea, 'no', schoice)


def scode6(schoice):
    default_dir = 'c:ABD'


def scode7(schoice):
    pass


def scode8(schoice):
    pass


def scode9(schoice):
    pass


def scode0(schoice):
    pass


def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()
        strtype = typestr[1].upper()
        strclass = typestr[2].upper()
        randfir = random.sample(number, 3)
        randsec = sorted(randfir)
        letterone = ''
        for i in range(9):
            letterone = letterone + random.choice(number)
        sim = str(letterone[0:int(randsec[0])]) + strpro + \
              str(letterone[int(randsec[0]): int(randsec[1])]) + strtype + \
              str(letterone[int(randsec[1]): int(randsec[2])]) + strclass + \
              str(letterone[int(randsec[2]):9]) + '\n'
        randstr.append(sim)
    wfile(
        randstr, typestr + 'scode' + str(schoice) + '.txt', ismessage,
        '生成含数据分析功能的防伪码共计: ', 'codepath'
    )
