def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  for key in guests2:
    #print(key)
    if key in guests1:
      print(key)
      Rorys_number = int(guests1.get(key))
      print(Rorys_number)
      Taylors_number = int(guests2.get(key))
      print(Taylors_number)
      update_number = Rorys_number + Taylors_number
      print(update_number)
      guests2.update({key: update_number})
  return guests2
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))