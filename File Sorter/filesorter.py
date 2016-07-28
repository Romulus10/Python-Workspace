filename0 = input("filename> ")
filename1 = filename + ".txt"
filename2 = filename + "2.txt"

f0 = open(filename1, 'r')
f1 = open(filename2, 'w')

text = f0.readlines()
for x in text:
    if x == "\n":
        text.remove(text.index(x))
text.sort()
for x in text:
    f1.write(x)

f0.close()
f1.close()
