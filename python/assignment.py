# # #1
# # a = int(input("enter a prime number:"))
# # if a%2==0:
# #     print(" not a prime number")
# # else:
# #     print(" prime number ")





# # #2
# # a=[2,5,7]
# # b =[4,8,9]
# # print(a==b)
# # #2.1
# # a=[2,5,7]
# # b =[2,5,7]
# # print(a==b)

# # #2.2
# # a=[2,5,6]
# # b =[2,5,7]
# # print(a is b)

# # #2.3
# # a=[2,5,6]
# # b =[2,5,6]
# # print(a is b)




# # #4



# # #5
# # def find_values(list):
# #     largest = list[0]
# #     smallest = list[0]
# #     for i in list:
# #         if i > largest:
# #             largest = i
# #         if  i < smallest:
# #             smallest = i
# #     return largest, smallest
# # #example list
# # examplelist = [3, 5, 1, 9, 2]
# # large, small = find_values(examplelist)

# # print("Largest value:", large)
# # print("Smallest value:", small)



# # #3

# # data = [5, -2, ”abc”, 7, 0 ,9,] 
# # for i in data: 
# # try : 
# # if not isinstance (i, int): 
# # raise ValueError(“Non-interger Value”) 
# # if i == 0: 
# # print(“Zero found. Stopping …”) 
# # break  
# # if i  == 0: 
# # continue
# # print(i) 

# # except ValueError as e : 
# # print(e)






# #assignment 2

# # #1

# # name = "sharaddha"
# # city = "jaipur"
# # course = "Data Science"
# # print(f"my name is {name} and i am from {city} and i am learning {course}") ## string formatting






# #2

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello", name + ", you are", age, "years old")

# #3
# text = input("Enter a string: ")

# # Reverse string
# reverse_text = text[::-1]

# # Count characters
# count = len(text)

# print("Reverse string is:", reverse_text)
# print("Total characters are:", count)

#ASSIGNMENT 3
#1

# name = "shraddha"
# age = 20
# height = 5.6
# is_student = True

# print("name: ",name)
# print("age: ", age)
# print("Height:", height)
# print("Student:", is_student)

# # #2

# text = "Hello Python"
# print("Original String:", text)
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())
# print("Length of String:", len(text))


# #3
# numbers = [10, 20, 30, 40, 50]

# print("First element:", numbers[0])
# print("Second element:", numbers[1])
# print("Third element:", numbers[2])
# print("Fourth element:", numbers[3])
# print("Fifth element:", numbers[4])

# #4
# str1 = "Hello"
# str2 = "Python"

# result = str1 + " " + str2
# print("Concatenated String:", result)

# #5

# # Creating a list of student names

# students = ["Aman", "Rahul", "Priya"]

# students.append("Mansi")

# print("Updated Student List:", students)







#Assignment 4

#4
#list operations
# lst=[1,2,3,4,5]
# print(lst)
# lst.append(6)
# print(lst)
# lst.remove(2)
# print(lst[0:4])

# #tuple indexing
# tup=(10,20,30,40,50)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])

# #set operations
# sat={1,2,3,4,5}
# print(sat)
# sat.union({6,7})
# print(sat)
# sat.intersection({2,3,4})
# print(sat)

# #dictionary keys
# student={"name":"Aman","age":20,"course":"Data Science"}
# print(student["name"])
# print(student["age"])
# print(student["course"])
# student.keys()
# print(student.keys())
# student.values()
# print(student.values())
# student.items()
# print(student.items())




#5
#min student management system
# student={
#     "name": "Shraddha",
#     "roll_no": 101,
#     "course": "B.Tech CSE"
# }
# #store marks using list
# student["marks"] = [85, 90, 78]
# #calculate average marks
# total=sum(student["marks"])
# #calculate average
# average=total/len(student["marks"])
# print("Student Name:", student["name"])
# print("Roll No:", student["roll_no"])
# print("Course:", student["course"])
# print("Marks:", student["marks"])
# print("Average Marks:", average)




#3
# mutable data type
#list is mutable data type
# lst=[10,20,30]
# print(lst)

# #string are immutable
# name = "Python"

# # name[0] = "J"   ❌ Error

# new_name = "J" + name[1:]

# print(new_name)



#2
# Integer
# a = 10

# # Float
# b = 25.5

# # String
# c = "Shraddha"

# # Boolean
# d = True

# # List
# e = [1, 2, 3]

# # Tuple
# f = (10, 20)

# # Set
# g = {1, 2, 3}

# # Dictionary
# h = {
#     "name": "Shraddha",
#     "course": "CSE"
# }

# # Printing values
# print("Values:")
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

# # Printing data types
# print("\nData Types:")
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))






#1
# python data type in detail
#integer
age = 20
roll_no = 101

print(age)
print(roll_no)
#float
price = 99.99
temperature = 36.5

print(price)
print(temperature)
#string
name = "Shraddha"
city = 'Jaipur'

print(name)
print(city)
#boolean
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
#list
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
#tuple
colors = ("red", "green", "blue")

print(colors)
print(colors[1])
#set
numbers = {1, 2, 3, 2, 1}

print(numbers)
#dict
student = {
    "name": "Shraddha",
    "age": 20,
    "course": "CSE"
}

print(student)
print(student["name"])







