import sys


class TextbookFunctions(object):

    def __init__(self):
        self.books = []
        self.dictionaries = []
        self.max_prices = []
        self.min_prices = []
        self.total = 0
    
    def load(self):
        f = open("files/textbooks.txt", "r")
        self.books = f.readlines()
        for y in range(len(self.books)):
            self.books[y] = self.books[y].strip('\n')
            self.books[y] = self.books[y].split(';')
        f.close()

    def format_list(self):
        for y in self.books:
            a = 0
            for z in y:
                a += 1
                print(('\t' * a) + z)
            print()

    def list_to_dict(self):
        for a in self.books:
            y = dict()
            y['title'] = a[0]
            # print(x[0])
            y['isbn'] = a[1]
            # print(x[1])
            y['prices'] = a[2:len(a)]
            # print(x[2:len(x)])
            self.dictionaries.append(y)

    def get_min_prices(self):
        for a in self.dictionaries:
            self.min_prices.append(min(a['prices']))
        for a in self.min_prices:
            self.total += float(a)

    def get_max_prices(self):
        for a in self.dictionaries:
            self.max_prices.append(max(a['prices']))
        self.total = 0
        for a in self.max_prices:
            self.total += float(a)

if __name__ == "__main__":
    sys.stdout = open('files/estimate.txt', 'w')
    print("----------------------------------------")
    print("Textbook Price Estimate - High")
    print("----------------------------------------")
    t = TextbookFunctions()
    t.load()
    t.list_to_dict()
    t.get_max_prices()
    r = 0
    for x in t.dictionaries:
        print(x['title'])
        print(x['isbn'])
        print("\t\t\t\t$" + t.max_prices[r])
        r += 1
    t.total = round(t.total, 2)
    tax = t.total * .06
    tax = round(tax, 2)
    final = round((t.total + tax), 2)
    print("----------------------------------------")
    print("Subtotal: \t\t\t$" + str(t.total))
    print("Tax: \t\t\t\t$" + str(tax))
    print("----------------------------------------")
    print("Total: \t\t\t\t$" + str(final))
    print("----------------------------------------")
    print
    print("-----------------------------------------------------------------------------------------------------------")
    print
    print("----------------------------------------")
    print("Textbook Price Estimate - Average")
    print("----------------------------------------")
    t = TextbookFunctions()
    t.load()
    t.list_to_dict()
    t.get_min_prices()
    low = t.total
    t.get_max_prices()
    high = t.total
    t.average_price = ((low + high) / 2)
    r = 0
    for x in t.dictionaries:
        print(x['title'])
        print("ISBN " + x['isbn'])
        print("\t\t\t\t${0}".format(str((float(t.min_prices[r]) + float(t.max_prices[r])) / 2)))
        r += 1
    tax = t.average_price * .06
    tax = round(tax, 2)
    final = t.average_price + tax
    print("----------------------------------------")
    print("Subtotal: \t\t\t$" + str(t.average_price))
    print("Tax: \t\t\t\t$" + str(tax))
    print("----------------------------------------")
    print("Total: \t\t\t\t$" + str(final))
    print("----------------------------------------")
    print
    print("-----------------------------------------------------------------------------------------------------------")
    print
    print("----------------------------------------")
    print("Textbook Price Estimate - Low")
    print("----------------------------------------")
    t = TextbookFunctions()
    t.load()
    t.list_to_dict()
    t.get_min_prices()
    r = 0
    for x in t.dictionaries:
        print(x['title'])
        print("ISBN " + x['isbn'])
        print("\t\t\t\t$" + t.min_prices[r])
        r += 1
    tax = t.total * .06
    tax = round(tax, 2)
    final = t.total + tax
    print("----------------------------------------")
    print("Subtotal: \t\t\t$" + str(t.total))
    print("Tax: \t\t\t\t$" + str(tax))
    print("----------------------------------------")
    print("Total: \t\t\t\t$" + str(final))
    print("----------------------------------------")
    sys.stdout.close()
