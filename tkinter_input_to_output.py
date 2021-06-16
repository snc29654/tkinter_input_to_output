import tkinter

# clickイベント
def btn_click():
    #入力文字列を獲得する
    get_data =txt.get()
    #出力エリアをクリアする
    txt2.delete(0, tkinter.END)
    #出力エリアにエコーする
    txt2.insert(tkinter.END,get_data)
#基本となるフレームをインスタンス
root = tkinter.Tk()

# ボタン 
# commandのオプションはボタンを押した場合の動作を指定します

btn = tkinter.Button(root, text='エコー', command=btn_click)
btn.place(x=140, y=170)


# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('Tkinterテスト')

# ラベル
lbl = tkinter.Label(text='入力文字列')
lbl.place(x=10, y=70)

lbl2 = tkinter.Label(text='出力文字列')
lbl2.place(x=10, y=100)

# テキストボックス
#ウイジット作成　部品のこと
txt = tkinter.Entry(width=20)
#場所決め
txt.place(x=90, y=70)
#文字初期値挿入
txt.insert(tkinter.END,"initial")

txt2 = tkinter.Entry(width=20)
txt2.place(x=90, y=100)


# 表示
root.mainloop()

import tkinter

# clickイベント
def btn_click():
#入力文字列を獲得する
    get_data =txt.get()
    #出力エリアをクリアする
    txt2.delete(0, tkinter.END)
    #出力エリアにエコーする
    txt2.insert(tkinter.END,get_data)
#基本となるフレームをインスタンス
root = tkinter.Tk()

# ボタン
# commandのオプションはボタンを押した場合の動作を指定します

btn = tkinter.Button(root, text='エコー', command=btn_click)
btn.place(x=140, y=470)


# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('Tkinterテスト')

# ラベル
lbl = tkinter.Label(text='入力文字列')
lbl.place(x=10, y=170)

lbl2 = tkinter.Label(text='出力文字列')
lbl2.place(x=10, y=300)

# テキストボックス
#ウイジット作成　部品のこと
txt = tkinter.Entry(width=20)
#場所決め
txt.place(x=250, y=170)
#文字初期値挿入
txt.insert(tkinter.END,"initial")

txt2 = tkinter.Entry(width=20)
txt2.place(x=250, y=300)


# 表示
root.mainloop()