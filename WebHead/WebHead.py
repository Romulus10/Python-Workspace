from pagefinder import PageFinder


def print_file():
    file_name = raw_input("file> ")
    f = open(file_name, 'r')
    text = f.readlines()
    f.close()
    for x in text:
        print(x)


print("Romulus10's WebHead Web Scraper")
cmds = [
    "pagefinder",
    "get_file"
]
done = False
while not done:
    option = raw_input("> ")
    if option == "pagefinder":
        p = PageFinder()
        p.go()
    if option == "get_file":
        print_file()
    if option == "help":
        for x in cmds:
            print(x)
