def valid_braces(string):
    otk = '([{'
    zakr = ')]}}'
    ar = {"(": ")", "[": "]", "{": "}"}
    ar_otk = []
    for i in string:
        if i in otk:
            ar_otk.append(i)
        elif i in zakr and len(ar_otk) == 0:
            return False
        elif i in zakr and i == ar[ar_otk[-1]]:
            ar_otk.pop()

    return not ar_otk
print(valid_braces("())({}}{()][]["))



