# Return Even Numbers

def myfunc(*args):
    return [n for n in args if n % 2 == 0]


print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9))


# Alternate Letters as Caps/Small

def myfunc1(str):
    a = True
    out = ''
    for alphabet in str:
        out += alphabet.lower() if a else alphabet.upper()
        if alphabet.isalpha():
            a = not a
    return out


print(myfunc1("Dasara3thy has 2 cATS"))

# try int vs String

val = "a2"
print(val.upper())


# to check if both numbers are even - return least among them. Else if one/more is odd, return biggest number among them.
def ret_big_number(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(ret_big_number(21112222, 20001))


# To Check for the first character in the 2-word string
def animal_crackers(str):
    print(str.upper().split(" ")[0][0])
    print(str.upper().split(" ")[1][0])
    result = str.upper().split(" ")[0][0] == str.upper().split(" ")[1][0]
    return result


print(animal_crackers("Das dataScientist"))


def find_20(a, b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False


print("Find_20 Function")
print(find_20(2, 19))


# reverse statement

def reverse_statement(statement):
    return ' '.join(statement.split(" ")[::-1])


print(reverse_statement('I am Home'))


# Number 10 within 100 or 200

def find_10(integer):
    if (integer >= 100 and integer <= 110) or (integer >= 200 and integer <= 210):
        return True
    else:
        return False


print("Find 10")
print(find_10(199))
