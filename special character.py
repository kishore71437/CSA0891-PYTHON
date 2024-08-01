statement="modi birthday @ september17,#&$%"
special_character_count=0
for char in statement:
    if not char.isalnum() and not char.isspace():
        special_character_count +=1
print("Number of special characters found:",special_character_count)

 

