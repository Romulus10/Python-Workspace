import datetime
import sys
import time

import requests


class BitcoinAccount(object):
    def __init__(self):
        self.current = []
        self.bitcoin_amount = .07359801

    def main(self):
        sys.stdout = open(sys.argv[2], "a")
        sys.stderr = open(sys.argv[2], "a")
        self.load()
        self.update()
        self.save()
        sys.stdout.close()
        sys.stderr.close()
        while True:
            sys.stdout = open(sys.argv[2], "a")
            sys.stderr = open(sys.argv[2], "a")
            time.sleep(60)
            self.update()
            self.save()
            sys.stdout.close()
            sys.stderr.close()

    def update(self):
        print(str(datetime.datetime.now().time()) + " Connecting to Bitstamp.")
        try:
            r = requests.get('https://www.bitstamp.net/api/ticker/')
            print(str(datetime.datetime.now().time()) + " Connected.")
            j = r.json()
            d = j['last']
            now = time.strftime("%a %b %d %H:%M:%S %Y")
            value = float(d) * self.bitcoin_amount
            string = str(d) + ";" + str(self.bitcoin_amount) + ";" + str(now) + ";" + str(value)
            self.current.append(string)
            print(str(datetime.datetime.now().time()) + " New value retrieved.")
        except requests.ConnectionError:
            print(str(datetime.datetime.now().time()) + " Connection failed.")

    def load(self):
        f = open(sys.argv[1], "r")
        self.current = f.readlines()
        f.close()
        for x in range(len(self.current)):
            self.current[x] = self.current[x].strip("\n")
        print(str(datetime.datetime.now().time()) + " Loaded bitcoin file.")

    def save(self):
        f = open(sys.argv[1], "w")
        for x in self.current:
            f.write(x + "\n")
        f.close()
        print(str(datetime.datetime.now().time()) + " Saved to bitcoin file.")

    def print_list(self):
        for x in self.current:
            print(x)


if __name__ == "__main__":
    bc = BitcoinAccount()
    bc.main()
