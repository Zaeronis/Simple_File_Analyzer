while True:
    fname = input("Enter file name: ")
    if fname.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU TOO!!!~~~")
        continue
    count = 0
    checkcount = 0
    total_words = 0
    total_characters = 0
    longest_word = ""
    long_word_length = 0
    shortest_word = ""
    short_word_length = 1000000
    try:
        fhand = open(fname)
        fcheck = input("Yes/No; Would you like to search for a word?\n")
        if fcheck.lower() == "yes":
            fword = input("Enter word: ")
        elif fcheck.lower() == "no":
            fword = "empty"
        fcount = input("Yes/No; Would you like to count the number of lines?\n")
        fwordcount = input("Yes/No; Would you like to count the number of words?\n")
        fcharcount = input("Yes/No; Would you like to count the number of characters?\n")
        flongest = input("Yes/No; Would you like the longest word and it's length?\n")
        fshortest = input("Yes/No; Would you like the shortest word and it's length?\n")
        for line in fhand:
            count += 1
            split_line = line.split()
            for word in split_line:
                if len(word) > long_word_length:
                    word = word.strip(",.")
                    longest_word = word
                    long_word_length = len(word)
                if len(word) < short_word_length:
                    word = word.strip(",.")
                    shortest_word = word
                    short_word_length = len(word)
            line_length = len(split_line)
            #Debugging lines
            #print(split_line)
            #print(line_length)
            total_words += line_length
            if fword in split_line:
                checkcount += 1
            for word in split_line:
                for char in word:
                    total_characters += 1
        if fcheck.lower() == "yes":
            print(f"'{fword.capitalize()}' appears {checkcount} times in {fname.lower()}")
        if fcount.lower() == "yes":
            print(f"There are {count} lines in the file {fname}")
        if fwordcount.lower() == "yes":
            print(f"There are {total_words} words in the file {fname}")
        if fcharcount.lower() == "yes":
            print(f"There are {total_characters} characters in the file {fname}")
        if flongest.lower() == "yes":
            print(f"The longest word in {fname} is '{longest_word.capitalize()}', being {long_word_length} characters long.")
        if fshortest.lower() == "yes":
            print(f"The shortest word in {fname} is '{shortest_word.capitalize()}', being {short_word_length} characters long.")
        fhand.close()
    except FileNotFoundError:
        if fname.lower() != "exit":
            print("File not found")
    if fname.lower() == "exit":
        fhand.close()
        break
