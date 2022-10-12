"""
commissioning form episodes 72-75
"""
# commissioning 1
def remove_chars(it):
    return it[1:len(it)-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list=map(remove_chars,friends_map)
for ob in cleaned_list:
    print(ob)
print("#"*100) 
for ob in map(lambda it:it[1:len(it)-1] ,friends_map):
    print(ob)   
# commissioning 2
from functools import reduce
def get_names(it):
        return str(it).endswith("m")
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names=filter(get_names,friends_filter)
for name in names:
    print(name)
print("#"*100)    
for name in filter(lambda it:str(it).endswith("m"),friends_filter):
    print(name)    
# commissioning 3
nums = [2, 4, 6, 2]
def dr(it):
    a=0
    sum=1
    for ob in it:
        sum*=ob
        a+=1
    return sum    
print(dr(nums))
print(reduce(lambda it,it2 :it*it2,nums))
# commissioning 4
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
a=50
loop=len(skills)-1
while loop>-1 :
    if type(skills[loop])==int:
         a+=1
         loop-=1
         continue
    print(f"{a}-{skills[loop]}")
    a+=1
    loop-=1
for count,ob in enumerate(reversed(skills),50):
    if type(ob)==int :
        continue
    print(f"{count} - {ob}")
