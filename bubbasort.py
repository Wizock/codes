def sort(n):

    arra = []
    for i in range(n):
        x = input("enter 5 numbers  ")
        arra += x
        
     
    for k in range(6):
        for j in range(1,5):
            if arra[j] > arra[j+1]:
                temp = arra[j]
                arra[j+1] = arra[j]
                arra[j+1] = temp
    print(str(arra))
            
sort(5)
