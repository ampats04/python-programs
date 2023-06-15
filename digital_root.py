class digitalRoot:
    def digital_root(n):
        convert = str(n)

        if (len(list(convert))) == 1:
            return n

        else:
            output = map(int, convert)
            c = list(output)
            return c


def main():
    dr = digitalRoot

    print(dr.digital_root(12))
    print("Hello world")


if __name__ == "__main__":
    main()
