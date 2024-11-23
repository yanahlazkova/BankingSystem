import customtkinter as ctk
import general_methods as gm
from .create_client import WindowCreateClient


class ClientWindow(WindowCreateClient):
    def __init__(self, parent, bank, client_id): #, func_update_table):
        super().__init__(bank)
        # self.func_update_table = func_update_table
        self.parent_window = parent
        # print('parent', type(parent).__name__)
        self.bank = bank
        self._current_client = self.bank.list_clients.find_by_id(client_id)

        self.__primary_account = self._current_client.primary_account

        self.title(f"Cabinet of client: {self._current_client.name}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Вікно клієнта
        self.text_new_client.configure(text=f'ID-{self._current_client.client_id}', text_color='white')
        # Робимо можливість скопіювати ID клієнта при кліку
        self.text_generate_account.configure(text="Рахунки клієнта:")

        # Ім'я клієнта та основний рахунок
        self.fill_out_form()

        self.button_get_account.destroy()

        # Рахунки клієнта

        self.button_open_account.configure(state='normal')

        # Кнопки

        self.button_close.configure(command=self.on_closing)
        self.button_save.configure(state='normal', command=self.save_data)

    def fill_out_form(self):
        self.name_client.configure(state='normal')
        self.name_client.delete(0, "end")
        self.name_client.insert(0, self._current_client.name)

        self.account_var = ctk.StringVar()
        self.account_var.set(self.__primary_account)
        self.text_account.configure(text='Особовий рахунок')
        self.personal_account.configure(textvariable=self.account_var)
        self.personal_account.grid(padx=10, columnspan=3)
        self.show_frame_accounts()

    def on_closing(self):
        # print('closing...')
        if type(self.parent_window).__name__ == 'ListWindow':
            self.parent_window.update_table()
        self.destroy()

    def reset_data(self):
        self.fill_out_form()

    @gm.check_all_fields_filled
    def save_data(self):
        # print('save data', self.name_client.get(), self._current_client.name)
        if self.name_client.get() != self._current_client.name:
            self._current_client.name = self.name_client.get()

    def checking_data_changes(self):
        pass
