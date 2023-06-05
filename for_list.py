def main():
    list = [
        "Jeremy",
        "Brian",
        "Enrico",
        "Jewel",
        "James",
        "Paul",
        "Michael",
        "Maverick",
        "Raymond",
        "Stephen",
    ]

    # Using a variable as a counter
    for i in range(len(list)):
        print(list[i])

    # taking advantage of the for loop auto-iterrate
    print()
    print("Another Way")
    print()
    for i in list:
        if i[0] is "M":
            print(i)


if __name__ == "__main__":
    main()
