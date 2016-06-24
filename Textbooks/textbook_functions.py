import sys

class TextbookFunctions(object):

    def __init__(self):
        self.books = []
    
    def load(self):
        f = open("files/textbooks.txt", "r")
        self.books = f.readlines()
        for x in range(len(self.books)):
            self.books[x] = self.books[x].strip('\n')
            self.books[x] = self.books[x].split(';')
        f.close()

    def format_list(self):
        x = 0
        for y in self.books:
            x= 0
            for z in y:
                x += 1
                print(('\t' * x) + z)
            print()

    def list_to_dict(self):
        self.dictionaries = []
        for x in self.books:
            y = dict()
            y['title'] = x[0]
            #print(x[0])
            y['isbn'] = x[1]
            #print(x[1])
            y['prices'] = x[2:len(x)]
            #print(x[2:len(x)])
            self.dictionaries.append(y)

    def min_prices(self):
        self.min_prices = []
        for x in self.dictionaries:
            self.min_prices.append(min(x['prices']))
        self.total = 0
        for x in self.min_prices:
            self.total += float(x)

    def max_prices(self):
        self.max_prices = []
        for x in self.dictionaries:
            self.max_prices.append(max(x['prices']))
        self.total = 0
        for x in self.max_prices:
            self.total += float(x)

if __name__ == "__main__":
    sys.stdout = open('files/estimate.txt', 'w')
    print("----------------------------------------")
    print("Textbook Price Estimate - High")
    print("----------------------------------------")
    t = TextbookFunctions()
    t.load()
    t.list_to_dict()
    t.max_prices()
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
    print()
    print()
    print("----------------------------------------")
    print("Textbook Price Estimate - Low")
    print("----------------------------------------")
    t = TextbookFunctions()
    t.load()
    t.list_to_dict()
    t.min_prices()
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
