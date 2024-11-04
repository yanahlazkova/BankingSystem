import customtkinter as ctk
import general_methods as gm
from .create_client import WindowCreateClient
from .open_account_window import OpenAccountWindow


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
        self.text_new_client.configure(text=self.__current_client.name)
        self.text_generate_account.configure(text="Рахунки клієнта:")

        # Ім'я клієнта
        self.name_var = ctk.StringVar()
        self.name_var.set(self.__current_client.name)
        self.name_client.configure(textvariable=self.name_var)

        # Рахунки клієнта
        self.account_var = ctk.StringVar()
        self.account_var.set(self.__primary_account)
        self.personal_account.configure(textvariable=self.account_var)

        # Кнопки
        self.button_get_account.destroy()

        self.button_open_account = ctk.CTkButton(self.frame_generate_account,
                                                 text="Open new account",
                                                 width=100,
                                                 command=self.open_new_account)

        self.button_open_account.grid(row=4, column=0, padx=10, pady=10, columnspan=3)

        self.button_close.configure(command=self.on_closing)

    def on_closing(self):
        print('closing...')
        self.func_update_table()
        self.destroy()

    def open_new_account(self):
        # open new window for opening of account
        print('Open new account')
        window_open_account = OpenAccountWindow(self.__current_client,
                                                self.bank.open_new_account,
                                                self.bank.generate_new_account_number)
        window_open_account.mainloop()


