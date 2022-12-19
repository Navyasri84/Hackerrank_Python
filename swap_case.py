def swap_case(s):
    name = ""
    for let in s:
        if let.isupper() == True:
            name+=(let.lower())
        else:
            name+=(let.upper())
    return name

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)