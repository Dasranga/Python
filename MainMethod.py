from pkg_resources import ensure_directory

print(__name__)


def main():
    print("Program starts")


def listComputations():
    a = [1, 2, 5, 6, 5, 78, 85, 2, 4, 8, 5, 77]
    print(a)
    print(a.__len__())
    print(a.pop(10))
    b = [1, 15, 16, 172]


def end():
    print("End Program")


# main()
# listComputations()
# end()

if __name__ == "__main__":
    print("Execute Actual Main")
    main()
    listComputations()
    end()
