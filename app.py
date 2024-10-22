from windows import Window


class App:
    def __init__(self):
        self.current_window = Window("Bank System")
        self.current_window.mainloop()