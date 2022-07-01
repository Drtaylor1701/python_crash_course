#!/usr/bin/env python3
'''
you can't change individual characters in a string because they are immutable

but you can make a new string based on the old one
'''
from xxlimited import new


message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

'''you can assign a new value to the same variable'''
message = "And another one"
print(message)

pets = "Cats & Dogs"
print(pets.index('&')) #figure out where the character is
print(pets.index("C"))
print(pets.index("Dog"))

print("Dragons" in pets)
print("Cats" in pets)

def replace_domain(email, old_domain, new_domain):
    '''replaces an old email domain with a new one'''
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("gillian@oldemail.com", "oldemail.com", "newemail.com"))
