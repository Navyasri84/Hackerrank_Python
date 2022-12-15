'''Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

'''............first way.........'''

# n=int(input())

# if(n%2!=0):
#     print("odd")
# elif(n%2==0 and 2<=n<=5):
#     print("even2-5")
# elif(n%2==0 and 6<=n<=20):
#     print("even6-20")
# elif(n%2==0 and n>20):
#     print("even>20")

'''............second way.........'''

#     n = int(input())
# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")            