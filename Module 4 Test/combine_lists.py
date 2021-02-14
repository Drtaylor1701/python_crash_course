def combine_lists(list1, list2):
    Jamies_list.reverse()
    #print(Jamies_list)
    complete_list = Drews_list
    #print(complete_list)
    for item in Jamies_list:
        complete_list.append(item)
    return complete_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
