def email_list(domains):
    emails = []
    addresses = domains.keys()
    #print(domains)
    for address in addresses:
        #print(address)
        #print(domains.values())
        user_list = domains.values()
        #print(user_list)
        #print(domains[address])
        #users = domains[addresses]
        for users in user_list:
            #print(users)
            for user in users:
                #print(user)
                email = user + "@" + address
                emails.append(email)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))