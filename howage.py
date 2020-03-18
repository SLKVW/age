print('hello my frind')

import datetime
def main():
    Age = input('Date of birth:')
    yearnow=datetime.datetime.now().year
    Myage= yearnow-int(Age)
    print('Your age now {}'.format(Myage))
main()