# #Day 1
# # print("Hello, World!")
# # print("123hello")


# # x= 10
# # y = "divya"
# # print(x)
# # print(y)


# # x = 34
# # y  = "radhika"
# # print(type(x))
# # print(type(y))  

# # x = y = z = "orange"
# # print(x)
# # print(y)
# # print(z)




# # a="ABC"
# # x ="A"
# # y = "B"
# # z = "C"

# # print(x)
# # print(y)
# # print(z)


# # Day 2

# #VARIABLE --Varibles are containers for storing data values.
# #A variable  name must start with a letter or the underscore character
# #A variable name cannot start with a number
# #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# #Variable names are case-sensitive (age, Age and AGE are three different variables) 
# #####THis means uppercase and lowercase letters are treated as different characters in variable names.
# # For example, "age" and "Age" would be considered two different variables in Python.
# # myvar = "John"
# # my_var = "John"
# # _my_var = "John"
# # myVar = "John"
# # MYVAR = "John"
# # myvar2 = "John"

# # #print()pretty flexible you can enter multiple value output separayted by spaces
# # print(34)
# # print("salman khan")
# # #print(salman khan )
# # print("divya",23,56,5)
# # print("divya",56,"radhika")


# # print("hello kha se ho ap",end =" ")
# # print("mai jaipur se hu")

# # print("hello",end = " -")
# # print("world")

# # print("hello");print("how are you");print("I am fine")


# # #dynamic typing == in python there is no fix datatype

# # a = 45
# # print(a)

# # a = "divya"
# # print(a)

# # a = int('5') #str->int
# # print(a)
# # print(type(a))  #casting --converting one data type to another data type

# # ##many value to many variables--python allows you to assign values to multiple variables  in one line
# # x,y,z = "apple","banana","cherry"
# # print(x)
# # print(y)
# # print(z)


# # x=y=z="orange"
# # print(x)
# # print(y)
# # print(z)

# # #unpack a collectoion -- if you have a collection of values in a list, tuple etc.
# # # Python allows you to extract the values into variables. This is called list  unpacking.
# # #list unpacking
# # a = ["divya","apple","juice"]
# # x,y,z = a
# # print(x)
# # print(y)
# # print(z)

# # #tuple unpacking
# # x = (3,4,5)
# # a,b,c = x
# # print(a,b,c)

# # #string unpacking
# # name ="ABC"
# # a,b,c = name
# # print(a,b,c)

# # x="python"
# # y= "is"
# # z="good"
# # print(x,y,z)
# # print(x+y+z)  #concatenation




# # ##casting-- if you want to specify a data type when creating a variable, this can be done with casting.
# # # Python has several built-in functions that can be used to cast values to a specific data type:
# # x = int(3)
# # y = float(3)
# # z = str(3)
# # print(x)
# # print(y)
# # print(z)
# # print(type(z))



# # #TYPE CONVERSION---you can convert from one data type to another data type using the built-in functions int(), float(), str() etc.
# # #1. implicit type conversion --internally data types
# # print(10 + 3.5) #int + float = float
# # print(type(10),type(3.5))

# # #2. explicit type conversion --programe req to change datatype
# # x= float(20)
# # print(x)
# # print(type(x))





# ##user input--
# #static VS dynamic software --static dont talk with user they only gives inforrmation(ex - calender clock)
# ##dynamic -- use input data hai(ex -- youtube,ola, zomato)
# #builde in function khate hai


# # a = input("what is your name:")
# # b = input("waht is your age: ")
# # print(a)
# # print(b)

# # a = int(input("enter a first number:"))
# # b = int(input("entert second number:"))

# # c = a+b
# # print(c)

# # name = input("apna naam bhatao: ")
# # print("hello",name)

# # a = int(input("enter a number:"))
# # b = int(input("enter a second number:"))

# # sum = a*b
# # print("total= ",sum)



# # #swap Two Numbers program

# # a = 20
# # b = 12
# # a,b = b,a
# # print("A:",a)
# # print("B:",b)

# # a= 20
# # b = 12
# # c= 38
# # a,b,c = c,b,a
# # print("A:",a)
# # print("B:",b)
# # print("C:",c)


# # #string rules- datatype h change or mutabel hoti h

# # # #1- sequence of characters written quotes.
# # # #2- strings are immutable /unchanged
# # ##3- include letter ,number,and spaces
# # ##4- but we can manipulate strings - usse like concentation ,slicing ,formating to create  new string 
# # ##5- delete an entries string varibles(python not paossible to deletes individuale characters )


# # a= 'hello'
# # print(a)

# # b= "python is good"
# # print(b)

# # c = '''hey how you
# # sb badiya
# # main think hu'''
# # print(c)



# #Day3 antigravity

# #data types in python  0 data types in python  are:
# #build in functions --int(), float(), str(), bool(), list(), tuple(), set(), dict() etc.
# #1. int --integer numbers
# #2. float --decimal numbers
# #3. str --string
# #4. bool --boolean values (True or False)
# #5. list --ordered collection of items
# #6. tuple --ordered collection of items (immutable)
# #7. set --unordered collection of unique items
# #8. dict --collection of key-value pairs
# #complex

# # name = "divya"
# # print("My Name is :-",name)
# # print("type of varible:",type(name))## type function type check karna ka kam karta hai

# # print("len of my string: - ",len(name)) ## len function string ki length check karne ka kam karta hai
# # name.upper() ## upper function string ko uppercase me convert karne ka kam karta hai
# # name.lower() ## lower function string ko lowercase me convert karne ka kam karta hai
# # name.capitalize() ## capitalize function string ke first character ko uppercase me convert karne ka kam karta hai aur baaki characters ko lowercase me convert karne ka kam karta hai
# #task 2
# # upper_name = name.upper()
# # print(upper_name)
# # lower_name = name.lower()
# # print(lower_name)


# #lw = upper_name.casefold() ## casefold function string ko lowercase me convert karne ka kam karta hai, lekin ye lower() se zyada aggressive hota hai, aur special characters ko bhi handle karta hai.
# #print(lw)   #task1

# # name = "divya"
# # print(name.title())
# # print(name.capitalize())



# #indexing and slicing
# # company_name = "upflair"
# # print(len(company_name))
# # print(company_name.strip())

# # # intro = "hello kase ho app"## task 3

# # company_name = "upflairs"
# # print(company_name[0]) ## indexing
# # print(company_name[1])
# # print(company_name[2])
# # print(company_name[3])
# # print(company_name[4])
# # print(company_name[5])
# # print(company_name[6])
# #print(company_name[7])
# #
# # print(company_name[-1]) ## negative indexing

# #print(company_name[0:4]) ## slicing
# #comapny_name>>task 4 reverse kase string mai 

# # name ="ritika"
# # last_name = "sharma"
# # print(name + " " + last_name) ##concatenation



# # #str*str
# # name = "dev"
# # print(name*name) ## repetition
# # print(name*3) ## repetition




# # """"paragraph likhna h """


# # task 5 dono comma mai kya difference hota h 

# # name = 'dev'
# # name = "dev"



# #intrio.strip()

# # name = "dev"
# # address = "jaipur"
# # print(f"my name is{name}and i from{address}") ## string formatting



# #input function
# # name = input("what is your name: ")
# # print(name)
# # print(type(name))


# # number1 =int(input("enter a first number: "))
# # number2 = int(input("enter a second number: "))
# # print(number1 + number2)
# # print(type(number1))
# # print(type(number2))

# ##input function by defult data type string hotdeta  hai, isliye agar aapko number ke roop me input lena hai to aapko usse int() ya float() me convert karna hoga.

# #day4



# #>>>>>>>>>>>>>>>>>>>>>>>>list<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #list is a collection which is ordered and changeable. Allows duplicate members.
# #list is defined by having values between square brackets [ ].
# #list is a collection which is ordered and changeable. Allows duplicate members.
# #list is defined by having values between square brackets [ ].
# #list is a collection which is ordered and changeable. Allows duplicate members.
# #list class hai 

# # lst = [1,2,3,4,5,"hello",3.2]
# # print("this is my first list: ",lst)
# # print("len of my list: ",len(lst))
# # print("type of my list: ",type(lst))


# # print=10
# # print(print)
# # lst=[1,2,3,4,5,"hello",3.2]
# # print(lst[0]) ## indexing
# # print(lst[1])
# # print(lst[2])
# # print(lst[3])
# # print(lst[4])
# # print(lst[5])
# # print(lst[6])


# # print(lst[-1]) ## negative indexing

# # print(lst[0:4]) ## slicing
# # print(lst[2:5])
# # print(lst[:4]) ## slicing from the beginning to index 4




# # #operations on list
# # fruits=['apple','banana','grapes','orange']
# # #add items
# # fruits.append('kiwi') ## append function list ke end me item add karne ka kam karta hai not return karna hai
# # print("fruits list: "fruits)



# # fruits=['apple','banana','grapes','orange']
# # #add items
# # fruits.insert(0,'kiwi') ## insert function list ke end me item add karne ka kam karta hai not return karna hai
# # print("fruits list: ",fruits)

# # fruits=['apple','banana','grapes','orange']
# # # #add items
# #  fruits.remove('kiwi') ## remove function list ke end me item add karne ka kam karta hai not return karna hai
# #  print("fruits list: ",fruits)



# #fruits=['apple','banana','grapes','orange']
# # #add items
# # fruits.pop(1) ## pop function list ke end me item add karne ka kam karta hai not return karna hai
# # fruits.clear()
# # fruits.copy()
# # print(fruits.count('apple')) ## count function list me item ke count karne ka kam karta hai

# # print(fruits.index('grapes')) ## index function list me item ke index number batane ka kam karta hai
# # fruits[0] = 'kiwi' ## list ke item ko change karne ka kam karta hai
# # fruits.reverse() ## reverse function list ke items ko reverse karne ka kam karta hai
# # print("fruits list: ",fruits)









# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(">>>>>",2 in lst1)


# print(lst1 + lst2) ## concatenation



# # function  use
# # len()    length of list
# # max()    maximum value in list
# # min()    minimum value in list
# # sum()    sum of all values in list
# # sorted() sorted version of list



#day4
#tuple is a collection which is ordered and unchangeable. Allows duplicate members.unmuthable
#tuple is defined by having values between parentheses ( ).
# tpl =(1,2,3,4,5,"hello",3.2,1.2)
# print("this is my first tuple: ",tpl)
# print("len of my tuple: ",len(tpl))
# print(tpl[0]) ## indexing
# print(tpl[1])
# print(tpl[2])
# print(tpl[3])
# print(tpl[4])
# print(tpl[5])
# print(tpl[6])
# print(tpl[7])
# print(tpl[-1]) ## negative indexing
# print(tpl[0:4]) ## slicing
# print(tpl[2:5])
# print(tpl[:4]) ## slicing from the beginning to index 


# a=1,23,5,6,5
# print(a)
# print(type(a))
# print(len(a))
#bydefault tuple ban jata hai jab aap comma se values ko separate karte hai, chahe aap 

#tuple unpacking
# a,b,c,=(1,3,2)
# print(a)
# print(b)
# print(c)



# a,b,c=(1,2,3)
# print(a)
# print(b)

# tpl =(1,2,3,"hello",3.2,1.2)
# print(tpl)
# print(tpl.count(3)) #count function tuple me item ke count karne ka kam karta hai
# print(tpl.index(2))## index function tuple me item ke index number batane ka kam karta hai
#count kina bare function repaetre hu hai 
#index function tuple me item ke index number batane ka kam karta hai


# tpl =(1,2,3,"hello",3.2,1.2)
# print("this is my tuple: ",tpl)
# print("type of my tuple: ",type(tpl))
# print("len of my tuple: ",len(tpl))
# print("tpl convert into list: ",list(tpl))
# lst = list(tpl)
# print("this is my list: ",lst)
# print("len of my list: ",len(lst))
# lst.append(4)
# print(lst)
# tpl= tuple(lst) ## tuple function list ko tuple me convert karne ka kam karta hai
# print(tpl)


#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.#denoted by dict,muthable
#dictionary is defined by having values between curly brackets { } and  key value pair

# student={"name":"John",
#          "class":"second year",
#           "roll number":23,
#           "branch":"computer science",
#           "Address":"Jaipur"}
 #name,class,rollnumber,branch,address>>>>keys
 #John,second year,23,computer science,jaipur>>>>values

# #key+value="Items"
# print(student)
# print("dict keys: ",student.keys())
# print("dict values: ",student.values())
# print("dict items: ",student.items())

# print(student['name'])
# print(student['class'])
# print(student['roll number'])
# print(student['branch'])
# print(student['Address'])




#add item in python dict
# student['subject']='python'
# print(student)

#task 1 upadate  function use karta dekhnana ,fromkeys ko use karara ka dekhna ha i 
# print(student.get('name')) 
# student.pop('roll number') ## pop function dict me item ko remove karne ka kam karta hai
# print(student)
# student.popitem() ## popitem function dict me last item ko remove karne ka kam karta hai
# print(student)
# # student.clear() ## clear function dict me sabhi items ko remove karne ka kam karta hai
# # print(student)
# student.copy() ## copy function dict me items ko copy karne ka kam karta hai
# print(student)
# student.update({'name':'divya'}) ## update function dict me items ko update karne ka kam karta hai
# print(student)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x = car.setdefault("color","red") ## setdefault function dict me item ko add karne ka kam karta hai, agar item already exist karta hai to usse return karta hai
# print(x)
#deep copy  task 2 cpmarsion b/w copy and deepcopy

# car={
#    "brand": "ford",
#    "model": "mustang",
#    "year": 1964
#  }
#print(car)
# car['year']=2020
# print(car)






# looping two type 
# for or while



# for x in car.keys(): ## keys function dict me keys ko return karne ka kam karta hai
#     for x in car.values(): ## values function dict me values ko return karne ka kam karta ha
#         for x in car.items(): ## items function dict me items ko return karne ka kam karta hai
# print(x) ## print keys





#set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. denoted by set
# set is defined by having values between curly brackets { } and separated by commas mutable,fastest data type
#  sat={1,2,3,4,5}
# print("this is first set: ",sat)
# print("type of my set: ",type(sat))
# print("len of my set: ",len(sat))
# #no indexing and slicing in set
# sat.add(6) ## add function set me item ko add karne ka kam karta hai
# print(sat)

# sat.discard(3) ## discard function set me item ko remove karne ka kam karta hai, agar item exist nahi karta hai to bhi error nahi deta hai
# print(sat)
# sat.pop()
# print(sat)
# sat.clear()
# print(sat)
# sat.copy() ## copy function set me items ko copy karne ka kam karta hai
# print(sat)
# sat.update({7,8,9}) ## update function set me items ko update karne ka kam karta hai
# print(sat)
#  sat.remove(7) ## remove function set me item ko remove karne ka kam karta hai, agar item exist nahi karta hai to error deta hai
#  print(sat)



#day 5










#operators in python
#1. arithmetic operators
#2. assignment operators
#3. comparison operators
#4. logical operators
#5. bitwise operators
#6. membership operators
#7. identity operators



