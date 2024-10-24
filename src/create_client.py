import customtkinter as ctk
import general_methods as gm


class WindowAddClient(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Banking System / Creating a new client...")

        gm.center_window(self, 500, 600)

        # Робимо вікно модальним
        self.grab_set()

        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame_data_client = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_data_client.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.name_client = ctk.CTkEntry(self.frame_data_client, placeholder_text="Введіть ім'я")
        self.name_client.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')



        self.frame_buttons = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_buttons.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_buttons.grid_columnconfigure(0, weight=1)
        self.frame_buttons.grid_rowconfigure(0, weight=1)

        self.button_save = ctk.CTkButton(self.frame_buttons, text="Save")
        self.button_save.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.button_close = ctk.CTkButton(self.frame_buttons, text="Close", fg_color='blue', command=self.destroy)
        # self.button_close.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
