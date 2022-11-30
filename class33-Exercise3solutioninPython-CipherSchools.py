name, char = input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)} ")
print(f"character count : {name.strip().lower().count(char.strip().lower())} ") # case sensitive
# PRANJAL - pranjal
# A - a
# "  Pranjal  " --> "Pranjal" --> "pranjal"
# "  A " --> "A" --> "a"
name.strip().lower().count(char.strip().lower())
# char.strip().lower()