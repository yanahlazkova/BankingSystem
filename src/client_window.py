import customtkinter as ctk
import general_methods as gm
from .create_client import WindowCreateClient


class ClientWindow(WindowCreateClient):
    def __init__(self, bank, id_client):
        super().__init__(bank)
        self.__id_client = id_client

        self.__current_client = gm.find_client_in_list(self.__id_client, bank.list_clients)
        self.__base_account = gm.find_account_in_list('BankAccount', self.__current_client.list_accounts)

        print(self.__current_client.name)
        self.title(f"Cabinet of client: {self.__current_client.name}")

        self.text_new_client.configure(text=self.__current_client.name)

        self.name_var = ctk.StringVar()
        self.name_var.set(self.__current_client.name)
        self.name_client.configure(textvariable=self.name_var)

        self.account_var = ctk.StringVar()
        self.account_var.set(self.__base_account.account_number)
        self.personal_account.configure(textvariable=self.account_var)

        self.update()

        self.button_get_account.destroy()
