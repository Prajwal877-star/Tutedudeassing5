try:
 dictionary = {'Alice':85,'Peter':96,'Nick':78,'Mike':92}
 key = input("Enter the student's name:")
 answer = dictionary[key]
 print("{}'s marks:".format(key),answer)
except KeyError:
    print('Student not found')