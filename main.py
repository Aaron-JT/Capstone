import tkinter as tk
import tkinter.messagebox
from tkinter import *
import serial as sr
import time
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

global s
s = sr.Serial('COM1', 9600)

data = np.array([])
cond = False


# ===== Login Screen =====
class Win1:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0, 0)
        self.master.title('Log In')
        self.master.geometry('450x250')
        # ===== Image background =====
        imageLogin = PhotoImage(file = 'loginGUI.png')
        self.w = w = tk.Label(master, image = imageLogin)
        w.imageLogin = imageLogin
        # ===== Place of the elements =====
        self.frame = tk.Frame(self.master, bg = 'white')
        w.pack()
        self.frame.place(x = 40, y = 115)

        self.Username = StringVar()
        self.Password = StringVar()

        self.LoginFrame1 = tk.LabelFrame(self.frame, bd = 0, bg = 'white')
        self.LoginFrame1.grid(row = 1, column = 0, pady = 15)
        self.LoginFrame2 = tk.LabelFrame(self.frame, bd = 0, bg = 'white')
        self.LoginFrame2.grid(row = 2, column = 0)
        # ===== Username and password =====
        self.lblUsername = tk.Label(self.LoginFrame1, text = 'Username: ', font = ('Verdana', 13, 'bold'), bg = 'white')
        self.lblUsername.grid(row = 0, column = 0)
        self.txtUser = tk.Entry(self.LoginFrame1, textvariable = self.Username, font = ('Verdana', 12), bg = 'white')
        self.txtUser.grid(row = 0, column = 1)

        self.lblPassword = tk.Label(self.LoginFrame1, text = 'Password: ', font = ('Verdana', 13, 'bold'), bg = 'white')
        self.lblPassword.grid(row = 1, column = 0)
        self.txtPassword = tk.Entry(self.LoginFrame1, show = '*', textvariable = self.Password, font = ('Verdana', 12), bg = 'white')
        self.txtPassword.grid(row = 1, column = 1)
        # ===== Buttons =====
        self.btnLogin = tk.Button(self.LoginFrame2, text = 'Log In', width = 15, command = self.Login_System)
        self.btnLogin.grid(row = 3, column = 0, pady = 10, padx = 5)
        self.btnExit = tk.Button(self.LoginFrame2, text = 'Exit', width = 15, command = self.iExit)
        self.btnExit.grid(row = 3, column = 1, pady = 10, padx = 5)
        self.btnReset = tk.Button(self.LoginFrame2, text = 'Reset', width = 15, command = self.Reset)
        self.btnReset.grid(row = 3, column = 2, pady = 10, padx = 5)

    def Login_System(self):
        u = str(self.Username.get())
        p = str(self.Password.get())
        if u == 'Aaron' and p == 'MariaFernanda':
            self.newWin = tk.Toplevel(self.master)
            self.app = Win2(self.newWin)
            self.master.withdraw()
        else:
            tkinter.messagebox.showinfo('Login Systems', 'Invalid details')
            self.Username.set('')
            self.Password.set('')
            self.txtUser.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUser.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno('Login Systems', 'Confirm if you want to exit')
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.Win2
            return


class Win2:
    def __init__(self, master):
        self.master = master
        self.master.resizable(0, 0)
        self.master.title('Menu')
        self.master.geometry('1000x500')
        # ===== Image background =====
        imageLogin = PhotoImage(file = 'homeGUI.png')
        self.w = w = tk.Label(master, image = imageLogin)
        w.imageLogin = imageLogin
        # ===== Place of the elements =====
        self.frame = tk.Frame(self.master, bg = 'white')
        w.pack()
        self.frame.place(x = 165, y = 10)

        self.OptionFrame1 = tk.LabelFrame(self.frame, bd = 0, bg = 'white')
        self.OptionFrame1.grid(row = 0, column = 0, pady = 10)
        self.OptionFrame2 = tk.LabelFrame(self.frame, bd = 0, bg = 'white')
        self.OptionFrame2.grid(row = 1, column = 0, pady = 10)
        # ===== Button treatments =====
        self.btn1 = tk.Button(self.OptionFrame1, text='Social anxiety', font = ('Verdana', 10, 'italic'), width = 12, command = self.test)
        self.btn1.grid(row = 0, column = 0, pady = 10, padx = 5)
        self.btn2 = tk.Button(self.OptionFrame1, text='anxiety1', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn2.grid(row = 0, column = 1, pady = 10, padx = 5)
        self.btn3 = tk.Button(self.OptionFrame1, text='anxiety2', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn3.grid(row = 0, column = 2, pady = 10, padx = 5)
        self.btn4 = tk.Button(self.OptionFrame1, text='anxiety3', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn4.grid(row = 0, column = 3, pady = 10, padx = 5)
        self.btn5 = tk.Button(self.OptionFrame1, text='anxiety4', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn5.grid(row = 0, column = 4, pady = 10, padx = 5)
        # ===== Option buttons =====
        self.btnExit = tk.Button(self.OptionFrame2, text = 'Exit', width = 15, command = self.iExit)
        self.btnExit.grid(row = 0, column = 0, pady = 10, padx = 5)

    def test(self):
        self.master.withdraw()
        self.newWin = tk.Toplevel(self.master)
        self.app = Win3(self.newWin)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno('Login Systems', 'Confirm if you want to exit')
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.Win2
            return


def plot_start():
    global cond, s
    cond = True
    s.reset_input_buffer()


def plot_stop():
    global cond
    cond = False


class Win3:
    global s
    def __init__(self, master):
        self.master = master
        self.master.resizable(0, 0)
        self.master.title('Anxiety test')
        self.master.geometry('1920x1080')
        # ===== Image background =====
        imageLogin = PhotoImage(file = 'testGUI.png')
        self.w = w = tk.Label(master, image = imageLogin)
        w.imageLogin = imageLogin
        # ===== Place of the elements =====
        w.pack(pady = 0, padx = 0)
        self.createWidgets()

    # ===== Arduino reader =====
    def plot_data(self):
        global cond, data
        if cond:
            ecg = s.readline().decode('utf-8')
            if len(data) < 100:
                data = np.append(data, float(ecg[0:4]))
            else:
                data[0:99] = data[1:100]
                data[99] = float(ecg[0:4])
            self.linesx.set_xdata(np.arange(0, len(data)))
            self.linesx.set_ydata(data)
            self.canvas.draw()
        self.master.after(1, self.plot_data)

    # ===== Figures for plot =====
    def createWidgets(self):
        fig = Figure(figsize = (15, 5), dpi = 75)
        ax = fig.add_subplot(311)
        ay = fig.add_subplot(312)
        az = fig.add_subplot(313)
        # ===== Labels and grids =====
        ax.set_ylabel('Voltage [V]')
        ay.set_ylabel('Conductance [S]')
        az.set_ylabel('O2')
        ax.grid()
        ay.grid()
        az.grid()
        # ===== Axis limits =====
        ax.set_xlim(0, 150)
        ax.set_ylim(0, 1024)
        ay.set_xlim(0, 150)
        az.set_xlim(0, 150)

        fig.tight_layout()

        # ===== Lines to plot =====
        self.linesx = ax.plot([], [])[0]
        self.linesy = ay.plot([], [])[0]
        self.linesz = az.plot([], [])[0]

        canvas = FigureCanvasTkAgg(fig, master = self.master)
        canvas.get_tk_widget().place(x = 170, y = 550, width = 1700, height = 450)
        canvas.draw()
        self.canvas = canvas
        # ===== Buttons to start or stop plots =====
        self.master.update()
        start = tk.Button(self.master, text = 'Start', font = ('Verdana', 12), width = 12, command = lambda: plot_start())
        start.place(x = 250, y = 480)
        self.master.update()
        stop = tk.Button(self.master, text = 'Stop', font = ('Verdana', 12), width = 12, command = lambda: plot_stop())
        stop.place(x = start.winfo_x() + start.winfo_reqwidth() + 20, y = 480)
        # ===== Arduino =====
        s.reset_input_buffer()
        self.master.after(1, self.plot_data)


if __name__ == '__main__':
    root = tk.Tk()
    app = Win1(root)
    root.mainloop()
