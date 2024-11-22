import customtkinter as ctk
import general_methods as gm


class OpenAccountWindow(ctk.CTkToplevel):
    list_required_fields = []

    def __init__(self, parent, client, bank):
        super().__init__()
        self.client = client
        self.__bank = bank
        # self.func_generate_number_account = gm.generate_unique_account_number(bank.mfo_bank)
        # self.func_open_new_account = bank.create_new_account()
        # поля, обов'язкові для заповнення
        self.list_required_fields = []
        self.selected_type_account = 0

        self.title(f'Open account {client.name}')

        gm.center_window(self, 400, 300)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Робимо вікно модальним
        self.grab_set()

        self.grid_columnconfigure(0, weight=1)

        self.label_title = ctk.CTkLabel(self, text_color='gray',
                                        text='Відкриття нового рахунку',
                                        font=ctk.CTkFont(size=16)
                                        )
        self.label_title.grid(row=0, padx=10, pady=10, sticky='nsew')

        self.radio_var = ctk.IntVar(value=0)
        self.radiobutton_1 = ctk.CTkRadioButton(self, text="Savings account",
                                                radiobutton_width=15,
                                                radiobutton_height=15,
                                                border_width_unchecked=2,
                                                text_color='gray',
                                                # text_color_disabled='green',
                                                variable=self.radio_var,
                                                command=self.show_frame,
                                                value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self, text="Credit account",
                                                radiobutton_width=15,
                                                radiobutton_height=15,
                                                border_width_unchecked=2,
                                                text_color='gray',
                                                # text_color_disabled='green',
                                                variable=self.radio_var,
                                                command=self.show_frame,
                                                value=2)
        self.radiobutton_3 = ctk.CTkRadioButton(self, text="Deposit account",
                                                radiobutton_width=15,
                                                radiobutton_height=15,
                                                border_width_unchecked=2,
                                                text_color='gray',
                                                # text_color_disabled='green',
                                                variable=self.radio_var,
                                                command=self.show_frame,
                                                value=3)

        self.radiobutton_1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.radiobutton_2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.radiobutton_3.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        # Frame Savings account
        self.frame_savings_account = ctk.CTkFrame(self, border_color='green',
                                                  border_width=1)
        # self.frame_savings_account.grid_rowconfigure(0, weight=1)
        self.frame_savings_account.grid_columnconfigure(0, weight=1)

        self.frame_savings_account.grid_columnconfigure(0, weight=1)
        self.frame_savings_account.grid_columnconfigure(1, weight=1)
        self.frame_savings_account.grid_columnconfigure(2, weight=1)

        self.interest_rate_var = ctk.StringVar()
        self.entry_interest_rate = ctk.CTkEntry(self.frame_savings_account,
                                                text_color='gray',
                                                placeholder_text_color='gray',
                                                placeholder_text='0.00',
                                                justify='right'
                                                )
        self.label_interest_rate = ctk.CTkLabel(self.frame_savings_account,
                                                text_color='gray',
                                                text='%, - фіксована відсоткова ставка')

        self.limit_min_var = ctk.StringVar()
        self.entry_limit_min = ctk.CTkEntry(self.frame_savings_account,
                                            text_color='gray',
                                            placeholder_text_color='gray',
                                            placeholder_text='0.00',
                                            justify='right'
                                            )

        self.label_limit_min = ctk.CTkLabel(self.frame_savings_account,
                                            text_color='gray',
                                            text='UAH, - мінімальна залишкова межа')

        self.entry_interest_on_loan_var = ctk.StringVar()
        self.entry_interest_on_loan = ctk.CTkEntry(self.frame_savings_account,
                                                   text_color='gray',
                                                   placeholder_text_color='gray',
                                                   placeholder_text='0.00',
                                                   justify='right')

        self.label_interest_on_loan = ctk.CTkLabel(self.frame_savings_account,
                                                   text_color='gray',
                                                   text='%, - відсоток по кредиту')

        self.entry_time_period_var = ctk.StringVar()
        self.entry_time_period = ctk.CTkEntry(self.frame_savings_account,
                                              text_color='gray',
                                              placeholder_text_color='gray',
                                              placeholder_text='1',
                                              justify='right')

        self.label_time_period = ctk.CTkLabel(self.frame_savings_account,
                                              text_color='gray',
                                              text='місяців, - період часу')

        self.frame_button = ctk.CTkFrame(self, border_color='green', border_width=1)
        self.frame_button.grid(row=2, column=0, padx=10, pady=10, columnspan=3, sticky='snwe')

        self.frame_button.grid_columnconfigure(0, weight=1)
        self.frame_button.grid_columnconfigure(1, weight=1)
        self.frame_button.grid_columnconfigure(2, weight=1)

        self.button_reset = ctk.CTkButton(self.frame_button, text="Reset", state='disabled',
                                          command=self.destroy)
        self.button_save = ctk.CTkButton(self.frame_button, text='Save', state='disabled',
                                         command=self.add_account)
        self.button_close = ctk.CTkButton(self.frame_button, text='Close',
                                          command=self.destroy)

        self.button_reset.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
        self.button_close.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
        self.button_save.grid(row=0, column=2, padx=10, pady=10, sticky='nswe')

    def show_frame(self):
        self.button_save.configure(state='normal')

        self.frame_savings_account.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky='snwe')

        self.entry_interest_rate.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
        self.label_interest_rate.grid(row=0, column=1, padx=5, pady=10, columnspan=2, sticky='wns')

        # Очищаем все виджеты перед отображением нужных
        for widget in (self.entry_limit_min, self.label_limit_min,
                       self.entry_interest_on_loan, self.label_interest_on_loan,
                       self.entry_time_period, self.label_time_period):
            widget.grid_forget()

        account_type = self.radio_var.get()

        if account_type == 1:  # Savings account
            self.selected_type_account = 'savings'
            self.list_required_fields = [[self.entry_interest_rate, 'відсоткова ставка'],
                                         [self.entry_limit_min, 'min залишкова межа']]

            self.entry_limit_min.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
            self.label_limit_min.grid(row=1, column=1, padx=5, pady=10, columnspan=2, sticky='wns')
        elif account_type == 2:  # Credit account
            self.selected_type_account = 'credit'
            self.list_required_fields = [[self.entry_interest_rate, 'відсоткова ставка'],
                                         [self.entry_interest_on_loan, 'відсоток по кредиту']]

            self.entry_interest_on_loan.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
            self.label_interest_on_loan.grid(row=2, column=1, padx=5, pady=10, columnspan=2, sticky='wns')
        elif account_type == 3:  # Deposit account
            self.selected_type_account = 'deposit'
            self.list_required_fields = [[self.entry_interest_rate, 'відсоткова ставка'],
                                         [self.entry_time_period, 'період часу (в місяцях)']]

            self.entry_time_period.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
            self.label_time_period.grid(row=3, column=1, padx=5, pady=10, columnspan=2, sticky='wns')

    def on_closing(self):
        # print('Closing')
        self.destroy()

    @gm.check_all_fields_filled
    def add_account(self):
        # print("Opening the account...")
        # account_number = gm.generate_unique_account_number(self.__bank.mfo_bank)
        interest_rate = self.entry_interest_rate.get()
        limit_min = None
        interest_on_loan = None
        time_period = None
        match self.selected_type_account:
            case 'savings': limit_min = self.entry_limit_min.get()
            case 'credit': interest_on_loan = self.entry_interest_on_loan.get()
            case 'deposit': time_period = self.entry_time_period.get()

        create_account = self.__bank.create_new_account(self.selected_type_account,
                                                        self.client,
                                                        interest_rate,
                                                        limit_min,
                                                        interest_on_loan,
                                                        time_period)
        if create_account:
            # print(f"open account {self.client}")
            self.destroy()
        else:
            print("Помилка при створенні рахунку")
