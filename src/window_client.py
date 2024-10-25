import customtkinter as ctk


class WindowClient(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Cabinet of client")
