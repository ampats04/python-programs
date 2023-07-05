class Tribonnaci:
    def tribonnaci(signature, n):
        if n == 0:
            return []
        elif n <= 3:
            return signature[:n]

        result = signature[:]

        for i in range(3, n):
            next_number = sum(result[-3])
            result.append(next_number)


def main():
    tr = Tribonnaci

    tr.tribonnaci([1, 1, 1], 10)


if __name__ == "__main__":
    main()
