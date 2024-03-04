# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 13, 2023

# Description:
# This program prompts the user to enter the address information for 2 different
# addresses, including street number, street name, optional apartment number,
# city, state, and postal code. It allows for US and Canadian postal codes.
# It then displays both addresses, formatted with the street on one line and the
# city, state, and postal code on the next line.
# Finally, it compares the postal codes of both addresses and tells the user
# address which comes first. 

# Logic:
# import address
# main:
#   address1 = create_address
#   address2 = create_address
#   display address1
#   display address2
#   if address1 comes_before address2: display message
#   if address2 comes_before address1: display message
#   else: display message that neither comes before other

# create_address:
#   number = prompt for string street number, strip()
#   street = prompt for string street name, strip()
#   apt = prompt for string apt number or enter to skip, strip()
#   city = prompt for string city, strip()
#   state = prompt for string state, strip()
#   while loop:
#       postal = prompt for string postal, strip()
#       if len is 5:
#           check if all digits, if so break from loop
#           else: display error; continue
#       if len is 7:
#           check if indices 0, 2, 5 are alpha
#           and indices 1, 4, 6 are digit and index 3 is ''
#           if true, postal = indices 1 + 4 + 6 + '00'; break from loop
#           else: display error; continue
#       else: display error; continue
#   create address with input
#   return address


# import address.py to use Address class
import address

# create main function to begin program execution
def main():
    # display header for user to input first address info
    print(f'Address 1 -')
    # call function to get address info from user
    address1 = create_address()

    # display header for user to input second address info
    print(f'\nAddress 2 -')
    # call function to get address info from user
    address2 = create_address()

    # display first address output header
    print(f'\n_____Address 1_____')
    # call method to display formatted first address
    address1.display_address()

    # display second address output header
    print(f'\n_____Address 2_____')
    # call method to display formatted second address
    address2.display_address()

    # display postal code comparation header
    print(f'\nCompared by Postal Code...')

    # use method to check if address 1's postal code comes before address 2's
    if address1.comes_before(address2):
        # if it does, display result
        print(f'Address 1 comes before Address 2')
    # use method to check if address 2's postal code comes before address 1's
    elif address2.comes_before(address1):
        # if it does, display result
        print(f'Address 2 comes before Address 1')
    # otherwise, they must be equal. Display result
    else:
        print(f'Neither address comes before the other.')
    
# function to prompt user to enter information for address
# allows user to opt out of an apartment number
# converts Canadian postal codes to US format
# creates and returns Address object with entered attributes
def create_address():
    # prompt user for street number, strip leading and trailing whitespace
    number = str(input(f'Enter the street number: ')).strip()
    # prompt user for street name, strip leading and trailing whitespace
    street = str(input(f'Enter the street name: ')).strip()
    # prompt user for apartment number, or allow them to press enter to skip
    apt = str(input(f'Enter the apartment number, or press ENTER if none: ')).strip()
    # prompt user for city, strip leading and trailing whitespace
    city = str(input(f'Enter the city: ')).strip()
    # prompt user for state, strip leading and trailing whitespace
    state = str(input(f'Enter the state: ')).strip()

    # while loop to validate postal code input
    while True:
        # prompt user for postal code, strip leading and trailing whitespace
        post = str(input(f'Enter the postal code (5-digit US, XXX XXX Canada): ')).strip()

        # if input is 5 characters...
        if len(post) == 5:
            # check if they are all numeric
            if post.isdigit():
                # if so, input is good, break from loop
                break
            # if characters are not all numeric...
            else:
                # input is not good, display error message
                print(f'Invalid zip code entered. Please try again.')
                # begin next iteration of loop to try again
                continue
        # if input is 7 characters...
        elif len(post) == 7:
            # check that they are in Canadian format (ex. A1A 1A1)
            if post[0].isalpha() and post[1].isdigit() and \
            post[2].isalpha() and post[3] == ' ' and post[4].isdigit() \
            and post[5].isalpha() and post[6].isdigit():
                # convert to US equivalent, which is the 3 numbers with trailing '00'
                post = post[1] + post[4] + v[6] + '00'
                # break from loop
                break
            # if not Canadian format...
            else:
                # input is not good, display error message
                print(f'Invalid zip code entered. Please try again.')
                # begin next iteration of loop to try again
                continue
        # if input is not 5 or 7 characters...
        else:
                # input is not good, display error message
                print(f'Invalid zip code entered. Please try again.')
                # begin next iteration of loop to try again
                continue

    # create Address object using provided data attributes
    entry = address.Address(number, street, city, state, post, apt)
    # return Address object
    return entry

# call main to execute program
if __name__ == '__main__':
    main()
        
    
                
