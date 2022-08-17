#set

marks ={12,14,16,18,16,16}
print(marks) 
#output will be 16,18,12,14 and 16 will be not be printed 3 times as set contains only unique values 
# print(marks[0]) --> This opeartion will not work as set do not have index
#we can iterate set using loop
for score in marks:
    print(score)

print("         **********************************************")    

#Dictionary

marks = {"English":95, "Physics" : 99 , "Chemistry": 80}

print(marks["Chemistry"])
marks["Math"] =96;
print(marks)