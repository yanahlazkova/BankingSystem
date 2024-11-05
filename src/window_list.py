import customtkinter as ctk
import general_methods as gm
from tkinter import messagebox
from .client_window import ClientWindow


class ListWindow(ctk.CTkToplevel):
    """ вікно відображення списку клієнтів або рахунків """

    def __init__(self, title, bank):
        super().__init__()
        # Список назв стовбців та їх довжина
        self.__bank = bank

        if title == "Список рахунків":
            self.__list_columns = {'№п/п': 50, '№ рахунку': 200, 'тип': 80, 'id клієнта': 80, 'власник': 300,
                             'баланс, грн.': 100, 'interest rate, %': 100}
            self.list_length = len(self.__bank.list_accounts)
        elif title == "Список клієнтів":
            self.__list_columns = {'№п/п': 50, 'id клієнта': 100, 'ФІО': 300, 'осн.рахунок': 200}
            self.list_length = len(self.__bank.list_clients)

        self.__padx = self.__pady = 5
        self.__title = title

        self.title(f"Banking System / {title}")

        width_widgets = sum(self.__list_columns[number] for number in self.__list_columns)
        number_widgets = len(self.__list_columns)

        # кількість строк на сторінці 10
        self.number_row = 10

        # висота табилці
        height_table = self.get_table_height()

        width_window = width_widgets + number_widgets * (self.__padx * 2) + 20

        # висота вікна
        height_window = self.get_window_height(height_table)

        gm.center_window(self, width_window, height_window)

        # Робимо вікно модальним
        self.grab_set()

        # self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Назва списку
        self.label_table_title = ctk.CTkLabel(self, text_color='gray',
                                              text=title,
                                              font=ctk.CTkFont(size=16))
        self.label_table_title.grid(row=0, column=0, padx=self.__padx, pady=self.__pady, sticky='nsew')

        # заголовки колонок таблиці
        self.frame_table_titles = ctk.CTkFrame(self, height=28)
        self.frame_table_titles.grid(row=2, column=0, padx=self.__padx, pady=self.__pady, sticky='nsew')

        self.create_table_column_names()

        # строки таблиці
        self.frame_list_accounts = ctk.CTkScrollableFrame(self, corner_radius=5, border_width=1,
                                                          width=width_window,
                                                          height=height_table,
                                                          label_font=ctk.CTkFont(size=16),
                                                          label_text_color='gray',
                                                          )

        self.frame_list_accounts.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.create_table()

        # gm.center_window(self, width_window, height_window)



    def get_table_height(self):
        number_table_row = (self.number_row if self.list_length >= self.number_row else self.list_length)
        table_height = ((28 + self.__padx*2) * number_table_row)
        return table_height

    def get_window_height(self, table_height):
        window_height = table_height + 300
        return window_height

    def create_table_column_names(self):
        # створити назви колонок таблиці

        for index, column_name in enumerate(self.__list_columns):
            title_table_var = ctk.StringVar()
            title_table_var.set(column_name)
            title_table = ctk.CTkEntry(self.frame_table_titles, corner_radius=3, border_width=0,
                                       width=self.__list_columns[column_name],
                                       text_color='gray',
                                       textvariable=title_table_var,
                                       # border_color='black',
                                       state='disabled',
                                       justify="center"
                                       )
            # title_table.bind(sequence=None, command=None, add=None)
            title_table.grid(row=0, column=index, padx=self.__padx, pady=self.__pady, sticky="nsew")

    def create_table(self):
        table = []
        if self.__title == "Список рахунків":
            self.number_table_row = self.__bank.list_accounts
            for index, account in enumerate(self.__bank.list_accounts):
                # print(f'{index + 1}. {account.account_number}')
                table.append({
                    '№ рахунку': account.account_number,
                    'тип': account.type,
                    'id клієнта': account.owner.client_id,
                    'власник': account.owner.name,
                    'баланс': account.balance,
                    'interest rate': account.interest_rate
                })
        elif self.__title == "Список клієнтів":
            self.number_table_row = self.__bank.list_clients
            for index, client in enumerate(self.__bank.list_clients):
                # print(f'{index + 1}. {client.client_id} - {client.name} - ')
                table.append({
                    'id клієнта': client.client_id,
                    'ПІБ': client.name,
                    'осн.рахунок': client.primary_account.account_number
                })

        *list_column, = (self.__list_columns[column] for column in self.__list_columns)

        for i, row in enumerate(table):
            # print(*row)
            row_number_var = ctk.StringVar()
            row_number_var.set(str(i+1))
            row_number = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_number_var,
                                      state='disabled', width=50)
            row_number.grid(row=i, column=0, padx=5, pady=5)
            for j, value in enumerate(row):
                if j == 0:
                    id_client = row['id клієнта']
                # id_client = row['id клієнта']
                row_table_var = ctk.StringVar()
                row_table_var.set(row[value])
                row_table = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_table_var,
                                         width=list_column[j + 1],
                                         state='disabled',
                                         )
                row_table.grid(row=i, column=j+1, padx=5, pady=5)
                row_table.bind("<Button-1>", lambda event, data=id_client: self.open_client_window(data))

                # print(f'{value}: {row[value]}')

    def open_client_window(self, id_client):
        client = gm.find_client_in_list(id_client, self.__bank.list_clients)
        # open window data of client
        window_data_client = ClientWindow(self.__bank, client, self.update_table)

    def update_table(self):
        for widget in self.frame_list_accounts.winfo_children():
            widget.destroy()
        if self.__title == "Список клієнтів":
            self.list_length = len(self.__bank.list_clients)
        elif self.__title == "Список рахунків":
            self.list_length = len(self.__bank.list_accounts)

        table_height = self.get_table_height()
        window_height = self.get_window_height(table_height)

        self.geometry(f'{self.winfo_width()}x{window_height}')
        self.frame_list_accounts.configure(height=table_height)
        print('висота таблиці:', table_height)
        self.create_table_column_names()

        self.create_table()


