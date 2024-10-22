import customtkinter as ctk


class Window(ctk.CTk):
    current_theme = "green"
    current_mode = "dark"
    current_frame = None
    show_current_frame = False

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.width = 400
        self.height = 300

        self.center_window(self.width, self.height)

        ctk.set_default_color_theme(self.current_theme)
        ctk.set_appearance_mode(self.current_mode)

        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.create_button_menu()

        self.frame_bank = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_clients = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_accounts = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')


    def center_window(self, width, height):
        """ centering window """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_button_menu(self):
        self.frame_menu = ctk.CTkFrame(self, height=30, corner_radius=5, border_width=1, border_color='green')
        self.frame_menu.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.button_1 = ctk.CTkButton(self.frame_menu, text="Bank", width=80, command=self.show_frame_bank)
        self.button_1.grid(row=0, column=0, padx=5, pady=5)

        self.button_2 = ctk.CTkButton(self.frame_menu, text="Clients", width=80, command=self.show_frame_cliens)
        self.button_2.grid(row=0, column=1, padx=5, pady=5)

        self.button_3 = ctk.CTkButton(self.frame_menu, text="Accounts", width=80, command=self.show_frame_accounts)
        self.button_3.grid(row=0, column=2, padx=5, pady=5)

        # Обновляем размеры виджетов перед получением размеров
        self.update()
        print(self.frame_menu.winfo_width())

    def show_frame_bank(self):
        self.current_frame = self.frame_bank
        self.show_current_frame = not self.show_current_frame
        if self.show_current_frame:
            self.frame_bank.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        else:
            self.current_frame = None
            self.frame_bank.grid_remove()

    def show_frame_cliens(self):
        self.show_current_frame = not self.show_current_frame
        if self.show_current_frame:
            self.frame_clients.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        else:
            self.current_frame = None
            self.frame_clients.grid_remove()

    def show_frame_accounts(self):
        self.show_current_frame = not self.show_current_frame
        if self.show_current_frame:
            self.frame_accounts.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        else:
            self.current_frame = None
            self.frame_accounts.grid_remove()
