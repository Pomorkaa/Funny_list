# импорт модулей
import hashlib
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import sqlite3
import re
import random
from PIL import Image, ImageTk



connect = sqlite3.connect('data.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users( 
    id INTEGER PIMARY KEY AUTOICREMENT,
    login VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL)
''')

def password_sha256(user_password):
    salt = 'nixao'
    password = bytes(user_password + salt, 'utf-8')
    password_hash = hashlib.sha256(password)
    return (password_hash.hexdigest())

def register():
    login = entLogin.get().strip()
    password = password_sha256(entPassword.get())
    cursor.execute('INSERT INTO users (login, password) VALUES (?,?)',[login,password])
    connect.commit()
    messagebox.showinfo('Регистрация ','Логин ' + login + " успешно зарегистрирован!")



def AuthWindow():
    def STARTGAME():
        def Modul1():
            spisok1 = ["Спеть песню", "Порисовать треугольнички", "Побегать по кругу", "Позвонить другу",
                       "Погулять одному","Нарисовать на стене","Спеть со сцены","Залезть на дерево",
                       "Посмеяться громко", "Посмотреть фильм"]
            return random.choice(spisok1)

        def Modul2():
            spisok2 = ["в костюме супермена", "в чужом свадебном платье", "в зеленых шортах",
                       "в целофановом пакете","в мешке из под картошки","в коробке из под новогодней ёлки",
                       "в костюме чебурека", "в пупырчатой пленке"]
            return random.choice(spisok2)

        def Modul3():
            spisok3 = ["дома в ванной", "в парке", "на центральной улице города",
                       "у моря","в горах", "на пляже", "в глухой деревушке", "в лесу"]
            return random.choice(spisok3)

        def START():
            t4['text'] = h2.get() + '- Отличный день для того, чтобы:'
            t5['text'] = Modul1()
            t6['text'] = Modul2()
            t7['text'] = Modul3()

        def check_null():
            if len(h2.get()) == 0:
                messagebox.showerror('АУУУ',
                                     'Ты не ввел число :( Без тебя я не справлюсь!')
            elif h2checkin.get() == 0:
                messagebox.showerror("Тест на внимательность",
                                     'Ты не нажал чек-бокс "Я молодец". Ну-ка похвали себя, экий сорванец!')
            elif int(h2.get()) > 31:
                ch = messagebox.askquestion('Проверочка',
                                            'Ты улетел на Марс где больше дней в месяце?', )
                if ch == 'yes':
                    START()
                else:
                    messagebox.showerror('Обманывать нехорошо!',
                                         'А если серьезно? Давай попробуем еще раз :)')
            else:
                START()
                

        def DONTPUSH():
            if h4checkin.get() == 0:
                h4checkmes = messagebox.showinfo('МДА...', 'НУ ЗАЧЕЕЕЕЕЕМ? Попросили же не нажимать. '
                                                           'А если все сломается и я не покажу тебе отличный совет?')


        def Close():
            window_new.quit()
            auth.quit()
            root.quit()

        window_new = Tk()
        window_new.title('Твоя интересная жизнь!')
        window_new.geometry("550x500")
        window_new.frame()
        window_new['bg'] = '#66CDAA'

        h = Label(window_new,bg='#66CDAA', text='Привет! Здесь можно найти совет \nкак поднять себе настроение:', font='Candara 18')
        h.place(x=60, y=40)

        h1 = Label(window_new,bg='#66CDAA', text='Какое сегодня число? ', font='Candara 14')
        h1.place(x=60, y=110)

        h2 = Entry(window_new,bg='#66CDAA',width=32, font='Candara 14')
        h2.place(x=80, y=150)

        h2checkin = IntVar(window_new)
        h2check = Checkbutton(window_new,text='Я ввел день! Я молодец!',
                                 variable=h2checkin,
                                 onvalue=1,
                                 offvalue=0,
                                 font='Candara 10',
                                 bg='#66CDAA',
                                 activebackground='#00FA9A')
        h2check.place(x=80, y=180)

        h3 = Button(window_new,text='Нажми меня!',
                    command=check_null,
                    activebackground='#00FA9A',
                    font='Candara 14',
                    bg='#00FFFF',
                    border=4)
        h3.place(x=90, y=210)

        h4checkin = IntVar(window_new)
        h4check = Checkbutton(window_new,text='А меня не нажимай!',
                            font='Candara 14',
                            activeforeground='#DC143C',
                            variable=h4checkin,
                            indicatoron=0,
                            activebackground='red',
                            bg='#00FFFF',
                            border=4,
                            command=DONTPUSH)
        h4check.place(x=260, y=210)

        h5 = Button(window_new,
                    text='Наигрался!',
                    command=Close,
                    activebackground='#00FA9A',
                    font='Candara 14',
                    bg='#00FFFF',
                    border=4)
        h5.place(x=200, y=450)


        t4 = Label(window_new,bg='#66CDAA',text= ' ' , font='Candara 14')
        t4.place(x=80, y=250)
        t5 = Label(window_new,bg='#66CDAA',text=' ' , font='Candara 14')
        t5.place(x=80, y=300)
        t6 = Label(window_new,bg='#66CDAA', text=' ', font='Candara 14')
        t6.place(x=80, y=340)
        t7 = Label(window_new,bg='#66CDAA', text=' ', font='Candara 14')
        t7.place(x=80, y=380)

        window_new.mainloop()

    def userAuth():
        login = entLoginAuth.get().strip()
        password = password_sha256(entPasswordAuth.get())
        cursor.execute('SELECT password FROM users WHERE login = ? AND password =?', [login,password])
        info = cursor.fetchall()
        if len(info)>0:
            auth.withdraw()
            STARTGAME()

        else:
            messagebox.showerror('Авторизация','Неверный пароль')
    root.withdraw()
    auth = Tk()
    auth.geometry('300x400')
    auth.title('Авторизация')
    auth.resizable(0, 0)
    auth['bg'] = '#66CDAA'

    lblMain = Label(auth,
                    text='Авторизация',
                    font='Colibri 20',
                    bg='#66CDAA')
    lblMain.place(x=20, y=20)

    lblLoginAuth = Label(auth ,
                         text='Логин',
                         font='Colibri 14',
                         bg='#66CDAA')
    lblLoginAuth.place(x=20, y=100)

    entLoginAuth = Entry(auth,
                         width=14,
                         font='Colibri 14',
                         bg='#66CDAA')
    entLoginAuth.place(x=100, y=100)

    lblPasswordAuth = Label(auth,
                            bg='#66CDAA',
                            text='Пароль',
                            font='Colibri 14')
    lblPasswordAuth.place(x=20, y=160)

    entPasswordAuth = Entry(auth,
                            width=14,
                            bg='#66CDAA',
                            font='Colibri 14')
    entPasswordAuth.place(x=100, y=160)

    btnAuth = Button(auth,  bg='#00FFFF',
                            text='Войти',
                            font='Colibri 11',
                            activebackground='#00FA9A',
                            command=userAuth,
                            border=4)
    btnAuth.place(x=40, y=200)



root = Tk()
root.geometry('300x400')
root.title('Регистрация')
root.resizable(0,0)
root['bg'] = '#66CDAA'


lblMain = Label(text= 'Регистрация',
                font='Colibri 20',
                bg='#66CDAA')
lblMain.place(x=20,y=20)

lblLogin = Label(text= 'Логин',
                 font='Colibri 14',
                 bg='#66CDAA')
lblLogin.place(x=20, y=100)

entLogin = Entry(width=14 ,
                 bg='#66CDAA',
                 font='Colibri 14' )
entLogin.place(x=100, y=100)

lblPassword = Label(text= 'Пароль',
                    font='Colibri 14',
                    bg='#66CDAA')
lblPassword.place(x=20, y=160)

entPassword = Entry(width=14 ,
                    font='Colibri 14',
                    bg='#66CDAA')
entPassword.place(x=100, y=160)

btnRegister = Button(text='Зарегистрироваться',
                     bg='#00FFFF',
                     font='Colibri 11',
                     activebackground='#00FA9A',
                     command=register,
                     border=4)
btnRegister.place(x=40,y=200)

btnAuth = Button(text='Войти',
                 border=4,
                 font='Colibri 11',
                 bg='#00FFFF',
                 command=AuthWindow,
                 activebackground='#00FA9A')
btnAuth.place(x=40,y=260)

root.mainloop()

