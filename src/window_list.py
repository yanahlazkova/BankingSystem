import customtkinter as ctk
import general_methods as gm
from tkinter import messagebox
from .client_window import ClientWindow


class ListWindow(ctk.CTkToplevel):
    """ вікно відображення списку клієнтів або рахунків """

    def __init__(self, title, bank, *list_table, **list_names_column):
        super().__init__()
        # Список назв стовбців та їх довжина
        self.__bank = bank
        self.__list_table = list_table
        self.__list_names_column = list_names_column
        self.__padx = self.__pady = 5
        self.__list_widgets_table = []
        self.__title = title

        self.title(f"Banking System / {title}")

        width_widgets = sum(self.__list_names_column[number] for number in self.__list_names_column)
        number_widgets = len(self.__list_names_column)
        width_window = width_widgets + number_widgets * (self.__padx * 2) + 20
        height_window = (38 * (self.__pady * 2) + 20)
        gm.center_window(self, width_window, height_window)

        # Робимо вікно модальним
        self.grab_set()

        self.grid_columnconfigure(0, weight=1)

        self.frame_list_accounts = ctk.CTkScrollableFrame(self, corner_radius=5, border_width=1,
                                                          width=width_window,
                                                          label_font=ctk.CTkFont(size=16),
                                                          label_text_color='gray',
                                                          label_text=title)

        self.frame_list_accounts.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.create_title_table()

        self.create_table()

    def create_title_table(self):
        # *list_names, = (title for title in self.__list_names_column)
        # print(list_names)

        for index, column_name in enumerate(self.__list_names_column):
            title_table_var = ctk.StringVar()
            title_table_var.set(column_name)
            title_table = ctk.CTkEntry(self.frame_list_accounts, corner_radius=3, border_width=0,
                                       width=self.__list_names_column[column_name],
                                       text_color='gray',
                                       textvariable=title_table_var,
                                       # border_color='black',
                                       state='disabled',
                                       justify="center"
                                       )
            # title_table.bind(sequence=None, command=None, add=None)
            title_table.grid(row=0, column=index, padx=self.__padx, pady=self.__pady, sticky="nsew")

    def create_table(self):
        # список ширини колонок
        *list_column, = (self.__list_names_column[column] for column in self.__list_names_column)
        for i, row in enumerate(self.__list_table):
            print(*row)
            row_number_var = ctk.StringVar()
            row_number_var.set(str(i+1))
            row_number = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_number_var,
                                      state='disabled', width=50)
            row_number.grid(row=i+1, column=0, padx=5, pady=5)
            for j, value in enumerate(row):
                if j == 0:
                    id_client = row[value]
                row_table_var = ctk.StringVar()
                row_table_var.set(row[value])
                row_table = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_table_var,
                                         width=list_column[j + 1],
                                         state='disabled',
                                         )
                row_table.grid(row=i+1, column=j+1, padx=5, pady=5)
                row_table.bind("<Button-1>", lambda event, data=id_client: self.open_detail_window(data))

                # print(f'{value}: {row[value]}')

    def open_detail_window(self, id_client):
        if self.__title == 'Список клієнтів':
            print(id_client)
            # open window data of client
            window_data_client = ClientWindow(self.__bank, id_client)
            # window_data_client.mainloop()

        else:
            # open window data of account
            pass
        # Создание нового окна для отображения информации по строке
        # detail_window = ctk.CTkToplevel(self)
        # detail_window.title("Детали строки")
        # detail_text = "\n".join(f"{key}: {value}" for key, value in row_data.items())
        # label = ctk.CTkLabel(detail_window, text=detail_text)
        # label.pack(padx=10, pady=10)

