import tkinter as tk
INIT_WIDTH = 2
INIT_HEIGHT = 3
INIT_AREASIZE = 12
MAGNIFICATION = 1000
OVAL_QUANTITY_LIMIT = 100

class Oval:
    canvas = None

    def __init__(self, center_x, center_y, start_x, start_y, end_x, end_y, areasize, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.areasize = areasize
        self.width = width
        self.height = height
        self.id = self.canvas.create_oval(self.start_x, self.start_y, self.end_x, self.end_y, outline='black', fill='', width=9)
        self.canvas.tag_bind(self.id, '<2>', self.delete)

    def delete(self, event):
        self.canvas.delete(self.id)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.oval = [None for _ in range(OVAL_QUANTITY_LIMIT)]
        self.master.title('esquisse')
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        # キャンバスの初期化
        self.canvas = tk.Canvas(self, bg='white', width=500, height=500)

        # 面積のテキストボックス
        self.areasize_lbl = tk.Label(text='面積')
        self.areasize_lbl.place(x=10, y=0)
        self.areasize_box = tk.Entry(width=10)
        self.areasize_box.place(x=50, y=0)
        self.areasize_box.insert(tk.END, INIT_AREASIZE)
        self.areasize = self.areasize_box.get()

        # 縦横比のテキストボックス
        # 縦
        self.height_relative_lbl = tk.Label(text='縦')
        self.height_relative_lbl.place(x=150, y=0)
        self.height_relative_box = tk.Entry(width=10)
        self.height_relative_box.place(x=190, y=0)
        self.height_relative_box.insert(tk.END, INIT_HEIGHT)
        self.height_relative = self.height_relative_box.get()

        # 横
        self.width_relative_lbl = tk.Label(text='横')
        self.width_relative_lbl.place(x=290, y=0)
        self.width_relative_box = tk.Entry(width=10)
        self.width_relative_box.place(x=330, y=0)
        self.width_relative_box.insert(tk.END, INIT_WIDTH)
        self.width_relative = self.width_relative_box.get()
        
        # 更新ボタン
        self.areasize_update_button = tk.Button(self, text='更新', command=self.areasize_update)
        self.areasize_update_button.place(x=430, y=0)

        # 移動ボタン
        self.move_button = tk.Button(self, text='移動', command=self.press_move)
        self.move_button.place(x=470, y=0)

        self.canvas.grid(row=1, column=0, columnspan=4)
        self.canvas.bind(sequence='<1>', func=self.create_oval)
        Oval.canvas = self.canvas

    def areasize_update(self):
        # 面積，縦横比の値を更新
        self.areasize = self.areasize_box.get()
        self.height_relative = self.height_relative_box.get()
        self.width_relative = self.width_relative_box.get()

    def press_move(self):
        self.canvas.bind()

    def create_oval(self, event):
        center_x = event.x
        center_y = event.y
        # areasize, width_relative, height_relativeの値をInt型に変換
        try:
            size = float(self.areasize) * MAGNIFICATION
            w = float(self.width_relative)
            h = float(self.height_relative)
            width  = ((size * h) / w) ** 0.5  # 楕円の横の長さ
            height = ((size * w) / h) ** 0.5  # 楕円の縦の長さ
            dist_x = ((size * w) / (4 * h)) ** 0.5    # 中心から楕円の端までの距離(x方向)
            dist_y = ((size * h) / (4 * w)) ** 0.5    # 中心から楕円の端までの距離(y方向)
            Oval(center_x, center_y, center_x-dist_x, center_y-dist_y, center_x+dist_x, center_y+dist_y, size, width, height)
            # self.oval.append(oval)
            self.canvas.delete('error_message')
        except ValueError:
            self.canvas.create_text(100, 100, text='数値を入力してください', fill='red', tags='error_message')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()