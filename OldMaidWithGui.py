from tkinter import Canvas, Label, StringVar, OptionMenu, Tk


class FirstGUI:
    def __init__(self):
        self.master = None
        self.choose_player_label = None
        self.choice = None
        self.variable = None
        self.choose_player_menu = None
        self.canvas = None

    def create_first_GUI(self):
        self.choose_player_label = Label(self.master, text='Choose how many players are going to play!',
                                         font="Times 20 italic bold")
        self.choose_player_label.pack(pady=10, padx=0)
        self.variable = StringVar(self.master)
        self.variable.set('Choose')
        self.variable.trace('w', self.choose_player)
        self.choice = ['2', '3', '4', '5']
        self.choose_player_menu = OptionMenu(self.master, self.variable, *self.choice)
        self.choose_player_menu.pack(pady=10, padx=0)

    def choose_player(self, *args):
        if self.variable.get() == '2':
            self.canvas = Canvas(width='1024', height='600')
            self.canvas.pack()

            x = 512
            y = 65

            self.canvas.create_text(x, y, text="Player1", font="Times 20 italic bold")

            x1 = 25
            x2 = 75
            y1 = 100
            y2 = 150

            for i in range(17):
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')

                x1 += 58
                x2 += 58

            x = 512
            y = 315

            self.canvas.create_text(x, y, text="Player2", font="Times 20 italic bold")

            x1 = 50
            x2 = 100
            y1 = 350
            y2 = 400

            for i in range(16):
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
                
                x1 += 58
                x2 += 58


if __name__ == "__main__":
    master = Tk()

    master.title('OldMaid')
    # master.geometry('1024x600')

    first_GUI = FirstGUI()
    first_GUI.create_first_GUI()

    master.mainloop()
