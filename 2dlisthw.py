#hw done on 6.5.2024

#making a normal list

drinks = ["Water", "Lassi", "Coffee", "Coca Cola", "Water."]


#printing list

print(drinks)

#access data postive integers

print(drinks[2])

print(drinks[0])

#access data negative integers

print(drinks[-3])

print(drinks[-5])

#adding data using append

drinks.append("Chikoo Shake")

#checking added item

print(drinks)

#removing an item

drinks.remove("Water.")

#checking removed item

print(drinks)

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#creating a 2d list

matrix = [[111, 222, 333],
          [444, 555, 000],
          [777, 888, 999]]

#print matrix

print(matrix)

#number of items in a list

cat = len(matrix)

#printing cat

print(cat)

#printing a item in the list

print(matrix[2])

#printing a certain piece of data in the list that is in a list

print(matrix[0][2])

#using elements

pinpoint = matrix[2][0]

#checking the "using elements" section

print(pinpoint)

#nested loops

for meow in range(len(matrix)):
    for miau in range(len(matrix[1])):
        print(matrix[meow][miau], end = "")
    print()