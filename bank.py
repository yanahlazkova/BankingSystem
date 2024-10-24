from clients import Client
import accounts


class Bank:
    __list_clients = []
    __list_accounts = []

    def create_new_client(self):
        """ створення нового клієнта"""
        pass

    def open_new_account(self):
        """ відкриття рахунку"""
        pass

    def transfer_to_account_ather_client(self):
        """ транзакція між рахунками різних клієнтів"""
        pass

    def generate_statement(self):
        """ генерація виписок по рахункам клієнтів"""
        pass

    def save_to_file(self):
        pass

    def download_width_file(self):
        pass
