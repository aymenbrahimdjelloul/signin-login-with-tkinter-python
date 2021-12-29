#written by Aymen.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os.path
import hashlib


root = Tk()
root.title("Login & Signin App")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="purple")

def sign_in():

    def signin_process():
        global firstname, lastname, username, password

        class user_infos:
            firstname = first_name.get()
            lastname = last_name.get()
            username = user_name.get()
            email = e_mail.get()
            password = pass_word.get()

            birthdateyear = birthdate_year.get()
            birthdatemonth = birthdate_month.get()
            birthdateday = birthdate_day.get()
            genderr = gender.get()

        def user_name_used():
            pass

        def create_account():
            spacing = (5 * " ")



            class account_options:

                now = datetime.now()
                current_date = now.strftime("Date :" + "[ " + "%y : %m : %d" + " ]")
                current_time = now.strftime("Time :" + "[ " + "%p %H : %M : %S" + " ]")

            class password_encryption:

                value_password = f"{user_infos.password}"
                hash_func = hashlib.sha256()
                encoded_value = value_password.encode()
                hash_func.update(encoded_value)
                password_hash = hash_func.hexdigest()

            writing_infos = (f"{account_options.current_date}" + spacing + f"{account_options.current_time}" "\r"
            ""+"\r"
            "First name :" + f"{user_infos.firstname}" + "\r"
            "Last name :" + f"{user_infos.lastname}" + "\r"
            "Username :" + f"{user_infos.username}" + "\r"
            "Email :" + f"{user_infos.email}" + "\r"
            ""+"\r"
            "Birth date :" + f"{user_infos.birthdateyear}" + " " + f"{user_infos.birthdatemonth}" + " " + f"{user_infos.birthdateday}"+"\r"
            "Gender :" + f"{user_infos.genderr}"
                             )

            account_file = open("database/" + f"{user_infos.username}" + ".txt", 'w')
            account_file.write(writing_infos)
            account_file.close()

            hash_file = open("database/" + f"{user_infos.username}" + ".hash", 'w')
            hash_file.write(f"{password_encryption.password_hash}")
            hash_file.close()

            messagebox.showinfo(title="Signin done", message="Sign in your account done succesfully.")
            signin_root.destroy()

        account_path = str("database/" + f"{user_infos.username}" + ".txt")
        if os.path.isfile(account_path):
            user_name_used()
        else:
            create_account()

    class combobox_values:
        birthdate__year = ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014"
                           "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006"
                           "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998"
                           "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990"
                           "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982"
                           "1981", "1980", "1979", "1978", "1977", "1976", "1975", "1974"
                           "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966"
                           "1965", "1964", "1963", "1962", "1961", "1960", "1959", "1958"
                           "1957", "1956", "1955", "1954", "1953", "1952", "1951", "1950"
                           "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942"
                           ]

        birthdate__month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        birthdate__day = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                          "17", "18", "19", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
                          ]



    years = f"{combobox_values.birthdate__year}"
    months = f"{combobox_values.birthdate__month}"
    days = f"{combobox_values.birthdate__day}"
    signin_root = Tk()
    signin_root.title("Sign in")
    signin_root.geometry("300x400")
    signin_root.resizable(False, False)

    Label(signin_root, text="Enter your informations to Signin", font=("Arial", 12), fg="purple").pack(side = TOP, pady = 10)
    Label(signin_root, text="Your First name :", font=("Arial",10), fg="black").place( y = 60)
    Label(signin_root, text="Your Last name :", font=("Arial",10), fg="black").place( y = 90)
    Label(signin_root, text="Your user name :", font=("Arial",10), fg="black").place( y = 120)
    Label(signin_root, text="Your Email :", font=("Arial", 10), fg="black").place( y = 150)
    Label(signin_root, text="Your password  :", font=("Arial",10), fg="black").place( y = 180)
    Label(signin_root, text="Your birth date :", font=("Arial", 10), fg="black").place( y = 215)
    Label(signin_root, text="Your Gender :", font=("Arial", 10), fg="black").place( y = 250)
    first_name = Entry(signin_root, width=30, fg="black")
    last_name = Entry(signin_root, width=30, fg="black")
    user_name = Entry(signin_root, width=30, fg="black")
    e_mail = Entry(signin_root, width=30, fg="black")
    pass_word = Entry(signin_root, width=30, show="*", fg="black")
    first_name.place( x = 110, y = 60)
    last_name.place( x = 110, y = 90)
    user_name.place( x = 110, y = 120)
    e_mail.place( x = 110, y = 150)
    pass_word.place( x = 110, y = 180)

    birthdate_year = ttk.Combobox(signin_root,  width=5, values=years, state="readonly")
    birthdate_month = ttk.Combobox(signin_root, width=4, values=months, state="readonly")
    birthdate_day = ttk.Combobox(signin_root, width=4, values=days, state="readonly")
    birthdate_year.set("2021")
    birthdate_month.set("Jan")
    birthdate_day.set("31")
    birthdate_year.place( x = 120, y = 215)
    birthdate_month.place( x = 185, y = 215)
    birthdate_day.place( x = 250, y = 215)

    gender = ttk.Combobox(signin_root, width=5, values=["Male", "Female"], state="readonly")
    gender.set("Male")
    gender.place(x=120, y=250)


    b3 = Button(signin_root, width=40, text="Submit", font=("Orbitron", 14), bg="gray", fg="purple", command=signin_process)
    b3.pack( side= BOTTOM, padx = 50, pady = 10)

def log_in():

    def account():
        class get_infos_account:
            account_for_firstname = open(user_account)
            lines_to_read = [2]
            for position, line in enumerate(account_for_firstname):
                if position in lines_to_read:
                    split_first_name = line.split()[2]
                    first_name = split_first_name[1:100]

            account_for_lastname = open(user_account)
            lines_to_read = [3]
            for position, line in enumerate(account_for_lastname):
                if position in lines_to_read:
                    split_last_name = line.split()[2]
                    last_name = split_last_name[1:100]


        first_name = f"{get_infos_account.first_name}"
        last_name = f"{get_infos_account.last_name}"
        messagebox.showinfo(title="Login Success", message="Hello " + first_name + " " +  last_name + " Welome to your account !")
        login_root.destroy()
        main()


    def login_process():
        class login_values:
            username = username_login.get()
            password = password_login.get()

        def username_confirm():
            global username_confirm, user_account
            username_confirm = False
            user_account = ("database/" + f"{login_values.username}" + ".txt")
            if os.path.isfile(user_account):
                password_confirm()

            if not os.path.isfile(user_account):
                messagebox.showinfo(title="Login Wrong", message="Your username is wrong ! try again.")
                login_root.destroy()
                login_main()


        def password_confirm():
            global password_confirm

            class login_password_hashing:
                value_password = f"{login_values.password}"
                hash_func = hashlib.sha256()
                encoded_value = value_password.encode()
                hash_func.update(encoded_value)
                login_password_hash = hash_func.hexdigest()

            class get_account_password_hash:
                user = f"{login_values.username}"
                with open("database/" + user + ".hash") as f:
                    account_password_hash = f.read()

            login_password = f"{login_password_hashing.login_password_hash}"
            account_password = f"{get_account_password_hash.account_password_hash}"
            if str(login_password) == str(account_password):
                account()
            if str(login_password) != str(account_password):
                messagebox.showinfo(title="Login wrong", message="Your password is wrong ! try again")


        username_confirm()
        password_confirm()

    def login_main():
        global username_login, password_login, login_root
        login_root = Tk()
        login_root.title("Login")
        login_root.geometry("300x200")
        login_root.resizable(False, False)
        login_root.configure()

        Label(login_root, text="Welcome to Login !", font=("Arial", 15), fg="black").pack(side = TOP)
        Label(login_root, text="Username :", font=("Arial", 10), fg="black").place(y = 30)
        Label(login_root, text="Password :", font=("Arial", 10), fg="black").place(y = 70)

        username_login = Entry(login_root, width=30, bg="white", fg="black")
        password_login = Entry(login_root, width=30, bg="white", fg="black")

        username_login.place( x = 80, y = 30)
        password_login.place( x = 80, y = 70)

        b4 = Button(login_root, width=20, text="Login", font=("Orbitron", 13), bg="gray", fg="purple", command=login_process)
        b4.pack( side = BOTTOM, pady = 10)

    login_main()


def main():

    author = Label(root, text="Written by Aymen.", font=("Arial", 10), bg="purple", fg="gray")
    author.pack(side = TOP)

    l1 = Label(root, text="Welcome to Login & Signin App", font=("Arial", 15), bg="purple", fg="gray")
    l1.pack(side = TOP, pady = 10)

    b1 = Button(root, width=20, height=3, text="Sign in", font=("Orbitron", 12), bg="gray", fg="purple", command=sign_in)
    b2 = Button(root, width=20, height=3, text="Login", font=("Orbitron", 12), bg="gray", fg="purple", command=log_in)
    b1.pack(side = TOP, pady = 40)
    b2.pack(side = TOP, pady = 40)

    root.mainloop()
main()