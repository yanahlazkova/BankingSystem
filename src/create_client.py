import customtkinter as ctk
import general_methods as gm


class WindowCreateClient(ctk.CTkToplevel):
    # Список полів обов'язкових для заповнення
    list_required_fields = []

    def __init__(self, bank):
        super().__init__()

        self.bank = bank

        self.title("Banking System / Creating a new client...")

        gm.center_window(self, 500, 600)

        # Робимо вікно модальним
        self.grab_set()

        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        # Фрейм з назвою вікна
        self.frame_general = ctk.CTkFrame(self)
        self.frame_general.grid(row=0, padx=10, pady=10, sticky='nsew')

        self.frame_general.columnconfigure(0, weight=1)

        self.label_new_client = ctk.CTkLabel(self.frame_general, text_color='gray', text="Додавання нового клієнта",
                                             font=ctk.CTkFont(size=16))
        self.label_new_client.grid(row=0, padx=10, pady=10, sticky='nsew')

        # Фрейм з даними клієнта
        self.frame_data_client = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_data_client.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.name_var = ctk.StringVar()
        self.name_client = ctk.CTkEntry(self.frame_data_client,
                                        text_color='grey',
                                        placeholder_text="Введіть ПІБ клієнта",
                                        width=300)
        self.name_client.grid(row=0, column=0, padx=20, pady=10, sticky='nsew')
        self.name_client.bind("<KeyRelease>", self.force_uppercase)

        self.list_required_fields.append([self.name_client, "\"ПІБ клієнта\""])

        self.account_var = ctk.StringVar()
        self.account_var.set('UA')
        self.personal_account = ctk.CTkEntry(self.frame_data_client,
                                             text_color='grey',
                                             textvariable=self.account_var,
                                             state='disabled',
                                             width=300)
        self.personal_account.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')

        self.button_get_account = ctk.CTkButton(self.frame_data_client, text="Get account", width=100, command=self.form_new_account)
        self.button_get_account.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        # Фрейм з кнопками Зберегти та закрити

        self.frame_buttons = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_buttons.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_buttons.grid_columnconfigure(0, weight=1)
        self.frame_buttons.grid_rowconfigure(0, weight=1)

        self.button_save = ctk.CTkButton(self.frame_buttons, text="Save",
                                         fg_color=['#0C955A', '#106A43'],
                                         state='disabled',
                                         command=self.add_new_client)
        self.button_save.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.button_close = ctk.CTkButton(self.frame_buttons, text="Close", fg_color='grey', command=self.destroy)
        self.button_close.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.button_close = ctk.CTkButton(self.frame_buttons, text="Reset", command=self.reset_data)
        self.button_close.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def force_uppercase(self, event):
        current_text = self.name_client.get()
        upper_text = current_text.upper()
        self.name_client.delete(0, ctk.END)
        self.name_client.insert(0, upper_text)

    @gm.check_all_fields_filled
    def form_new_account(self):
        """ Створення нового особового рахнутку клієнта"""
        data_part, random_part = gm.generate_unique_account_number()
        new_account = f'UA{random_part}{self.bank.mfo_bank}{data_part}'
        self.account_var.set(new_account)
        self.button_save.configure(fg_color=['#2CC985', '#2FA572'], state='normal')

    def reset_data(self):
        self.name_var.set('')

        self.name_client.configure(textvariable=self.name_var)
        self.account_var.set("UA")
        self.personal_account.configure(textvariable=self.account_var)
        self.button_save.configure(fg_color=['#0C955A', '#106A43'], state='disabled')

    def add_new_client(self):
        new_client = self.name_client.get()
        account_client = self.personal_account.get()
        self.bank.create_new_client(new_client, account_client)