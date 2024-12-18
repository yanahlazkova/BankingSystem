import json
import random
import datetime

import accounts


def center_window(self, width, height):
    """ centering window """
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    self.geometry(f"{width}x{height}+{x}+{y}")


def check_all_fields_filled(func):
    def wrapper(self, *args, **kwargs):
        list_fields = self.list_required_fields
        count_empty_fields = 0
        for field, name in list_fields:
            if not field.get():
                field.configure(border_color="red")
                count_empty_fields += 1
            else:
                field.configure(border_color=['#979DA2', '#565B5E'])
        if count_empty_fields:
            return
        return func(self, *args, **kwargs)
    return wrapper


def generate_unique_account_number(mfo_bank):
    """Генераці унікального номера рахунку клиента."""
    # Отримання поточної дати та часу
    data = datetime.datetime.now()
    data_part = data.strftime("%Y%m%d%H%M%S")

    # Генеруємо випадкову частину номера
    random_part = random.randint(10, 99)

    return f'UA{random_part}{mfo_bank}{data_part}'


def save_to_file(bank):
    file_name = 'bank_data.json'
    data = {
        'accounts': [account.to_dict() for account in bank.list_accounts],
        'clients': [client.to_dict() for client in bank.list_clients]
    }

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)



# def find_client_in_list(id_client, list_clients: list):
#     client = next((client for client in list_clients if client.client_id == id_client), None)
#     return client


def find_account_in_list(type_account, list_account: list):
    account = next((account for account in list_account if account.type == type_account), None)
    return account


def load_from_file_json():
    print('Loading....')
    file_name = 'bank_data.json'
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

        return data
    except Exception as e:
        print('File does not exist' )
        return {}

def data_setting_list_window(type_window):
    # if type_window == ''
    pass
