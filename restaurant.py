#Kevin Gemian
#CS 175L
#restaurant

vegetarian = str(input('Is anyone in your party vegetarian?(Yes or No): '))
vegan = str(input('Is anyone in your party vegan?(Yes or No): '))
glutenFree = str(input('Is anyone in your party gluten-free?(Yes or No): '))
vegetarian =  vegetarian.lower()
vegan = vegan.lower()
glutenFree = glutenFree.lower()
print ('Here are your restaurant choices:')
if vegetarian != 'yes' and vegan != 'yes' and glutenFree != 'yes':
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Cafè")
    print ("Mama's Fine Italian")
    print ("The Chef's Kitchen")
if vegetarian == 'yes' and vegan != 'yes' and glutenFree != 'yes':
    print ("Joe's Gourmet Burgers")
    print ("Main Street Pizza Company")
    print("Corner Cafè")
    print("The Chef's Kitchen")
if vegetarian != 'yes' and vegan != 'yes' and glutenFree == 'yes':
    print ("Main street Pizza Company")
    print ("Corner Cafè")
    print ("Chef's Kitchen")
if vegetarian == 'yes' and vegan != 'yes' and glutenFree == 'yes':
    print ("Main street Pizza Company")
    print ("Corner Cafè")
    print ("Chef's Kitchen")
if vegetarian != 'yes' and vegan == 'yes' and glutenFree != 'yes':
    print ("Corner Cafè")
    print ("Chef's Kitchen")
if vegetarian != 'yes' and vegan == 'yes' and glutenFree == 'yes':
    print ("Corner Cafè")
    print ("Chef's Kitchen")
if vegetarian == 'yes' and vegan == 'yes' and glutenFree != 'yes':
    print ("Corner Cafè")
    print ("Chef's Kitchen")
if vegetarian == 'yes' and vegan == 'yes' and glutenFree == 'yes':
    print ("Corner Cafè")
    print ("Chef's Kitchen")