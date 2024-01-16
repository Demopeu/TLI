from sys import stdin
Num = int(stdin.readline())
List = list(map(int,stdin.readline().split()))
List.sort(reverse = True)
max = List[0]
NewList = []
for i in range(Num):
    New_ = (List[i]/max)*100
    NewList.append(New_)
A = sum(NewList)/len(NewList)
print(A)