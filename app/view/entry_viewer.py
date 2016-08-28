import tkinter as tk
from PIL import Image, ImageTk
import os.path

'''
エントリー画面
Start  ゲーム開始
Exit   ゲーム終了
Score  スコア表の表示
'''

class EntryViewer(tk.Canvas):
    Width = 800  # 画面横幅
    Height = 600  # 画面縦幅
    SideMargin = 100

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        # controller
        self.controller = controller

        # title image size=(300,300)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_title = Image.open(os.path.join(script_dir, 'static/title.png'))
        self.img_title.resize((self.Width-2*self.SideMargin,200))
        self.tkimg_title = ImageTk.PhotoImage(self.img_title)
        self.label_tkimg_title = tk.Label(self,image=self.tkimg_title)
        self.label_tkimg_title.place(relx=0.15,rely=0.1)


        # button Frame
        buttonFrame = tk.Frame(master=self,width=100,height=200)
        self.button_start = tk.Button(buttonFrame, text="Start",command=lambda: None)
        self.button_start.pack(side=tk.TOP)
        self.button_exit = tk.Button(buttonFrame, text="Exit", command=lambda: None)
        self.button_exit.pack(side=tk.TOP)
        self.button_score = tk.Button(buttonFrame, text="Score", command=lambda: None)
        self.button_score.pack(side=tk.TOP)
        buttonFrame.place(relx=0.5,rely=0.5)

        self.pack()

    def animate(self):
        pass
