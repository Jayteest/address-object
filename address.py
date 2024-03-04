# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 13, 2023

# Description:
# This file contains the Address class. Each instance of this class will
# have data attributes consisting of street number, street name, city, state,
# postal code, and optional apartment number.
# It contains methods for setting and getting each of these attributes.
# It contains a method for displaying the address, formatted with
# the street on one line, and the city, state, and postal code on another.
# It also contains a method to determine whether or not the postal code of
# the instance comes before the postal code of another instance of the class.
# Setters and getters have also been included, for the sake of thoroughness.

# Logic:
# class Address
# init:
#   set number, street, city, state, post to argument values
#   set apt to '' if no argument passed, otherwise set to argument value

# sets for number, street, city, state, post, apt:
#   accept argument value, set attribute to argument value

# gets for number, street, city, state, post, apt:
#   return attribute

# display_address:
#   if apt != '': apt = '#' + apt
#   print(f'{number} {street} {apt}\n{city}, {state} {post}')

# comes_before:
#   

# declare Address class
class Address:
    # constructor method to initialize object's data attributes
    # if apartment number is not passed, initialize to empty string
    def __init__(self, number, street, city, state, post, apt=''):
        # set each attribute to corresponding passed argument
        self.__number = number
        self.__street = street
        self.__city = city
        self.__state = state
        self.__post = post
        self.__apt = apt

    # set method to allow user to set street number
    def set_number(self, number):
        self.__number = number

    # set method to allow user to set street name
    def set_street(self, street):
        self.__street = street

    # set method to allow user to set city
    def set_city(self, city):
        self.__city = city

    # set method to allow user to set state
    def set_state(self, state):
        self.__state = state

    # set method to allow user to set postal code
    def set_post(self, post):
        self.__post = post

    # set method to allow user to set apartment number
    def set_apt(self, apt):
        self.__apt = apt

    # get method to return street number
    def get_number(self):
        return self.__number

    # get method to return street name
    def get_street(self):
        return self.__street

    # get method to return city
    def get_city(self):
        return self.__city

    # get method to return state
    def get_state(self):
        return self.__state

    # get method to return postal code
    def get_post(self):
        return self.__post

    # get method to return apartment number
    def get_apt(self):
        return self.__apt

    # method to display formatted address
    def display_address(self):
        # if an apartment number was provided...
        if self.__apt != '':
            # concatenate '#' to beginning for formatting
            self.__apt = '#' + self.__apt
        # print formatted address
        print(f'{self.__number} {self.__street} {self.__apt}\n{self.__city}, '
              f'{self.__state} {self.__post}')

    # method to determine if postal code of address comes before other address'
    def comes_before(self, other):
        # return True if postal code comes before that of other address
        return self.__post < other.__post
            
