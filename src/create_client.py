import customtkinter as ctk
import general_methods as gm
from tkinter import messagebox
from clients import Client
from src.open_account_window import OpenAccountWindow


class WindowCreateClient(ctk.CTkToplevel):

    def __init__(self, bank):
        super().__init__()
        # Список полів обов'язкових для заповнення
        self.list_required_fields = []

        self.bank = bank

        self.title("Banking System / Creating a new client...")

        self._current_client = None

        self.__padx = self.__pady = 10

        gm.center_window(self, 500, 600)

        # Робимо вікно модальним
        self.grab_set()

        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        # Фрейм з назвою вікна
        self.frame_general = ctk.CTkFrame(self)
        self.frame_general.grid(row=0, padx=self.__padx, pady=self.__pady, sticky='nsew')

        self.frame_general.grid_columnconfigure(0, weight=1)

        self.text_new_client = ctk.CTkLabel(self.frame_general, text_color='gray', text="Додавання нового клієнта",
                                            font=ctk.CTkFont(size=16))
        self.text_new_client.grid(row=0, padx=self.__padx, pady=self.__pady, sticky='nsew')

        # Дані клієнта
        self.frame_data_client = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_data_client.grid(row=1, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

        self.frame_data_client.grid_columnconfigure(0, weight=1)
        self.frame_data_client.grid_columnconfigure(1, weight=1)
        self.frame_data_client.grid_columnconfigure(2, weight=1)
        self.frame_data_client.grid_columnconfigure(3, weight=1)

        # ПІБ клієнта та особовий рахунок
        self.text_data_clien = ctk.CTkLabel(self.frame_data_client, text_color='gray', text='Дані клієнта')
        self.name_var = ctk.StringVar()
        self.name_client = ctk.CTkEntry(self.frame_data_client,
                                        text_color='grey',
                                        placeholder_text="Введіть ПІБ клієнта")
        self.name_client.bind("<KeyRelease>", self.force_uppercase)

        self.text_data_clien.grid(row=0, column=0, pady=self.__pady, padx=self.__padx, columnspan=4, sticky="nsew")
        self.name_client.grid(row=1, column=0, padx=self.__padx, pady=self.__pady, columnspan=4, sticky="nsew")

        self.list_required_fields.append([self.name_client, "\"ПІБ клієнта\""])

        self.text_account = ctk.CTkLabel(self.frame_data_client, text_color='gray', text='Особ.рах.:')

        self.account_var = ctk.StringVar()
        self.account_var.set('UA')
        self.personal_account = ctk.CTkEntry(self.frame_data_client,
                                             text_color='grey',
                                             textvariable=self.account_var,
                                             state='disabled',
                                             font=ctk.CTkFont(size=14),
                                             width=300)

        self.button_get_account = ctk.CTkButton(self.frame_data_client, text="Generate", width=80,
                                                command=self.generate_new_account)

        self.text_account.grid(row=2, column=0, padx=5, pady=self.__pady, sticky='nse')
        self.personal_account.grid(row=2, column=1, padx=5, pady=self.__pady, columnspan=2, sticky='nsew')
        self.button_get_account.grid(row=2, column=3, padx=self.__padx, pady=self.__pady, columnspan=3)

        # Формування рахунку клієнта
        self.frame_generate_account = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_generate_account.grid(row=2, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

        self.frame_generate_account.grid_columnconfigure(0, weight=1)

        self.text_generate_account = ctk.CTkLabel(self.frame_generate_account, text_color='gray',
                                                  text="Створення рахунку")

        self.button_open_account = ctk.CTkButton(self.frame_generate_account,
                                                 text="Open new account",
                                                 width=100,
                                                 state='disabled',
                                                 command=self.open_new_account)

        self.button_open_account.grid(row=0, column=0, padx=10, pady=10, columnspan=3)


        self.text_generate_account.grid(row=0, column=0, padx=self.__padx, pady=self.__pady, columnspan=4, sticky='nsew')
        # self.text_interest_rate.grid(row=1, column=0, padx=self.__padx, pady=self.__pady, sticky='w')
        # self.interest_rate.grid(row=1, column=1, padx=self.__padx, pady=self.__pady, sticky='w')
        # self.text_limit_min.grid(row=2, column=0, padx=self.__padx, pady=self.__pady, sticky='w')
        # self.limit_min.grid(row=2, column=1, padx=self.__padx, pady=self.__pady, sticky='w')
        # self.text_UAH.grid(row=2, column=2, padx=self.__padx, pady=self.__pady, sticky='e')


        # Frame рахунку клієнта
        self.frame_accounts = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.accounts_label = ctk.CTkLabel(self.frame_accounts, text_color='gray',text="Рахунки клієнта")
        values = ['Ощадні', 'Кредитні', 'Депозитні']
        self.accounts_seg_batton = ctk.CTkSegmentedButton(self.frame_accounts, values=values,
                                                          command=self.clicker)
        self.combo_list_account = []
        combo_var = ctk.StringVar(self._current_client.primary_account)
        self.accounts_combo = ctk.CTkComboBox(self.frame_accounts)
        self.show_frame_accounts()

        # Фрейм з кнопками Зберегти та закрити

        self.frame_buttons = ctk.CTkFrame(self, corner_radius=5, border_width=1, border_color='green')
        self.frame_buttons.grid(row=4, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

        self.frame_buttons.grid_columnconfigure(0, weight=1)
        self.frame_buttons.grid_columnconfigure(1, weight=1)
        self.frame_buttons.grid_columnconfigure(2, weight=1)

        self.button_save = ctk.CTkButton(self.frame_buttons, text="Save",
                                         # fg_color=['#0C955A', '#106A43'],
                                         # fg_color='gray',
                                         state='disabled',
                                         command=self.add_new_client_to_bank)
        self.button_save.grid(row=0, column=2, padx=self.__padx, pady=self.__pady, sticky="nsew")

        self.button_close = ctk.CTkButton(self.frame_buttons, text="Close", command=self.destroy)
        self.button_close.grid(row=0, column=1, padx=self.__padx, pady=self.__pady, sticky="nsew")

        self.button_reset = ctk.CTkButton(self.frame_buttons, text="Reset", command=self.reset_data)
        self.button_reset.grid(row=0, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

    def show_frame_accounts(self):
        if self._current_client:
            self.frame_accounts.grid(row=3, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")
            self.frame_accounts.grid_columnconfigure(0, weight=1)
            self.accounts_label.grid(row=0, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")
            self.accounts_seg_batton.grid(row=1, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

            self.combo_list_account = self._current_client.list_accounts
            self.combo_list_account.append(self._current_client.primary_account)
            self.accounts_combo.configure(values=self.combo_list_account)
            self.accounts_combo.set(self.combo_list_account[0])
            self.accounts_combo.grid(row=2, column=0, padx=self.__padx, pady=self.__pady, sticky="nsew")

    def clicker(self, value):
        """ Виводить список рахунків з обратим типом """
        print(f'Обрано {value}')

    def choose_account(self):
        pass

    @property
    def current_client(self):
        return self._current_client

    @current_client.setter
    def current_client(self, client):
        self._current_client = client

    def force_uppercase(self, event):
        """ Робить ввод символів у верхньому регістрі"""
        current_text = self.name_client.get()
        upper_text = current_text.upper()
        self.name_client.delete(0, ctk.END)
        self.name_client.insert(0, upper_text)

    @gm.check_all_fields_filled
    def generate_new_account(self):
        """ Створення нового особового рахнутку клієнта"""
        # тут генерується рахунок і створюється новий клієнт

        new_account = gm.generate_unique_account_number(self.bank.mfo_bank)
        self.account_var.set(new_account)

        self.button_save.configure(fg_color=['#2CC985', '#2FA572'], state='normal')
        self.button_get_account.configure(fg_color='gray', state='disabled')
        # self.list_required_fields.append([self.personal_account, '\"Personal account\"'])
        self.button_open_account.configure(state='normal')
        self.name_client.configure(state='disabled')

        # створення клієнта
        client_name = self.name_client.get()
        account_number = self.personal_account.get()
        self._current_client = self.bank.create_new_client(client_name, account_number)
        print(self._current_client)



    # @gm.check_all_fields_filled
    def reset_data(self):
        """ Скид усіх введених даних """
        self._current_client = None
        self.name_var.set('')
        self.name_client.configure(state='normal', textvariable=self.name_var)
        self.account_var.set("UA")
        self.personal_account.configure(textvariable=self.account_var)
        self.button_save.configure(fg_color=['#0C955A', '#106A43'], state='disabled')
        self.button_get_account.configure(fg_color=['#2CC985', '#2FA572'], state='normal')
        self.button_open_account.configure(state='disabled')



    @gm.check_all_fields_filled
    def add_new_client_to_bank(self):
        """ Додавання нового клієнта в список клієнтів банку"""
        if self._current_client:
            self._current_client.name = self.name_client.get()
            self.bank.list_clients = self._current_client
            if messagebox.askokcancel('Saving',
                                      message="Дані збережені\nДодати наступного клієнта?"):
                self.reset_data()
            else:
                self.destroy()
                from src.client_window import ClientWindow
                ClientWindow(self, self.bank, self._current_client.client_id)

    @gm.check_all_fields_filled
    def open_new_account(self):
        # open new window for opening of account
        print('Open new account')

        if self._current_client:
            window_open_account = OpenAccountWindow(self, self._current_client, self.bank)
            window_open_account.mainloop()

    def update_table(self):
        print('update у вікні клієнта')