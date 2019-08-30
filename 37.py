list=[1,2,3,4,5]
flag=0

for i in list:
    print("current element:",i,end="\n");
    if i==3:
        pass;
        print("\n Came out of pass\n");
        flag=1;
    if flag==1:
        print("\nCame out of pass\n");
        flag=0;

    

