# List : It is used to store multiple variables in a single variable.List is mutable.
# Mutable: Mutable means we can modify the data
# List operations:
# Manipulating elements: 
# Append: to add element at the last position
# insert: to insert element at the specific index
# extend: to add elements from one list to another list
# remove: to remove specific element from the list
# pop: it returns the last element from the list
# ordering elements:
# reverse: to reverse the string
# sort : order the elements from ascending order to descending order
# len : it returns the length of the list
# index : it returns the index of elements
# min: it returns the minimum valkue from the list
# max : it returns the maximum value from the list
# mathematical operations :
# concatentation: two add two strings
# repetitrion : it repets the string
# comparing operator : compare two lists
#Example for list operations:
a=[1,2,3,4,5,6,7,8]
print(type(a))
print(a[0])
print(a[-1])
a[5]=60
print(a)
print("----------------------------")
for i in a:
    print(i)
print("------------------")
i=0
while i<len(a):
    print(a[i])
    i=i+1
print("append function")
a.append(70)
print(a)
print("insert function")
a.insert(0,90)
print(a)
print("extend function")
b=[30,40,50]
a.extend(b)
print(b)
print("remove function")
a.remove(8)
print("pop function")
print(a.pop())
print("reverse function")
a.reverse()
print(a)
print("sort function")
print(a.sort())
print(a)
print("concatenation function")
c=a+b
print(c)
print("repetition function")
d=a*3
print(d)
print("clear function")
print(a.clear())
print("list comprehension")
s=[x for x in range(1,11)]
print(s)

print("--------------------------")
print("tuple operations")
#tuple:to store mutiple values in a single varaiable. list is immutable.
#immutable: we cannnot modify the data
#Len: to return the length of elements from the tuple
#count: to return the number of occurance of the given element
#max:it returns the largest element from the tuple
#min:it returns the smallest element from the tuple
#sorted:to sort the elements that is asscending order from the tuple

#examples
l=(100,200,300,400,800,600,700,960,340)
print(type(l))
print("len function")
print(len(l))
print("count function")
print(l.count(400))
print("index function")
print(l.index(300))
print("max function")
print(max(l))
print("min function")
print(min(l))
print("sorted function")
l1=sorted(l)
print(l1)

print("--------------------------")
print("set operations")
# set:set is unordered collection and set contaions no duplicate element.set is mutable.
# set functions
#Add: to add the element to the  set
#update : to update the multiple elements to the set
#clear:removes all the elements from the set
#copy: returns the elments from the set
#pop: removes the random element from the set
#remove: it removes the specific element from the set
#discard : it also removes the specific element from the set
print("some mathematical operations for set")
#union:combine two sets
#intersection:returns the element opresent in both sets
#difference: returnbs the elements  present in one set not in two sets
#symmetric difference : returns the elements present in either set1 or set2 not in both sets
#examples
#empty 
n=set()
print(type(n))
m={4,2,8,1,9,6}
print(type(m))
print("add function")
print(m.add(10))
print("update function")
r={20,40,25,10,6}
m.update(r,range(5))
print(m)
print("copy function")
x=m.copy()
print(x)
print("pop function")
print(m.pop())
print("remove function")
print(m.remove(6))
print(m)
print("discard function")
print(m.discard(20))
print("clear function")
print(m.clear())
print("union function")
print(m.union(r))
print(m|r)
print("intersection function")
print(m.intersection(r))
print(m&r)
print("difference function")
print(m.difference(r))
print(m-r)
print("symmetric difference function")
print(m.symmetric_difference(r))
print(m^r)
print("set comprehension")
t={v*v for v in range(5)}
print(t)

print("--------------------------")
print("dictionary ")
#dictionary: it contains both keys and values keys are unique but values are different.dict is mutable.
#dictiuonary operations:
#len: it returns the length of the dictionary
#clear: it remove all the elemnts from he dictionary
#get : to get the value associated with key
#pop : it removes the specific key and returns the corresponding value 
#pop items: it removes the keys and values from the dictionary
# keys: it returns all the keys associated with dict
#copy: to create exactly duplicate dict
# items :it returns the list of tuples representing key-value pairs
# examples
m1={1:"madhu",2:"gopi",3:"sai"}
print(type(m1))
print("update dictionary")
m1[4]="bhavani"
print(m1)
print("delete function")
del m1[3]
print(m1)
print("len function")
print(len(m1))

print(m1)
print("pop items function")
print(m1.popitem())
print(m1)
print("keys function")
print(m1.keys())
print(m1)
print("clear function")
m1.clear()
print("dictionatry comprehension")
squares={y:y*y for y in range(1,6)}
print(squares)









