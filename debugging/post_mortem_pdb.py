def add_one_hundred():
    again = 'yes'
    while again == 'yes':
        number = input('Enter a number between 1 and 10: ')
        new_number = (int(number) + 100)
        print('{} plus 100 is {}!'.format(number, new_number))
        again = input('Another round, my friend? ("yes" or "no") ')
    print("Goodbye!")
