import customtkinter as ctk
import general_methods as gm


class OpenAccountWindow(ctk.CTkToplevel):
    list_required_fields = []

    def __init__(self, client_name):
        super().__init__()
        self.title(f'Open account {client_name}')

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
                                                command=self.show_frame_savings,
                                                value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self, text="Credit account",
                                                radiobutton_width=15,
                                                radiobutton_height=15,
                                                border_width_unchecked=2,
                                                text_color='gray',
                                                # text_color_disabled='green',
                                                variable=self.radio_var,
                                                command=self.show_frame_credit,
                                                value=2)
        self.radiobutton_3 = ctk.CTkRadioButton(self, text="Deposit account",
                                                radiobutton_width=15,
                                                radiobutton_height=15,
                                                border_width_unchecked=2,
                                                text_color='gray',
                                                # text_color_disabled='green',
                                                variable=self.radio_var,
                                                command=self.show_frame_deposit,
                                                value=3)

        self.radiobutton_1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.radiobutton_2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.radiobutton_3.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        self.frame_savings_account = ctk.CTkFrame(self, border_color='green',
                                                  border_width=1)


    def show_frame_savings(self):
        # Frame Savings account
        self.frame_savings_account.grid_rowconfigure(0, weight=1)
        self.frame_savings_account.grid_columnconfigure(0, weight=1)

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

        self.frame_savings_account.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky='snwe')
        self.entry_interest_rate.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
        self.label_interest_rate.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
        self.entry_limit_min.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.label_limit_min.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')


    def show_frame_deposit(self):
        # Frame Deposit account
        self.frame_deposit_account = ctk.CTkFrame(self, border_color='green',
                                                  border_width=1)

        self.interest_rate_var = ctk.StringVar()
        self.entry_interest_rate = ctk.CTkEntry(self.frame_deposit_account,
                                                text_color='gray',
                                                placeholder_text_color='gray',
                                                placeholder_text='0.00'
                                                )
        self.label_interest_rate = ctk.CTkLabel(self.frame_deposit_account,
                                                text_color='gray',
                                                text='%, - відсоткова ставка')

        self.time_period_var = ctk.StringVar()
        self.entry_time_period = ctk.CTkEntry(self.frame_deposit_account,
                                            text_color='gray',
                                            placeholder_text_color='gray',
                                            placeholder_text='0')

        self.label_time_period = ctk.CTkLabel(self.frame_deposit_account,
                                            text_color='gray',
                                            text='місяців, - період часу')

    def show_frame_credit(self):
        # Frame Savings account
        self.frame_savings_account = ctk.CTkFrame(self, border_color='green',
                                                  border_width=1)

        self.interest_rate_var = ctk.StringVar()
        self.entry_interest_rate = ctk.CTkEntry(self.frame_savings_account,
                                                text_color='gray',
                                                placeholder_text_color='gray',
                                                placeholder_text='0'
                                                )
        self.label_interest_rate = ctk.CTkLabel(self.frame_savings_account,
                                                text_color='gray',
                                                text='%, - фіксована відсоткова ставка')

        self.limit_min_var = ctk.StringVar()
        self.entry_limit_min = ctk.CTkEntry(self.frame_savings_account,
                                            text_color='gray',
                                            placeholder_text_color='gray',
                                            placeholder_text='0.00')

        self.label_limit_min = ctk.CTkLabel(self.frame_savings_account,
                                            text_color='gray',
                                            text='UAH, - мінімальна залишкова межа')


    def on_closing(self):
        print('Closing')
        self.destroy()