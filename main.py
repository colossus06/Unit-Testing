def main():

    inp = input("What's x: ")

    print("x squared is ", square(inp))


def square(n):
    n = n * n
    return n


if __name__ == "__main__":
    main()
