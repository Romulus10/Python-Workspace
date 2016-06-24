#!/usr/bin/env python

import datetime
import sys

from prettytable import PrettyTable

import Containers
import Data
import Finance
from startGUI import TKBook


class CheckBook(object):
    def __init__(self):
        self.account_name = "none"
        self.total = 0
        self.currentCount = 0
        self.fin = Finance.Register()
        self.transactions = []
        self.categories = []
        self.amounts = []
        self.help = ("\nRomulus10's Quick Checkbook Register\nVersion 1.0.3 - Revision 12\n"
                     "PyBook is a command-line-driven checkbook register system written in Python.\n"
                     "Commands\n"
                     "help - Display this help message.\n"
                     "\tUsage: help\n"
                     "new - Add a new account.\n"
                     "\tUsage: new [name]\n"
                     "save - Save the current account.\n"
                     "\tUsage: save\n"
                     "load - Load a previously created account by name.\n"
                     "\tUsage: load [name]\n"
                     "copy - Copy an account file.\n"
                     "\tUsage: copy [one] [two]\n"
                     "add - Add a new transaction.\n"
                     "\tUsage: add [name] [category] [amount]\n"
                     "delete - Delete a transaction by number.\n"
                     "\tUsage: delete [number]\n"
                     "categories - Show all of the created categories and the values they currently contain.\n"
                     "\tUsage: categories\n"
                     "print - Print out the entire checkbook register.\n"
                     "\tUsage: print\n"
                     "quit - Close the program.\n"
                     "\tUsage: quit")

    def main(self):
        print
        print("Romulus10's Quick Checkbook Register")
        print
        done = False
        while not done:
            print(self.account_name)
            self.total = self.fin.get_total(self.transactions)
            if self.total is None:
                print("$0")
            else:
                print('$' + str(self.total))
            cmd = raw_input('> ')
            cmd = cmd.split(' ')
            while len(cmd) < 4:
                cmd.append('')
            if cmd[0] == "quit":
                done = True
            if cmd[0] == "help":
                print(self.help)
            if cmd[0] == "new":
                if cmd[1] != '':
                    self.transactions = Data.new(cmd[1])
                    self.account_name = cmd[1]
            if cmd[0] == "load":
                if cmd[1] != '':
                    self.transactions = Data.load(cmd[1])["transactions"]
                    self.categories = Data.load(cmd[1])["categories"]
                    self.amounts = Data.load(cmd[1])["category_amounts"]
                    self.account_name = cmd[1]
            if cmd[0] == "save":
                Data.save(self.account_name, self.transactions)
            if cmd[0] == "copy":
                Data.copy(cmd[1], cmd[2])
            if cmd[0] == "add":
                if cmd[1] != '' and cmd[2] != '' and cmd[3] != '':
                    self.add(cmd)
            if cmd[0] == "delete":
                if cmd[1] != '':
                    x = None
                    for y in self.transactions:
                        if y.number == int(cmd[1]):
                            x = y
                    self.transactions.remove(x)
            if cmd[0] == "print":
                t = PrettyTable(["Number", "Name", "Category", "Date", "Amount"])
                for x in self.transactions:
                    t.add_row([x.number, x.name, x.category, x.date, ('$' + str(x.value))])
                print(t)
            if cmd[0] == "categories":
                t = PrettyTable(["Name", "Current Value"])
                for i in range(len(self.categories)):
                    t.add_row([str(self.categories[i]), ('$' + str(self.amounts[i]))])
                print(t)
            if cmd[0] == "gui":
                gui = TKBook()
                gui.root.mainloop()
            print
        print

    def add(self, cmd):
        x = Containers.Transaction(self.currentCount, cmd[1], cmd[2], datetime.date.today(), cmd[3])
        if cmd[2] not in self.categories:
            self.amounts.append(0)
            self.categories.append(cmd[2])
        self.amounts[self.categories.index(cmd[2])] += float(cmd[3])
        self.transactions.append(x)
        self.currentCount += 1


if __name__ == "__main__":
    if "gui" not in sys.argv:
        cb = CheckBook()
        try:
            cb.main()
        except KeyboardInterrupt:
            sys.exit()  # Trying to clean up the KeyboardInterrupt exception thrown when exiting via ^C.
    elif "gui" in sys.argv:
        book = TKBook()
        book.root.mainloop()
