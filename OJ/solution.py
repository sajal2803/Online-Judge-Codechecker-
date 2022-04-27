n=int(input())


a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
target= int(input())
target= int(target)
for i in range(len(a)):
    diff=target-a[i]
            
    if diff in a and i!= a.index(diff):
        print (i, a.index(diff))

          
                