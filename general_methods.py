def center_window(self, width, height):
    """ centering window """
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    self.geometry(f"{width}x{height}+{x}+{y}")