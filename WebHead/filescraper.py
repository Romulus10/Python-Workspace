def scrape():
    file_name = str(raw_input("file> "))
    keyword = str(raw_input("keyword> "))
    f = open(file_name, "r")
    lines = f.readlines()
    new_lines = []
    f.close()
    for x in lines:
        print(x)
        if keyword in x:
            new_lines.append(x)
            print("\tmatch")
    f = open(file_name, "w")
    for x in new_lines:
        f.write(x + "\n")
    f.close()
    print("File now contains ONLY lines containing the specified keyword.")
