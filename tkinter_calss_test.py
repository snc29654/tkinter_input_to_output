import tkinter

class main_class:
    def __init__(self):
        #基本となるフレームをインスタンス
        root = tkinter.Tk()

        # ボタン 
        # commandのオプションはボタンを押した場合の動作を指定します

        btn = tkinter.Button(root, text='クラス作成', command=self.btn_click)
        btn.place(x=140, y=170)


        # 画面サイズ
        root.geometry('300x200')
        # 画面タイトル
        root.title('Tkinterテスト')


        # 表示
        root.mainloop()


    # clickイベント
    def btn_click(self):
        instance=main_class()
        
instance=main_class()

