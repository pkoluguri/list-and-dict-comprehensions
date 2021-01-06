#creating an nums and heros list with the names and the hero they played
#our task is to make an dict with combination of the name and hero they played
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#creating the dictionary
my_dict = {}
#using the zip function to add the elements of the name and hero and taking the name and hero
for name ,hero in zip(names,heros):
  #and assigning the name to the hero they played in the dictionary
  my_dict[name] = hero
print(my_dict)
#doing the same thing but in dict-comprehension
my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)
#doing the same thing but we are aviding the name peter which in turn avoids spiderman we can avoid any other name too
my_dict = {name:hero for name,hero in zip(names,heros) if name != "Peter"}
print(my_dict)