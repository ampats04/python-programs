from datetime import datetime
from random import random, randrange


class practice:
    def main():
        # instantiate
        a1 = "Angelina"
        a2 = "Ariana"
        a3 = "Lady Gaga"

        strins = "lucky ass ass nigga"
        t = "I am bitch ass nigga %s" % strins

        example = "find me"
        test = "find me here"

        # array of words
        words = ["Hi", "I'm", "Jeremy", "Andy", "F.", "Ampatin"]

        # String join() method
        sentence = " ".join(words)

        # String split() method
        example = "Jeremy Andy Ampatin"
        split_example = example.split()

        # String len() method // return the length of the given string
        not_array_example = len(example)
        array_example = len(split_example)

        # datetime library (date) // return the date today
        today = datetime.now()
        date_time = today.strftime("%m/%d/%y, %H:%M:%Y")

        # String replace() method
        rep = strins.replace("ass nigga", "fucker", 1)

        # String find() method
        find = strins.find("nigga")

        # String List() method // breaks down words to letter
        lst = "Easy"
        list_example = list(lst)

        # Random Numbers (3 types)
        rndom = random()
        rndom_range = randrange(1, 100)
        rndom_float = random.uniform(1, 100)

        # if-else condition in python
        if "nihga" in strins:
            print("nigga yes")
        else:
            print("nigag no")

        if example in test:
            print("Query Found")
        else:
            print("query not found")

        print(a1 + " " + a2 + " " + a3)
        print(t)
        print("The Date Today: " + date_time)
        print("String Replace: " + str(rep))
        print("String Find: " + str(find))
        print("String Join: " + sentence)
        print("String Split: " + str(split_example))

        # print the length of a string (array or not) / String len() method
        print("String length of a word: " + str(not_array_example))
        print("String lenght of an Array: " + str(array_example))

        print("String List: " + str(list_example))

        print("Random Number: " + str(rndom))
        print("Random Number with Range: " + str(rndom_range))
        print("Random Number with Floats: " + str(rndom_float))

    if __name__ == "__main__":
        main()
