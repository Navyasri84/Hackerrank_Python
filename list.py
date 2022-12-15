n=int(input())
a=[]

for i in range(0,n):
        p=input().split();
        if p[0] == "insert":
            a.insert(int(p[1]),int(p[2]))
        elif p[0] == "append":
            a.append(int(p[1]))
        elif p[0] == "pop":
            a.pop();
        elif p[0] == "print":
            print(a)
        elif p[0] == "remove":
            a.remove(int(p[1]))
        elif p[0] == "sort":
            a.sort();
        else:
            a.reverse();