# find volume of Sphere

def volume_of_sphere(r):
    return (4 * 22 * r ** 3) / (3 * 7)


print(volume_of_sphere(5))


# Check if a number is in Range

def number_in_range(num, a, b):
    return num in range(a, b)


print(number_in_range(32, 20, 30))


# find number of lower and upper characters in a string

def upper_lower_chars(str):
    d = {'upper': 0, 'lower': 0}
    for c in str:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass
    print(d['upper'])
    print(d['lower'])


upper_lower_chars("This is a brand new Pixel 5. What does the Hype Machine offer?")


# Return a unique List
def return_unique_list(lst):
    return list(dict.fromkeys(lst))


print(return_unique_list([1, 2, 44, 3, 55, 55, 55, 3, 2, 1]))


# Multiply all numbers in a list

def multiply_all_list_values(lst):
    out = 1
    for n in lst:
        out = out * n
    return out


print(multiply_all_list_values([1, 2, 3, -10]))


# Check if a string is palindrome or not

def palindrome_check(str):
    new_str = str[::-1]
    print(str.lower())
    return str.lower() == new_str.lower()


print("Palindrome?", palindrome_check("DDDAAADDD"))
