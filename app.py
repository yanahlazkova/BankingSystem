from src.window import Window
from bank1 import Bank

class App:
    def __init__(self):
        self.my_bank = Bank(mfo_bank=305229)
        self.my_bank.load_from_file(file_name='bank_data1.json')
        self.current_window = Window(self.my_bank)
        self.current_window.mainloop()
        # self.my_bank.save_to_file_json()
