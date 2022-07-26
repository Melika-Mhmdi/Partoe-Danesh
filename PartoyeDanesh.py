from abc import ABC, abstractmethod
from datetime import time


class part(ABC):
    def __init__(self,ID,Name):
        self.Name=Name
        self.ID=ID

    @abstractmethod
    def c_h_a_n_g_e(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def Show(self):
        pass
    @abstractmethod
    def csv_format(self):
        pass
class Masters(part):
    def __init__(self, ID, name, last_name, phone):
        super(Masters, self).__init__(ID,name)
        self.last_name = last_name
        self.phone = phone

    @property
    def csv_format(self):
        return '%s,%s,%s,%s\n' % \
               (self.ID, self.Name, self.last_name, self.phone)

    @staticmethod
    def c_h_a_n_g_e():
        while True:
            request = int(input(
                "\n\t0-Return\n\t1-Delete\n\t2-Add\n\t3-Update\n\t4-Show"))
            if request == 0:
                ResponsibleforRegistration.show_menu()
            elif request == 1:
                Masters.delete()
            elif request == 2:
                Masters.add()
            elif request == 3:
                Masters.Update()
            elif request == 4:
                Masters.Show()
            else:
                print("Your input is incorrect")

    @staticmethod
    def delete():
        ID = input("Enter ID :")
        lines=TextFile.read("Masters.txt")
        for line in lines:
            Master_str_List=line.rstrip('\r\n').split(',')
            if Master_str_List[0]==ID:
                M_L=line.rstrip('\r\n')
                with open("Masters.txt",'w')as  f:
                    for line in lines:
                        if line.strip('\n')!=M_L:
                            f.write(line)


    @staticmethod
    def add():
        ID = input("Enter ID :")
        name = input("Enter  name :")
        last_name = input("Enter Last name :")
        phone = input("Enter phone :")
        master = Masters(ID, name, last_name, phone)
        TextFile.write('Masters.txt', master.csv_format)

    @staticmethod
    def Update():
      while True:
        ID = input("Enter ID :")
        lines=TextFile.read("Masters.txt")
        for line in lines:
                 Masters_str_List=line.rstrip('\r\n').split(',')
                 if Masters_str_List[0]==ID:
                    print('Enter the word that you want to update\n%s'%line.rstrip('\r\n'))
                    word=input('Exact word :')
                    update_word=input('Update word :')
                    last_Master=line.rstrip('\r\n')
                    Masters_str=line.rstrip('\r\n').replace(word,update_word)
                    with open("Masters.txt",'w')as  f2:
                        for line in lines:
                            if line.strip('\n')!=last_Master:
                                f2.write(line)
                            else:
                                f2.write(Masters_str)
                                f2.write('\n')
                    print("Updated")

        if int(input("\n0-Return")) == 0:
                Masters.c_h_a_n_g_e()
    __Master_list = {}

    @staticmethod
    def Show():
        while True:
            titles = ('ID', 'Name', 'Last Name', 'Phone')
            print('\nMaster\n%s%12s%17s%13s'
                  % (titles[0], titles[1],
                     titles[2], titles[3]))
            dashes_count = sum(len(title) for title in titles) + \
                           (len(titles) - 1) * 11
            for i in range(dashes_count):
                print('-', end='')
            print()

            lines = TextFile.read('Masters.txt')

            for line in lines:
                Master_str_list = line.rstrip('\r\n').split(',')
                master = Masters(*Master_str_list)
                Masters.__Master_list[Master_str_list[0]] = master
                print(
                    '{0}         {1}         {2}         {3}'
                        .format(Master_str_list[0],
                                Master_str_list[1],
                                Master_str_list[2],
                                Master_str_list[3]))
                print()
            a = int(input("\n\t0-Return"))
            if a == 0:
                Masters.c_h_a_n_g_e()

            else:
                print("Your input is incorrect")


class Department(part):
    def __init__(self, department__i_d, name):
        super(Department, self).__init__(department__i_d,name)

    @property
    def csv_format(self):
        return '%s,%s\n' % \
               (self.ID, self.Name)

    @staticmethod
    def c_h_a_n_g_e():
        while True:
            request = int(input(
                "\n\t0-Return\n\t1-Delete\n\t2-Add\n\t3-Update\n\t4-Show"))
            if request == 0:
                ResponsibleforRegistration.show_menu()
            elif request == 1:
                Department.delete()
            elif request == 2:
                Department.add()
            elif request == 3:
                Department.Update()
            elif request == 4:
                Department.Show()
            else:
                print("Your input is incorrect")

    @staticmethod
    def delete():
        ID = input("Enter ID :")
        lines = TextFile.read("department.txt")
        for line in lines:
            Department_str_List = line.rstrip('\r\n').split(',')
            if Department_str_List[0] == ID:
                M_L = line.rstrip('\r\n')
                with open("department.txt", 'w')as  f:
                    for line in lines:
                        if line.strip('\n') != M_L:
                            f.write(line)
    @staticmethod
    def add():
        ID = input("Enter ID :")
        name = input("Enter  name :")
        department = Department(ID, name)
        TextFile.write('department.txt', department.csv_format)

    @staticmethod
    def Update():
        while True:
            ID = input("Enter ID :")
            lines = TextFile.read("department.txt")
            for line in lines:
                Department_str_List = line.rstrip('\r\n').split(',')
                if Department_str_List[0] == ID:
                    print('Enter the word that you want to update\n%s' % line.rstrip('\r\n'))
                    word = input('Exact word :')
                    update_word = input('Update word :')
                    last_Department = line.rstrip('\r\n')
                    Department_str = line.rstrip('\r\n').replace(word, update_word)
                    with open("department.txt", 'w')as  f2:
                        for line in lines:
                            if line.strip('\n') != last_Department:
                                f2.write(line)
                            else:
                                f2.write(Department_str)
                                f2.write('\n')
                    print("Updated")
            if int(input("\n0-Return")) == 0:
                Department.c_h_a_n_g_e()
    __Department_list = {}

    @staticmethod
    def Show():
        while True:
            titles = ('ID', 'Name')
            print('\nDepartment\n%s%12s'
                  % (titles[0], titles[1]))
            dashes_count = sum(len(title) for title in titles) + \
                           (len(titles) - 1) * 11
            for i in range(dashes_count):
                print('-', end='')
            print()

            lines = TextFile.read('Department.txt')

            for line in lines:
                Department_str_list = line.rstrip('\r\n').split(',')
                dep = Department(*Department_str_list)
                Department.__Department_list[Department_str_list[0]] = dep
                print(
                    '{0}         {1}'
                        .format(Department_str_list[0],
                                Department_str_list[1]))
                print()
            a = int(input("\n\t0-Return"))
            if a == 0:
                Department.c_h_a_n_g_e()
            else:
                print("Your input is incorrect")
class Reports:
    @staticmethod
    def menu():
        R=int(input("\n\t0-Return\n\t1-Show the list of students in a course\n\t2-Show  master\'s course list\n\t3-Show the list of courses for a department\n"))
        if R==0:
            pass
        elif R==1:
            course=input("Enter Course ID")
            Lines = TextFile.read("studentCourses.txt")
            for line in Lines:
                if course in line:
                   print(line)
        elif R==2:
            master= input("Enter Master\'s name")
            Lines = TextFile.read("Courses.txt")
            for line in Lines:
                if master in line:
                    print(line)
        elif R==3:
            department = input("Enter Department")
            Lines = TextFile.read("Courses.txt")
            for line in Lines:
                if department in line:
                    print(line)


class ResponsibleforRegistration:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def show_menu():
        while True:
            print('Content Management')
            request = int(input(
                "\n\t0-Return\n\t1-Masters\n\t2-Departments\n\t3-Courses\n\t4-Reports"))
            if request == 0:
                Menu.show_menu()
            elif request == 1:
                Masters.c_h_a_n_g_e()
            elif request == 2:
                Department.c_h_a_n_g_e()
            elif request == 3:
                Courses.c_h_a_n_g_e()
            elif request == 4:
                Reports.menu()
            else:
                print("Your input is incorrect")


class login:
    @staticmethod
    def Login():
        print('Login Form')
        name = input('Name :')
        password = input('password :')
        login.check_pass(name, password)

    __user = {}

    @staticmethod
    def check_pass(name, password):
        Flag = False
        lines = TextFile.read('UserPass.txt')
        for line in lines:
            user_str_list = line.rstrip('\r\n').split(',')
            login.__user[user_str_list[0]] = ResponsibleforRegistration(*user_str_list)
            if user_str_list[0] == name:
                if user_str_list[1] == password:
                    Flag = True
        if Flag == True:
            ResponsibleforRegistration.show_menu()
        else:
            print('User name or password is incorrect')
            print()
            login.Login()


class TextFile:
    @staticmethod
    def read(file_name):
        contents = ''

        f = open(file_name, 'r')
        if f.mode == 'r':
            contents = f.readlines()
            f.close()
        return contents

    @staticmethod
    def write(file_name, contents):
        f = open(file_name, 'a+')
        f.write(contents)
        f.close()


class Menu:
    @staticmethod
    def show_menu():
        print("Your welcome to PartoyeDanesh school")
        while True:
            request = int(input("\n\t1-Student\n\t2-Responsible for registration\n\t3-Exit\n"))
            if request == 1:
                Student.show_menu()
            elif request == 2:
                login.Login()
            elif request == 3:
                print("Thanks for choosing partoye Danesh school\nWe hope to see you soon \nGood luck\n")
                break
            else:
                print("Your input is incorrect")


class Courses(part):

    def __init__(self, Department, ID,name, Duration, Day, Hours, Start_Date, End_Date, Tuition, Master,
                 Prerequisites):
        self.Department = Department
        super(Courses, self).__init__(ID,name)
        self.Duration = Duration
        self.Day = Day
        self.Hours = Hours
        self.Start_Date = Start_Date
        self.End_Date = End_Date
        self.Tuition = Tuition
        self.Master = Master
        self.Prerequisites = Prerequisites

    @property
    def csv_format(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % \
               (
               self.Department, self.ID, self.Name, self.Duration, self.Day, self.Hours, self.Start_Date, self.End_Date,
               self.Tuition, self.Master, self.Prerequisites)

    @staticmethod
    def c_h_a_n_g_e():
        while True:
            request = int(input(
                "\n\t0-Return\n\t1-Delete\n\t2-Add\n\t3-Update\n\t4-Show"))
            if request == 0:
                ResponsibleforRegistration.show_menu()
            elif request == 1:
                Courses.delete()
            elif request == 2:
                Courses.add()
            elif request == 3:
                Courses.Update()
            elif request == 4:
                Courses.Show()
            else:
                print("Your input is incorrect")

    @staticmethod
    def delete():
        ID = input("Enter ID :")
        lines = TextFile.read("Courses.txt")
        for line in lines:
            Courses_str_List = line.rstrip('\r\n').split(',')
            if Courses_str_List[1] == ID:
                M_L = line.rstrip('\r\n')
                with open("Courses.txt", 'w')as  f:
                    for line in lines:
                        if line.strip('\n') != M_L:
                            f.write(line)
    @staticmethod
    def add():
        Lines=TextFile.read("department.txt")
        for line in Lines :
            print(line)
        department = input("Enter Department")
        name = input("Enter name :")
        ID = input("Enter ID :")
        Duration = input("Enter Duration :")
        Day = input("Enter Day :")
        Hours = input("Enter Hours :")
        Start_Date = input("Enter Start Date :")
        End_Date = input("Enter End Date :")
        Tuition = input("Enter Tuition :")
        Master = input("Enter Master :")
        Prerequisites = input("Enter Prerequisites :")
        with open('department.txt') as f , open("Masters.txt") as M:

            if department in f.read():
                if Master in M.read():
                    course = Courses(department, ID, name, Duration, Day, Hours, Start_Date, End_Date, Tuition, Master,
                                     Prerequisites)

                    TextFile.write('Courses.txt', course.csv_format)
                else:
                    r = input("This Master is not Exist\n 0-Return 1-If you want to create it\n ")
                    if r == 0:
                        Courses.c_h_a_n_g_e()
                    elif r == 1:
                        Masters.c_h_a_n_g_e()
                    else:
                        print("Your input is incorrect")
            else:
                    req = input("This department is not Exist\n 0-Return 1-If you want to create it\n ")
                    if req == 0:
                        Courses.c_h_a_n_g_e()
                    elif req == 1:
                       Department.c_h_a_n_g_e()
                    else:
                        print("Your input is incorrect")

    @staticmethod
    def Update():
        while True:
            ID = input("Enter ID :")
            lines = TextFile.read("Courses.txt")
            for line in lines:
                Courses_str_List = line.rstrip('\r\n').split(',')
                if Courses_str_List[0] == ID:
                    print('Enter the word that you want to update\n%s' % line.rstrip('\r\n'))
                    word = input('Exact word :')
                    update_word = input('Update word :')
                    last_Course = line.rstrip('\r\n')
                    Courses_str = line.rstrip('\r\n').replace(word, update_word)
                    with open("Masters.txt", 'w')as  f2:
                        for line in lines:
                            if line.strip('\n') != last_Course:
                                f2.write(line)
                            else:
                                f2.write(Courses_str)
                                f2.write('\n')
                    print("Updated")
            if int(input("\n0-Return")) == 0:
                Courses.c_h_a_n_g_e()
    __Master_list = {}

    @staticmethod
    def Show():
        while True:
            title = (
            'Department', 'Course ID', 'Course Name', 'Duration', 'Day', 'Hours', 'Start Date', 'End Date', 'Tuition',
            'Master', 'Prerequisites')
            print('\n Courses\n%s%17s%19s%16s%11s%13s%18s%16s%15s%14s%19s' % (
            title[0], title[1], title[2], title[3], title[4], title[5], title[6], title[7], title[8],
            title[9], title[10]))
            dashes_count = sum(len(title) for title in title) + \
                           (len(title) - 1) * 8

            for i in range(dashes_count):
                print('-', end='')
            print()
            lines = TextFile.read("Courses.txt")

            for line in lines:
                Courses_str_list = line.rstrip('\r\n').split(',')
                Courses.__Course_list[Courses_str_list[0]] = Courses(*Courses_str_list)
                print(
                    '{0}              {1}             {2}            {3}          {4}           {5}          {6}          {7}           {8}            {9}        {10}'
                        .format(Courses_str_list[0],
                                Courses_str_list[1],
                                Courses_str_list[2],
                                Courses_str_list[3],
                                Courses_str_list[4],
                                Courses_str_list[5],
                                Courses_str_list[6],
                                Courses_str_list[7],
                                Courses_str_list[8],
                                Courses_str_list[9],
                                Courses_str_list[10]))
                print()
            a = int(input("\n\t0-Return"))
            if a == 0:
                Courses.c_h_a_n_g_e()

            else:
                print("Your input is incorrect")

    @staticmethod
    def show_courses():
        while True:
            print("please select your department to display its training courses from the list below ")
            lines=TextFile.read("department.txt")
            for line in lines:
                C_str_List = line.strip('\r\n')
                d=C_str_List.split(',')
                print(C_str_List)
            req =input()

            Courses.print_courses(d[1],req)

    __Course_list = {}

    @staticmethod
    def print_courses(department,user_dep):
        while True:
            titles = (
                'Course ID', 'Course Name', 'Duration', 'Day', 'Hours', 'Start Date', 'End Date', 'Tuition', 'Master',
                'Prerequisites')
            print('\n%s\n%s%15s%12s%7s%9s%14s%12s%11s%10s%17s'
                  % (department, titles[0], titles[1],
                     titles[2], titles[3], titles[4], titles[5], titles[6], titles[7], titles[8], titles[9]))
            dashes_count = sum(len(title) for title in titles) + \
                           (len(titles) - 1) * 4

            for i in range(dashes_count):
                print('-', end='')
            print()
            lines = TextFile.read("Courses.txt")
            for line in lines:
                Courses_str_list = line.strip('\r\n').split(',')
                if int(Courses_str_list[0])==int(user_dep):
                   Courses.__Course_list[Courses_str_list[0]] = Courses(*Courses_str_list)
                   print(
                        '\t{0}          {1}         {2}      {3}   {4}      {5}     {6}       {7}         {8}         {9}  '
                        .format(Courses_str_list[1],
                                Courses_str_list[2],
                                Courses_str_list[3],
                                Courses_str_list[4],
                                Courses_str_list[5],
                                Courses_str_list[6],
                                Courses_str_list[7],
                                Courses_str_list[8],
                                Courses_str_list[9],
                                Courses_str_list[10]))
                   print()
            request = int(input("\n\t0-Return\n\t1-Submit Request\n"))
            if request==0:
                Courses.show_courses()
            elif request==1:
                Courses.Elective_course()
            else:
                print("Your input is incorrect")

    @staticmethod
    def __save_order(order):
        TextFile.write('studentCourses.txt', order.csv_format)
    @staticmethod
    def Elective_course():
        print('\n please enter your information\n')
        name = input('\tName :\n')
        last_name = input('\tLast Name :\n')
        phone = input('\tPhone :\n')
        st = Student(name, last_name, phone)
        order = Order(st,{})
        while True:
            Flag=False
            dep_ID = input('\nPlease select your department ID : \n')
            course_ID=input('\nPlease select your Course ID : \n')
            if course_ID !='0':

                order.courses[dep_ID] = OrderCourse(course_ID,Courses.__Course_list[dep_ID] )
                Courses.__save_order(order)

            i = int(input('\n\t0-Return\n\t1-submit'))
            if i == 0:
                break
            else:
                print('\nThe course you have requested has been recorded\n')
class OrderCourse:
    def __init__(self,courses,department):
        self.courses=courses
        self.department=department

class Order:
    def __init__(self, student,courses):
        self.student = student
        self.courses=courses

    @property
    def csv_format(self):
        for course in self.courses.values:
                return str(course.courses.ID)+','+course.courses.Name+','+self.student.Name+','+self.student.Last_Name



class Student:
    def __init__(self, Name, Last_Name, Phone):
        self.Name = Name
        self.Last_Name = Last_Name
        self.Phone = Phone

    @staticmethod
    def show_menu():
        while True:
            print("please select your option from the list below\n")
            request = int(input("\n\t0-Return\n\t1-Visit courses list\n"))
            if request == 0:
                Menu.show_menu()
            elif request == 1:
                Courses.show_courses()
            else:
                print("Your input is incorrect")





Menu.show_menu()
