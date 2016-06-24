from datetime import datetime

from tkinter import *

import Data
from Containers import Transaction
from Finance import Register


class TKBook(object):
    def __init__(self):
        # Global variables for the GUI.
        self.labels = []  # The labels that create the transaction list.
        self.new_window = None  # We'll use this to create new child windows.
        self.transaction_list = []  # The list of transactions in the current active account.
        self.categories = []  # The list of transaction categories in the current account.
        self.amounts = []  # How much money each category holds.
        self.total = 0  # Account total.
        self.count = 0  # Used for tracking the number to give to each new transaction.
        self.account_name = "No Account"  # Name of the current account.
        self.root = Tk()  # Main GUI window.
        self.root.minsize(250, 150)
        self.root.title("TKBook")  # Set the main window's title.
        self.menubar = Menu(self.root)  # New menubar for the main window.
        # Displays the current account's name.
        self.s = StringVar()
        self.y = Label(self.root, textvariable=self.s)
        # Displays the current account's total.
        self.t = StringVar()
        self.x = Label(self.root, textvariable=self.t)
        # UI Interaction buttons.
        self.b = Button(self.root, text="Add Transaction", command=self.add_transaction)
        self.b2 = Button(self.root, text="Delete Transaction", command=self.delete)

        # Configure GUI for initial launch.
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        helpmenu.add_command(label="Refresh", command=self.display_list)
        helpmenu.add_command(label="Categories", command=self.show_categories)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=self.menubar)

        self.s.set(self.account_name)
        self.t.set("$" + str(self.total))
        self.y.pack()
        self.x.pack()
        self.b.pack()
        self.b2.pack()

    def new(self):
        """
        Create the window to create a new account file.
        """
        self.new_window = Toplevel()
        z = Label(master=self.new_window, text="Account Name:")
        y = Entry(self.new_window)
        b = Button(master=self.new_window, text="Ok", command=(lambda: self.close_new(y.get())))
        z.pack()
        y.pack()
        b.pack()

    def close_new(self, y):
        """
        Create a new account with name y.
        :param y: string
        """
        self.transaction_list = Data.new(str(y))
        self.labels = []
        self.account_name = str(y)
        self.total = 0
        self.s.set(self.account_name)
        self.t.set('$' + str(self.total))
        self.new_window.destroy()
        for x in self.labels:
            x.destroy()

    def save(self):
        """
        Save the current account to disk.
        """
        Data.save(self.account_name, self.transaction_list)

    def open(self):
        """
        Create the window to open a previous account.
        """
        self.new_window = Toplevel()
        z = Label(master=self.new_window, text="Account Name:")
        y = Entry(self.new_window)
        b = Button(master=self.new_window, text="Ok", command=(lambda: self.close_open(y.get())))
        z.pack()
        y.pack()
        b.pack()

    def close_open(self, y):
        """
        Logic to load an account.
        :param y: string
        """
        self.transaction_list = Data.load(str(y))['transactions']
        self.categories = Data.load(str(y))['categories']
        self.amounts = Data.load(str(y))['category_amounts']
        self.s.set(str(y))
        self.new_window.destroy()
        self.t.set('$' + str(Register.get_total(self.transaction_list)))
        self.display_list()

    def add_transaction(self):
        """
        Open a new window to add a new transaction.
        """
        self.new_window = Toplevel()
        l1 = Label(master=self.new_window, text="Name")
        l2 = Label(master=self.new_window, text="Category")
        l3 = Label(master=self.new_window, text="Amount")
        e1 = Entry(master=self.new_window)
        e2 = Entry(master=self.new_window)
        e3 = Entry(master=self.new_window)
        b1 = Button(master=self.new_window, text="Ok", command=(lambda: self.add_two(e1.get(), e2.get(), e3.get())))
        l1.pack()
        e1.pack()
        l2.pack()
        e2.pack()
        l3.pack()
        e3.pack()
        b1.pack()

    def add_two(self, x, y, z):
        """
        Pass x, y, and z to the logic to create a new Transaction object.
        :param x: string
        :param y: string
        :param z: float
        """
        self.count += 1
        x = Transaction(self.count, x, y, datetime.today(), z)
        self.transaction_list.append(x)
        self.new_window.destroy()
        self.t.set("${0}".format(str(Register.get_total(self.transaction_list))))
        self.display_list()

    def delete(self):
        """
        New window to delete an existing transaction.
        """
        self.new_window = Toplevel()
        l = Label(master=self.new_window, text="Number")
        e = Entry(self.new_window)
        b = Button(master=self.new_window, text="Ok", command=(lambda: self.delete_two(e.get())))
        l.pack()
        e.pack()
        b.pack()

    def delete_two(self, z):
        """
        Logic to delete transaction with number z
        :param z: int
        """
        x = None
        r = None
        for y in self.transaction_list:
            if y.number == int(z):
                x = y
        for y in self.labels:
            text = y.cget("text")
            assert isinstance(text, str)
            text = text.split("\t")
            if text[0] in str(z):
                r = y
        self.transaction_list.remove(x)
        self.labels.remove(r)
        self.new_window.destroy()
        self.t.set("${0}".format(str(Register.get_total(self.transaction_list))))
        self.display_list()

    @staticmethod
    def about():
        """
        Display the 'about' dialog box.
        """
        x = Toplevel()
        z = Label(master=x, text="TKBook")
        w = Label(master=x, text="Version 1.1.0.0")
        y = Label(master=x, text="tkinter frontend for PyBook")
        t = Label(master=x, text="Written by Romulus10")
        b = Button(master=x, text="Ok", command=x.destroy)
        z.pack()
        w.pack()
        y.pack()
        t.pack()
        b.pack()

    def show_categories(self):
        x = Toplevel()
        cat_labels = []
        Label(master=x, text="Category: Value").pack()
        for y in range(len(self.categories)):
            cat_labels.append(Label(master=x, text=(self.categories[y] + ": $" + self.amounts[y])))
        for z in cat_labels:
            z.pack()

    def display_list(self):
        # TODO Format transaction list display.
        """
        Add the list of transactions to the main window.
        """
        for x in self.labels:
            x.destroy()
        self.labels = []
        self.labels.append(Label(master=self.root))
        for x in self.transaction_list:
            self.labels.append(Label(master=self.root,
                                     text=(
                                         '{0}\t{1}\t{2}\t{3}\t\t${4}'.format(x.number, x.name, x.category, x.date,
                                                                             x.value))))
        self.labels.append(Label(master=self.root))
        for y in self.labels:
            y.pack()
