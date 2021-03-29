import tkinter as tk
win = tk.Tk()
win.geometry('640x480')
win.resizable(False,False)
win.title('練習 python GUI')  

input_frm = tk.Frame(win,width=640,height=50)
input_frm.pack()
lb = tk.Label(input_frm, text='Type a link like a video or a playlist',fg='black')
lb.place(rely=0.2, relx=0.5, anchor='center')
#設定輸入
input_url = tk.StringVar()
input_et = tk.Entry(input_frm, textvariable=input_url, width=60)
input_et.place(rely=0.75, relx=0.5, anchor='center')
#設定按鈕
def btn_click():   # 按鈕的函式
    print('後面再實作')
btn = tk.Button(input_frm, text='下載', command = btn_click,
                bg='orange', fg='Black')
btn.place(rely=0.75, relx=0.9, anchor='center')

#下載清單區域
dl_frm = tk.Frame(win, width=640, height=280)
dl_frm.pack()
#設定提示文字
lb = tk.Label(dl_frm, text='下載清單',fg='black')
lb.place(rely=0.1, relx=0.5, anchor='center')
#設定顯示清單
listbox = tk.Listbox(dl_frm, width=65, height=15)
listbox.place(rely=0.6, relx=0.5, anchor='center')
#設定捲軸
sbar = tk.Scrollbar(dl_frm)
sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)

listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)
#啟動主視窗
win.mainloop()