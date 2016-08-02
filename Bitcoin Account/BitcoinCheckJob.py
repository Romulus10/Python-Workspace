import sys
import time

import requests


class BitcoinAccount(object):
    def __init__(self):
        self.current = []
        self.bitcoin_amount = .06521442

    def main(self):
        sys.stdout = open("logfile.log", "a")
        self.load()
        self.update()
        self.save()
        sys.stdout.close()
        while True:
            sys.stdout = open("logfile.log", "a")
            time.sleep(60)
            self.update()
            self.save()
            sys.stdout.close()

    def update(self):
        print("Connecting to Bitstamp.")
        try:
            r = requests.get('https://www.bitstamp.net/api/ticker/')
            print("Connected.")
            j = r.json()
            d = j['last']
            now = time.strftime("%a %b %d %H:%M:%S %Y")
            value = float(d) * self.bitcoin_amount
            string = str(d) + ";" + str(self.bitcoin_amount) + ";" + str(now) + ";" + str(value)
            self.current.append(string)
            print("New value retrieved.")
        except requests.ConnectionError:
            print("Connection failed.")

    def load(self):
        f = open("bitcoin.txt", "r")
        self.current = f.readlines()
        f.close()
        for x in range(len(self.current)):
            self.current[x] = self.current[x].strip("\n")
        print("Loaded bitcoin file.")

    def save(self):
        f = open("bitcoin.txt", "w")
        for x in self.current:
            f.write(x + "\n")
        f.close()
        print("Saved to bitcoin file.")

    def print_list(self):
        for x in self.current:
            print(x)


if __name__ == "__main__":
    bc = BitcoinAccount()
    bc.main()
