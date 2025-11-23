# ask the user for words to build a game scene
location = input("Name a place on an island (forest, dock, cliff): ")
creature = input("Name a creature (shrimp, crow, orca): ")
object_found = input("Name an object you might find outside: ")
adjective = input("Enter an adjective: ")

# print the sentence using an f-string
print(f"While walking near the {location}, you see a {adjective} {creature} "
      f"holding a {object_found}. What does it want?")