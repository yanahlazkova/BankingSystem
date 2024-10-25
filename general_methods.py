import random
import datetime


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
        for field, name in list_fields:
            if not field.get():
                field.configure(border_color="red")
                print(f"Field {name} is empty")
                return
        return func(self, *args, **kwargs)
    return wrapper

def generate_unique_account_number():
    """Генераці унікального номера рахунку клиента."""
    # Отримання поточної дати та часу
    data = datetime.datetime.now()
    data_part = data.strftime("%Y%m%d%H%M%S")

    # Генеруємо випадкову частину номера
    random_part = random.randint(10, 99)

    return data_part, random_part

