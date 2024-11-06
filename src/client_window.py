import customtkinter as ctk
import general_methods as gm
from .create_client import WindowCreateClient


class ClientWindow(WindowCreateClient):
    def __init__(self, bank, client, func_update_table):
        super().__init__(bank)
        self.func_update_table = func_update_table
        self.bank = bank
        self.__current_client = client
        self.__id_client = client.client_id

        self.__primary_account = self.__current_client.primary_account.account_number

        self.title(f"Cabinet of client: {self.__current_client.name}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Вікно клієнта
        self.text_new_client.configure(text=f'{self.__current_client.name}\t(id-{self.__current_client.client_id})')
        self.text_generate_account.configure(text="Рахунки клієнта:")

        # Ім'я клієнта та основний рахунок
        self.name_var = ctk.StringVar()
        self.name_var.set(self.__current_client.name)
        self.name_client.configure(textvariable=self.name_var)

        self.account_var = ctk.StringVar()
        self.account_var.set(self.__primary_account)
        self.text_account.configure(text='Особовий рахунок')
        self.personal_account.configure(textvariable=self.account_var)
        self.personal_account.grid(padx=10, columnspan=3)

        self.button_get_account.destroy()
        # Рахунки клієнта


        # Кнопки
        self.button_close.configure(command=self.on_closing)

    def on_closing(self):
        print('closing...')
        self.func_update_table()
        self.destroy()



