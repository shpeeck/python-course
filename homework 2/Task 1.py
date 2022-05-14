# Task 1
school = {"1а" : 30, "1б" : 28, "2б" : 33, "6а" : 27, "7в" : 31}

#a
school["1а"] = 25
#b
school["5а"] = 20
#c
del school["1а"]
# a1 = school.pop("1а")

#summ all people
print(sum(school.values()))
print(school)

#reverse dict function
def reverse(dic):
    new_dict = {}
    for i in dic:
        new_dict[dic[i]] = i
    return new_dict

dk = {"first" : 1, "second" : 2}

print(dk)
new = reverse(dk)
print(new)