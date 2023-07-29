def main():
    
    x = [2,3,6,1,7,8,5]

    x.sort()
    for i in range(len(x)):
        # print(x[i])
        # x = list(reversed(x))
        # print(x[i])
        x = x[::-1]
        print(x[i])


    
if __name__ == "__main__":
    main()