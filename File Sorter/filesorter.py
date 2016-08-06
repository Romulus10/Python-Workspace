import sys

filename0 = sys.argv[1]
filename1 = filename0 + "2"

f0 = open(filename0, 'r')
f1 = open(filename1, 'w')

text = f0.readlines()
for x in text:
    if x == "\n":
        text.remove(text[text.index(x)])
text.sort()
for x in text:
    f1.write(x)

f0.close()
f1.close()
