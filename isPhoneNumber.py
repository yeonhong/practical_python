import re

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
    phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search('my dd is (432) 455-2333')
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(0))

    areaCode, mainNumber = mo.groups()
    print(areaCode)
    print(mainNumber)

    print('? operation----------')
    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo = phoneRegex.search(('My number is 334-234-5233'))
    print(mo.group())
    mo = phoneRegex.search(('My number is 234-5233'))
    print(mo.group())

    batRegex = re.compile(r'Bat(wo)?man')
    mo = batRegex.search('The Story of Batman')
    print(mo.group())
    mo = batRegex.search('The Story of Batwoman')
    print(mo.group())

    print('| operation----------')
    heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo1 = heroRegex.search('Batman and Tina Fey.')
    print(mo1.group())

    mo = heroRegex.search('Batmobile lost a wheel')
    print(mo.group())
    print(mo.group(1))




