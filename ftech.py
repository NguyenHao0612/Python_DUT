A = input("Nhap chuoi : ")
A = list(A)

for i in range (0,len(A)):
    a = A.count(A[i])
    
    print(A[i],a,i)
print(A)