import customtkinter as ctk
import general_methods as gm


class Window(ctk.CTk):
    current_theme = "green"
    current_mode = "dark"
    current_frame = None
    show_current_frame = False
    pressed_button_menu = None

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.width = 400
        self.height = 300

        gm.center_window(self, self.width, self.height)

        ctk.set_default_color_theme(self.current_theme)
        ctk.set_appearance_mode(self.current_mode)

        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.create_button_menu()

        self.frame_bank = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_clients = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_accounts = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')

    def show_frame_bank(self):
        print(self.button_menu_bank.cget("hover_color"))
        print(self.button_menu_bank.cget("fg_color"))
        self.frame_bank.grid_rowconfigure(0, weight=1)
        self.frame_bank.grid_columnconfigure(0, weight=1)

        self.button_list_clients = ctk.CTkButton(self.frame_bank, text="Список клієнтів")
        self.button_list_clients.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.button_list_accounts = ctk.CTkButton(self.frame_bank, text="Список рахунків")
        self.button_list_accounts.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.button_add_new_client = ctk.CTkButton(self.frame_bank, text="Add new client", command=self.add_new_client)
        self.button_add_new_client.grid(row=1, column=0, padx=10, pady=10, sticky="ew")



    def show_frame_clients(self):
        self.button_cliens = ctk.CTkButton(self.frame_clients, text="Clients")
        self.button_cliens.grid(row=0, column=0, padx=5, pady=5)

    def show_frame_accounts(self):
        self.button_accounts = ctk.CTkButton(self.frame_accounts, text="Accounts")
        self.button_accounts.grid(row=0, column=0, padx=5, pady=5)



    def create_button_menu(self):
        self.frame_menu = ctk.CTkFrame(self, height=30, corner_radius=5, border_width=1, border_color='green')
        self.frame_menu.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.button_menu_bank = ctk.CTkButton(self.frame_menu, text="Bank", width=80, command=lambda: self.show_frame(self.frame_bank, self.show_frame_bank, self.button_menu_bank))
        self.button_menu_bank.grid(row=0, column=0, padx=5, pady=5)

        self.button_menu_clients = ctk.CTkButton(self.frame_menu, text="Clients", width=80, command=lambda: self.show_frame(self.frame_clients, self.show_frame_clients, self.button_menu_clients))
        self.button_menu_clients.grid(row=0, column=1, padx=5, pady=5)

        self.button_menu_accounts = ctk.CTkButton(self.frame_menu, text="Accounts", width=80, command=lambda: self.show_frame(self.frame_accounts, self.show_frame_accounts, self.button_menu_accounts))
        self.button_menu_accounts.grid(row=0, column=2, padx=5, pady=5)

        # Обновляем размеры виджетов перед получением размеров
        # self.update()
        # print(self.frame_menu.winfo_width())

    def show_frame(self, frame, show_frame, pressed_button):
        if self.current_frame:
            self.current_frame.grid_remove()
            self.pressed_button_menu.configure(fg_color=['#2CC985', '#2FA572'])
            if self.current_frame == frame:
                self.current_frame = None
                return

        self.current_frame = frame
        self.pressed_button_menu = pressed_button
        self.pressed_button_menu.configure(fg_color=['#0C955A', '#106A43'])
        frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        show_frame()

    """ методи меню Банк"""

    def add_new_client(self):
        window_add_client = WindowClient()
        window_add_client.mainloop()

