BRAC = {
    "(": ")",
    "{": "}",
    "[": "]",
}


def check(string):
    stack = []
    for element in string:
        if element in BRAC:
            stack.append(element)
        else:
            if not stack:
                return False
            last = stack.pop()
            if element != BRAC[last]:
                return False

    return not stack


string = input()

print(check(string))
