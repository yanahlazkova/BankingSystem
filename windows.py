import customtkinter as ctk


class Window(ctk.CTk):
    current_theme = "green"
    current_mode = "dark"

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.width = 400
        self.height = 300

        self.center_window(self.width, self.height)

        ctk.set_default_color_theme(self.current_theme)
        ctk.set_appearance_mode(self.current_mode)

        menu_var = ctk.StringVar(value="option 2")
        self.menu = ctk.CTkOptionMenu(self, values=["option 1", "option 2"],
                                         command=self.menu_callback)

    def center_window(self, width, height):
        """ centering window """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    def menu_callback(choice):
        print("menu dropdown clicked:", choice)
