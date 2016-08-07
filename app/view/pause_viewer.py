import tkinter as tk
from PIL import Image, ImageTk
import os.path

'''
ポーズ画面
Continue  ゲームに戻る
Exit   タイトルに戻る
'''


class PauseViewer(tk.Canvas):
    Width = 800  # 画面横幅
    Height = 600  # 画面縦幅

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        # controller
        self.controller = controller

        # pause title
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.img_title = Image.open(os.path.join(script_dir, 'static/title.png'))
        self.img_title = self.img_title.resize((273, 84))
        self.tkimg_title = ImageTk.PhotoImage(self.img_title)
        self.label_tkimg_title = tk.Label(self, image=self.tkimg_title)

        # button
        self.button_continue = tk.Button(master, text="Continue", command=lambda: None)
        self.button_exit = tk.Button(master, text="Exit", command=lambda: None)

        # create view
        self.pack()
        self.label_tkimg_title.pack()
        self.button_continue.pack()
        self.button_exit.pack()

    def animate(self):
        pass
