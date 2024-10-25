import customtkinter as ctk
import general_methods as gm
from tkinter import messagebox


class WindowCreateClient(ctk.CTkToplevel):
    # Список полів обов'язкових для заповнення

    def __init__(self, bank):
        super().__init__()
        self.list_required_fields = []

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

        self.frame_general.grid_columnconfigure(0, weight=1)

        self.text_new_client = ctk.CTkLabel(self.frame_general, text_color='gray', text="Додавання нового клієнта",
                                            font=ctk.CTkFont(size=16))
        self.text_new_client.grid(row=0, padx=10, pady=10, sticky='nsew')

        # Дані клієнта
        self.frame_data_client = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_data_client.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_data_client.grid_columnconfigure(0, weight=1)

        # ПІБ клієнта
        self.text_data_clien = ctk.CTkLabel(self.frame_data_client, text_color='gray', text='Данні клієнта')
        self.name_var = ctk.StringVar()
        self.name_client = ctk.CTkEntry(self.frame_data_client,
                                        text_color='grey',
                                        placeholder_text="Введіть ПІБ клієнта")
        self.name_client.bind("<KeyRelease>", self.force_uppercase)

        self.text_data_clien.grid(row=0, column=0, pady=5, padx=10, columnspan=2, sticky="nsew")
        self.name_client.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.list_required_fields.append([self.name_client, "\"ПІБ клієнта\""])

        # Формування рахунку клієнта
        self.frame_generate_account = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_generate_account.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_generate_account.grid_columnconfigure(0, weight=1)

        self.text_generate_account = ctk.CTkLabel(self.frame_generate_account, text_color='gray',
                                                  text="Створення рахунку")

        # # Відсоткова ставка клієнта
        # self.text_interest_rate = ctk.CTkLabel(self.frame_generate_account, text_color="grey",
        #                                        text="Відсоткова ствка:")
        #
        # self.interest_rate_var = ctk.StringVar()
        # self.interest_rate = ctk.CTkEntry(self.frame_generate_account, text_color='gray',
        #                                   # textvariable = self.interest_rate_var,
        #                                   font=ctk.CTkFont(size=14),
        #                                   width=50)
        #
        # self.text_limit_min = ctk.CTkLabel(self.frame_generate_account, text_color="grey",
        #                                    text="Мін.сума залишку:")
        #
        # self.limit_min = ctk.CTkEntry(self.frame_generate_account, text_color='gray',
        #                               font=ctk.CTkFont(size=14),
        #                               width=250)
        #
        # self.text_UAH = ctk.CTkLabel(self.frame_generate_account, text_color='gray', text="UAH", width=50)
        #
        self.text_generate_account.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky='nsew')
        # self.text_interest_rate.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        # self.interest_rate.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        # self.text_limit_min.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        # self.limit_min.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        # self.text_UAH.grid(row=2, column=2, padx=10, pady=10, sticky='e')


        # Entry виводу рахунку клієнта
        self.text_account = ctk.CTkLabel(self.frame_generate_account, text_color='gray', text='Особовий рах.:')

        self.account_var = ctk.StringVar()
        self.account_var.set('UA')
        self.personal_account = ctk.CTkEntry(self.frame_generate_account,
                                             text_color='grey',
                                             textvariable=self.account_var,
                                             state='disabled',
                                             font=ctk.CTkFont(size=14),
                                             width=300)

        self.button_get_account = ctk.CTkButton(self.frame_generate_account, text="Get account", width=100, command=self.generate_new_account)

        self.text_account.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
        self.personal_account.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky='nsew')
        self.button_get_account.grid(row=4, column=0, padx=10, pady=10, columnspan=3)



        # Фрейм з кнопками Зберегти та закрити

        self.frame_buttons = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_buttons.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_buttons.grid_columnconfigure(0, weight=1)

        self.button_save = ctk.CTkButton(self.frame_buttons, text="Save",
                                         # fg_color=['#0C955A', '#106A43'],
                                         fg_color='gray',
                                         state='disabled',
                                         command=self.add_new_client)
        self.button_save.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.button_close = ctk.CTkButton(self.frame_buttons, text="Close", command=self.destroy)
        self.button_close.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.button_reset = ctk.CTkButton(self.frame_buttons, text="Reset", command=self.reset_data)
        self.button_reset.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def force_uppercase(self, event):
        """ Робить ввод символів у верхньому регістрі"""
        current_text = self.name_client.get()
        upper_text = current_text.upper()
        self.name_client.delete(0, ctk.END)
        self.name_client.insert(0, upper_text)

    @gm.check_all_fields_filled
    def generate_new_account(self):
        """ Створення нового особового рахнутку клієнта"""
        data_part, random_part = gm.generate_unique_account_number()
        new_account = f'UA{random_part}{self.bank.mfo_bank}{data_part}'
        self.account_var.set(new_account)
        self.button_save.configure(fg_color=['#2CC985', '#2FA572'], state='normal')
        self.button_get_account.configure(fg_color='gray', state='disabled')
        self.list_required_fields.append([self.personal_account, '\"Personal account\"'])

    def reset_data(self):
        self.name_var.set('')

        self.name_client.configure(textvariable=self.name_var)
        self.account_var.set("UA")
        self.personal_account.configure(textvariable=self.account_var)
        self.button_save.configure(fg_color=['#0C955A', '#106A43'], state='disabled')
        self.button_get_account.configure(fg_color=['#2CC985', '#2FA572'], state='normal')
        self.list_required_fields.remove([self.personal_account, '\"Personal account\"'])


    @gm.check_all_fields_filled
    def add_new_client(self):
        new_client = self.name_client.get()
        account_number = self.personal_account.get()
        if self.bank.create_new_client(new_client, account_number):
            self.destroy()
            messagebox.showinfo(message="Дані збережені")
            # self.reset_data()
