def main():
    
    # Prints 5 indices
    x = list(range(5))
    print(x)

    # list(range(start,end))
    # Print starts in 1 and ends with 4
    y = list(range(1,5))
    print(y)

    # list(range(start,end,step))
    # Print starts in 1 and have an interval of 2 excluding 10
    z = list(range(1,10,2))
    print(z)

if __name__ == "__main__":
    main()