def isphonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if not text[i].isdecimal():
            if text[7] != '-':
                return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


if __name__ == '__main__':
    testNumber = '415-555-4242'
    print(testNumber + 'is phone number?')
    print(isphonenumber(testNumber))

    testNumber = 'test is good'
    print(testNumber + 'is phone number?')
    print(isphonenumber(testNumber))
