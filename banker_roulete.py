import random
names = input("Enter names separated by commas: ")
splitted_names = names.split(",")
list_of_names = splitted_names

number_of_items = (len(list_of_names))
random_choise = random.randint(0, number_of_items -1)
person_that_pays = list_of_names[random_choise]

print(f"Unfortunately {person_that_pays} pays the bill :( ")