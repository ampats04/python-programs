class digitalRoot:
    def digital_root(n):
        while n >= 10:
            n = sum(map(int, str(n)))
        return n


def main():
    dr = digitalRoot

    print(dr.digital_root(9123131231231231))
    print("Hello world")


if __name__ == "__main__":
    main()
