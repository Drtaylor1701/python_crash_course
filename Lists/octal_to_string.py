'''The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
For example: 
640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
Fill in the blanks to make the code convert a permission in octal format into a string format.
'''

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for num in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        #print(num)
        if num == 7:
            result = result + "rwx"
        elif num == 6:
            result = result + "rw-"
        elif num == 5:
            result = result + "-xr"
        elif num == 4:
            result = result + "r--"
        elif num == 3:
            result = result = "-wx"
        elif num == 2:
            result = result = "-w-"
        elif num == 1:
            result = result = "--x"
        else:
            result = result + "---"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------