# compare adjecents element in list
# check whether the list contains the same number in adjacent positions
# Display the count of such adjacent occurrences.

a= [1,0,0,20,40,40,1,1,9]
count =0
for x ,y in zip(a,a[1:]):
    if(x==y):
        count=count+1

print("same number in adjecent positions : ",count)