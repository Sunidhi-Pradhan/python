n = 451
dem = [500,200,100,50,20,10,1]
for i in dem:
    count =  n//i
    if count != 0:
        print(f"{i} : {count}")
    n=n%i