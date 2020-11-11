import array
#Reverse Function------------------------------------
def rev_(y):
   New_arr_ = array.array('i', [])
   New_arr_2 = array.array('i', [])
   ind = 0 
   d = 0 
   print("Enter the number of left rotation: ")
   d=int(input(d))
   if 1<=d and d<=len(y):
       
        #rotated element being copied 
        while ind < d:
            val_ = y[ind]
            New_arr_.append(val_)
            ind +=1
        #Copy the not rotated elements to a new array 
        while ind<len(y):
            val3 = y[ind]
            New_arr_2.append(val3)
            ind +=1
        #appending the rotated elements at the end of the array 
        for x in range (0, len(New_arr_)):
                val4 = New_arr_[x]
                New_arr_2.append(val4)
        #print rotated array 
        print("The reversed array: ")
        for x in range (0, len(New_arr_2)):
            print (New_arr_2[x], end=" ")
   else: 
        print ("out of boundaries, try again ")
        main()
 
 #------------------------------------------------   
def main ():
    arr_ = array.array('i', []) #creating my array 
    z1 =0
    print("Please enter the number of integers: ")
    n1_ = int(input(z1))
    if 1 <=n1_ and n1_<=1000000:
        for x in range (0,n1_):
            x1 = x+1
            arr_.append(x1)
        print ("input array:")
        for w in range (0, len(arr_)):
            print ( arr_[w], end=" ")
        print ("\n")
        rev_(arr_) # Calling Function 
    else:
        print ("Out of range")

if __name__== "__main__":
    main()







