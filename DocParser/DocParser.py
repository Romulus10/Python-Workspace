class Parse(object):
    def __init__(self):
        self.docs = []
        self.input = None
        self.output = None
        self.text = None

    def make(self, file_name, out_file):
        self.get_file(file_name)
        self.parse_text()
        self.gen_out(out_file)

    def get_file(self, file_name):
        self.input = open(file_name, 'r')
        x = self.input.readlines()
        for y in x:
            if '#^^' in y:
                self.docs.append(y)

    def parse_text(self):
        z = []
        for x in self.docs:
            x = x.split()
            x.remove("#")
            x.remove("^")
            x.remove("^")
            x = "".join(x)
            z.append(x)
        self.text = "".join(z)

    def gen_out(self, out_file):
        self.output = open(out_file, 'w')
        self.output.write(self.text)
