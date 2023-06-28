#Program to count odd and even
# By taking inputs from users
a=[1,2,3,4,5,6,7,8,9]
length=len(a)
even=0
odd=0
for i in range(length):
    if(a[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("No of even numbers :",even,"\n","No of odd numbers is :", odd)                