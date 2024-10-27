import customtkinter as ctk
import general_methods as gm
from tkinter import messagebox


class WindowList(ctk.CTkToplevel):
    """ вікно відображення списку клієнтів або рахунків """

    def __init__(self, list_display, list_setting, title):
        super().__init__()
        # Список назв стовбців та їх довжина
        self.__list_setting = list_setting
        self.__list = list_display
        self.__list_widgets_table = []

        self.title(f"Banking System / {title}")

        self.width_first_column = 50 # довжити першого стовба немає в списку

        width_widgets = sum(width[1] for width in self.__list_setting) + self.width_first_column

        width_window = width_widgets + (len(self.__list_setting) + 1) * 10 + 40
        height_window = (38 * 10 + 20)
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

        self.create_table()

    def create_table(self):
        title_number_row_var = ctk.StringVar()
        title_number_row_var.set('№ п/п')
        title_number_row = ctk.CTkEntry(self.frame_list_accounts, text_color='gray',
                                        width=self.width_first_column,
                                        corner_radius=3,
                                        border_width=0,
                                        textvariable=title_number_row_var,
                                        # border_color='black',
                                        state='disabled', justify='center'
                                        )
        title_number_row.grid(row=0, padx=5, pady=5, sticky="nsew")

        for index, column_name in enumerate(self.__list_setting):
            title_table_var = ctk.StringVar()
            title_table_var.set(column_name[0])
            title_table = ctk.CTkEntry(self.frame_list_accounts, corner_radius=3, border_width=0,
                                       width=self.__list_setting[index][1],
                                       text_color='gray',
                                       textvariable=title_table_var,
                                       # border_color='black',
                                       state='disabled',
                                       justify="center"
                                       )
            title_table.grid(row=0, column=(index+1), padx=5, pady=5, sticky="nsew")

        for i, row in enumerate(self.__list):
            row_number_var = ctk.StringVar()
            row_number_var.set(str(i+1))
            row_number = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_number_var,
                                      state='disabled', width=50)
            row_number.grid(row=i+1, column=0, padx=5, pady=5)
            for j, value in enumerate(row):
                row_table_var = ctk.StringVar()
                row_table_var.set(row[value])
                row_table = ctk.CTkEntry(self.frame_list_accounts, textvariable=row_table_var,
                                         width=self.__list_setting[j][1],
                                         state='disabled',
                                         )
                row_table.grid(row=i+1, column=j+1, padx=5, pady=5)
                # print(f'{value}: {row[value]}')



