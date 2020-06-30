#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    studentsystem.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.06.17   13:27
-------------------------------------------------------------------------------
   @Change:   2020.06.22
-------------------------------------------------------------------------------
"""
import re
import os

filename = 'students.txt'


def menu():
    # 输出菜单
    print('''
    ┌───────────────── 学生信息管理系统 ─────────────────┐
    |                                                   |
    |    ================= 功能菜单 ==================   |
    |                                                   | 
    |    1 录入学生信息                                  |
    |    2 查找学生信息                                  |
    |    3 删除学生信息                                  |
    |    4 修改学生信息                                  |
    |    5 排序                                         |
    |    6 统计学生总人数                                |
    |    7 显示所有学生信息                              |
    |    0 退出系统                                      |
    |    ============================================== |
    |    说明：通过数字或↑↓方向键选择菜单                 |
    └───────────────────────────────────────────────────┘
    ''')


def insert():
    student_list = []
    mark = True
    while mark:
        id = input("请输入ID（如1001）: ")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩： "))
            python = int(input("请输入Python成绩： "))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整型数值...重新录入信息")
            continue
        student = {
            "id": id,
            "name": name,
            "English": english,
            "Python": python,
            "C": c
        }
        student_list.append(student)
        input_mark = input("是否继续添加？(y/n): ")
        if input_mark == 'y':
            mark = True
        else:
            mark = False
    save(student_list)
    print("学生信息录入完毕！！！")


def search():
    mark = True
    student_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按 ID 查输入1; 按姓名查输入2: ")
            if mode == '1':
                id = input("请输入学生 ID: ")
            elif mode == '2':
                name = input("请输入学生姓名: ")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, 'r') as file:
                student = file.readlines()
                for l in student:
                    d = dict(eval(l))
                    if id is not '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name is not '':
                        if d['name'] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                input_mark = input("是否继续查询？(y/n): ")
                if input_mark == 'y':
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


def save(students):
    try:
        students_txt = open(filename, 'a')
    except Exception as e:
        students_txt = open(filename, 'w')
    for info in students:
        students_txt.write(str(info) + '\n')
    students_txt.close()


def delete():
    mark = True
    while mark:
        student_id = input("请输入要删除的学生ID: ")
        if student_id is not "":
            if os.path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for l in student_old:
                        d = dict(eval(l))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID 为%s的学生信息已经被删除..." % student_id)
                    else:
                        print("没有找到 ID 为 %s 的学生信息..." % student_id)
            else:
                print("无学生信息...")
                break
            show()
            input_mark = input("是否继续删除？(y/n): ")
            if input_mark == 'y':
                mark = True
            else:
                mark = False


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学生 ID: ")
    with open(filename, 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['id'] == student_id:
                print("找到了这名学生，可以修改他的信息！")
                while True:
                    try:
                        d['name'] = input("请输入姓名：")
                        d['English'] = int(input("请输入英语成绩："))
                        d['Python'] = int(input("请输入Python成绩："))
                        d['C'] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break
                student = str(d)
                wfile.write(student + '\n')
                print("修改成功！")
            else:
                wfile.write(student)
    mark = input("是否继续修改其他学生信息？(y/n): ")
    if mark == 'y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_old = file.readlines()
            student_new = []
        for l in student_old:
            d = dict(eval(l))
            student_new.append(d)
    else:
         return
    asc_or_dsc = input("请选择（0升序；1降序）: ")
    if asc_or_dsc == '0':
        asc_or_dsc_bool = False
    elif asc_or_dsc == '1':
        asc_or_dsc_bool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式(1按英语成绩排序;2按Python成绩排序;3按C成绩排序;0按总成绩排序):")
    if mode == '1':
        student_new.sort(key=lambda x: x['English'], reverse=asc_or_dsc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: x['Python'], reverse=asc_or_dsc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: x['C'], reverse=asc_or_dsc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: x['English'] + x['Python'] + x['C'], reverse=asc_or_dsc_bool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r') as rfile:
            student_old = rfile.readlines()
        for l in student_old:
            student_new.append(eval(l))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择： ")
        option_str = re.sub(r'\D', '', option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


def show_student(studengt_list):
    if not studengt_list:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studengt_list:
        print(
            format_data.format(
                info.get('id'),
                info.get('name'),
                str(info.get('English')),
                str(info.get('Python')),
                str(info.get('C')),
                str(info.get('English') + info.get('Python') + info.get('C')).center(12)
            )
        )


if __name__ == '__main__':
    main()
