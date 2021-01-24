import tkinter as tk
from tkinter import font
import os
import sys
import config
import argparse
from bs4 import BeautifulSoup
from time import sleep
import requests
from colored import fg, bg, attr
def expo(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{config.PROGRAM_NAME} | By : {config.AUTHOR}")
        self.geometry("400x588")
        self.resizable(0, 0)
        self.configure(bg="gray15")
        self.hel15b = font.Font(family="Helvetica", size=15, weight="bold")
        self.ubuntu = font.Font(family="Ubuntu", size=15, weight="normal")
        self.ubuntu_s = font.Font(family="Ubuntu", size=10, weight="normal")
        self.ubuntuMono = font.Font(family="Ubuntu Mono", size=10, weight="normal")
class Main(Application):
    def __init__(self):
        super().__init__()
        self.im = tk.Label(self, text="Insert Your Mail List :", bg="gray25", fg="white", font=self.ubuntu_s)
        self.im.place(x=5, y=6)
        self.entry_box = tk.Text(self, bg="gray25", fg="white", width=55, height=10, borderwidth=0, relief="raised", font=self.ubuntu_s)
        self.entry_box.place(x=5, y=33)
        self.result_box = tk.Text(self, bg="gray25", fg="white", width=37, height=19, borderwidth=0, relief="raised", font=self.ubuntu_s, state='disabled')
        self.result_box.place(x=5, y=220)
        self.result_box.tag_config('NO', foreground="red")
        self.result_box.tag_config('YES', foreground="green")
        self._Log = tk.Label(self, text="Log : Empty :)", width=55, height=2, borderwidth=0, font=self.ubuntuMono, bg="gray25", fg="white")
        self._Log.place(x=5, y=550)
        self.mb = tk.Label(self, text="Status Side Bar  : ", bg="gray25", fg="white", font=self.ubuntu_s)
        self.mb.place(x=275, y=220)
        self.tu = tk.Button(self, text="Unknown : 0", width=13, height=3, borderwidth=0, relief="raised", font=self.ubuntu_s, bg="gray25", fg="white", state='disabled')
        self.tu.place(x=275, y=250)
        self.td = tk.Button(self, text="Die : 0", width=13, height=3, borderwidth=0, relief="raised", font=self.ubuntu_s, bg="gray25", fg="white", state='disabled')
        self.td.place(x=275, y=315)    
        self.tl = tk.Button(self, text="Live : 0", width=13, height=3, borderwidth=0, relief="raised", font=self.ubuntu_s, bg="gray25", fg="white", state='disabled')
        self.tl.place(x=275, y=380)  
        self.ltc = tk.Label(self, text="0 Lines To Check ", bg="gray25", fg="white", font=self.ubuntu_s)
        self.ltc.place(x=275, y=445)      
        self.btn_run = tk.Button(self, text="vaildate", width=9, height=2, borderwidth=0, relief="raised", font=self.ubuntu, bg="green", fg="white", command=self.run)
        self.btn_run.place(x=275, y=480)
        self.bind("<Key>", self.lenall)
    def lenall(self,*args):
        All = self.entry_box.get('1.0', 'end').split('\n')
        while True:
            try:
                All.remove("")
            except ValueError:
                break
        num = len(All)
        if num > 49:
            pass
            return False
        else:
            self.ltc.configure(text="{} Lines To Check ".format(num), fg='white')
    def run(self):
        Lista = self.entry_box.get("1.0", "end").split("\n")
        while True:
            try:
                Lista.remove("")
            except ValueError:
                break
        if len(Lista) > 0:
            try:
                requests.get("https://google.com")
            except:
                self._Log.configure(text="Check Your Network", fg='red')
                return False
            self._Log.configure(text="Log : All Is Good :)", fg='white')
            self.result_box.delete("1.0", "end")
            LIVE= 0
            DIE = 0
            UNKNOWN= 0
            for mail in Lista:
                res = config.check(mail)
                soup = BeautifulSoup(res,features="html.parser").findAll('div',{'class':'success valid'})
                if len(soup) > 0:
                    self.result_box.configure(state='normal')
                    self.result_box.insert('end', "{}\n".format(mail), 'YES')
                    self.result_box.configure(state='disabled')
                    LIVE +=1
                    self.tl.configure(text=f"LIVE : {LIVE}")
                else:
                    self.result_box.configure(state='normal')
                    self.result_box.insert('end', "{}\n".format(mail), 'NO')
                    self.result_box.configure(state='disabled')
                    DIE +=1
                    self.td.configure(text=f"DIE : {DIE}")
        else:
            self._Log.configure(text="Insert Your Mail list in The entry box", fg='red')
def setup():
    main = Main()
    main.iconbitmap(expo("icon.ico"))
    main.mainloop()
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mail', required=False,  help="mail you want to check", default=None)
parser.add_argument('-ml', '--maillist', required=False, help="Path to mail list you want to check", default=None)
args = parser.parse_args()
if __name__ == "__main__":
    if args.mail:
        try:
            requests.get("https://google.com")
        except:
            print("Check Your Network")
            sys.exit(1)
        res = config.check(args.mail)
        soup = BeautifulSoup(res,features="html.parser").findAll('div',{'class':'success valid'})
        if len(soup) > 0:
            print(fg("#00FF00")+soup[0].text+attr("reset"))
        else:
            print("{1}{0} Not Valid{2}".format(args.mail,fg("#f00"),attr("reset")))
    elif args.maillist:
        if config.file_get_contents(args.maillist):
            Lista = config.file_get_contents(args.maillist).split("\n")
            try:
                requests.get("https://google.com")
            except:
                print("Check Your Network")
                sys.exit(1)
            for mail in Lista:
                res = config.check(mail)
                soup = BeautifulSoup(res,features="html.parser").findAll('div',{'class':'success valid'})
                if len(soup) > 0:
                    print(fg("#00FF00")+soup[0].text+attr("reset"))
                else:
                    print("{1}{0} Not Valid{2}".format(mail,fg("#f00"),attr("reset")))
        else:
            print(f"The Path `{args.maillist}` Not Valid")
    else:
        setup()