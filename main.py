import simplejson
import tkinter as tk
import tkinter.messagebox
from tkinter import *
import serial as sr
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

global ecg, gsr, hb, spo2
s = sr.Serial('COM3', 115200)

data_ecg = np.array([])
data_gsr = np.array([])
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
        self.btn1 = tk.Button(self.OptionFrame1, text = 'Social anxiety', font = ('Verdana', 10, 'italic'), width = 12, command = self.test)
        self.btn1.grid(row = 0, column = 0, pady = 10, padx = 5)
        self.btn2 = tk.Button(self.OptionFrame1, text = 'anxiety1', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn2.grid(row = 0, column = 1, pady = 10, padx = 5)
        self.btn3 = tk.Button(self.OptionFrame1, text = 'anxiety2', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn3.grid(row = 0, column = 2, pady = 10, padx = 5)
        self.btn4 = tk.Button(self.OptionFrame1, text = 'anxiety3', font = ('Verdana', 10, 'italic'), width = 12)
        self.btn4.grid(row = 0, column = 3, pady = 10, padx = 5)
        self.btn5 = tk.Button(self.OptionFrame1, text = 'anxiety4', font = ('Verdana', 10, 'italic'), width = 12)
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
        self.frame = tk.Frame(self.master, bg = 'white')
        w.pack(pady = 0, padx = 0)
        self.frame.place(x = 1430, y = 30)
        self.createWidgets()

    # ===== Arduino reader =====
    def plot_data(self):
        global cond, data_ecg, data_gsr, ecg, gsr, hb, spo2
        if cond:
            while s.inWaiting() == 0:
                pass
            jsonResult = s.readline()
            try:
                jsonObject = simplejson.loads(jsonResult)
                ecg = jsonObject['ecg']
                gsr = jsonObject['gsr']
                hb = jsonObject['hb']
                spo2 = jsonObject['spo2']
            except Exception:
                pass
            ecg = float(ecg) / 1024 * 5
            gsr = float(gsr)
            if len(data_ecg) < 100:
                data_ecg = np.append(data_ecg, ecg)
                data_gsr = np.append(data_gsr, gsr)
            else:
                data_ecg[0:99] = data_ecg[1:100]
                data_gsr[0:99] = data_gsr[1:100]
                data_ecg[99] = ecg
                data_gsr[99] = gsr
                # ECG plot
            self.linesx.set_xdata(np.arange(0, len(data_ecg)))
            self.linesx.set_ydata(data_ecg)
                # GSR plot
            self.linesy.set_xdata(np.arange(0, len(data_gsr)))
            self.linesy.set_ydata(data_gsr)
                # HB
            self.canvas.draw()
            self.hb_data = tk.Label(self.label_data, text = str(hb), font=('Verdana', 24), width=10, bg = 'white')
            self.hb_data.grid(row = 0, column = 1, pady = 10, padx = 1)
            self.spo2_data = tk.Label(self.label_data, text = str(spo2), font = ('Verdana', 24), width = 10, bg='white')
            self.spo2_data.grid(row = 1, column = 1, pady = 10, padx = 1)
        self.master.after(1, self.plot_data)

    # ===== Figures for plot =====
    def createWidgets(self):
        fig = Figure(figsize = (15, 5), dpi = 75)
            # ECG
        ax = fig.add_subplot(211)
            # GSR
        ay = fig.add_subplot(212)
        # ===== Labels and grids =====
        ax.set_ylabel('Voltage [V]')
        ay.set_ylabel('Conductance [S]')
        ax.grid()
        ay.grid()
        # ===== Axis limits =====
        ax.set_xlim(0, 120)
        ax.set_ylim(1, 3)
        ay.set_xlim(0, 120)
        ay.set_ylim(400, 600)

        fig.tight_layout()

        # ===== Lines to plot =====
        self.linesx = ax.plot([], [], 'k')[0]
        self.linesy = ay.plot([], [], 'k')[0]

        canvas = FigureCanvasTkAgg(fig, master = self.master)
        canvas.get_tk_widget().place(x = 170, y = 550, width = 1700, height = 450)
        canvas.draw()
        self.canvas = canvas
        # ===== HB and SPO2 =====
        self.label_data = tk.LabelFrame(self.frame, bd = 0, bg = 'white')
        self.label_data.grid(row = 2, column = 2, pady = 10)
        self.hb_label = tk.Label(self.label_data, text = 'BPM', font = ('Verdana', 24, 'bold'), width = 10, bg = 'white')
        self.hb_label.grid(row = 0, column = 0, pady = 10, padx = 5)
        self.spo2_label = tk.Label(self.label_data, text = 'SPO2', font = ('Verdana', 24, 'bold'), width = 10, bg = 'white')
        self.spo2_label.grid(row = 1, column = 0, pady = 10, padx = 5)
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
