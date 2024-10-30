from src.window import Window
from bank import Bank

class App:
    def __init__(self):
        self.my_bank = Bank()
        self.my_bank.download_from_file()
        self.current_window = Window(self.my_bank)
        self.current_window.mainloop()
