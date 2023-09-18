import tkinter

class main_class:
    def __init__(self,initial):
        #基本となるフレームをインスタンス
        root = tkinter.Tk()

        # ボタン 
        # commandのオプションはボタンを押した場合の動作を指定します

        btn = tkinter.Button(root, text='エコー', command=self.btn_click)
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
        self.txt = tkinter.Entry(width=20)
        #場所決め
        self.txt.place(x=90, y=70)
        #文字初期値挿入
        self.txt.insert(tkinter.END,initial)

        self.txt2 = tkinter.Entry(width=20)
        self.txt2.place(x=90, y=100)


        # 表示
        root.mainloop()


    # clickイベント
    def btn_click(self):
        #入力文字列を獲得する
        get_data =self.txt.get()
        #出力エリアをクリアする
        self.txt2.delete(0, tkinter.END)
        #出力エリアにエコーする
        self.txt2.insert(tkinter.END,get_data)


instance=main_class("初期値")

