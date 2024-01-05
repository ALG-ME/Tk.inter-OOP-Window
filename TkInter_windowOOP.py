import tkinter as tk

class BaseWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Основное окно')
        self.geometry('300x200')
        self.resizable(False, False)

        self.button = tk.Button(self, text='Нажми!', command=self.show_message)
        self.button.pack(pady=20)

    def show_message(self):
        print('Ку это основное окно')


class SubWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title('подкласс окна')
        self.geometry('400x300')

        self.another_button = tk.Button(self, text='Это другая кнопка', command=self.show_another_massage)
        self.another_button.pack(pady=20)

    def show_another_massage(self):
        print('Привет это подкласс окна')


base_window = BaseWindow()

sub_window = SubWindow()

base_window.mainloop()
