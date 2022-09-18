def myfun(list):
    
    meanval = 0;
    even =0;
    maxnum = 0.0;
    evenlist = []
    floatlist = []
    
    for x in range(0,len(list),1): 
        
         if  isinstance(list[x], int):
            
     if list[x] % 2 == 0 :
     meanval = meanval + list[x]
     even = even +1
        evenlist.append(list[x])
        
        
        if  isinstance(list[x], float):
            
            if list[x] > maxFloat :
             maxnum = list[x]
              floatlist.append(list[x])
              
        
    
                
                
        
        
    meanval = meanval/even
    
    
    return print("List float is" ,floatlist), 
    print("List even is " ,evenlist),
    print("Float max number is ", maxnum),
    print("List mean is ", meanval)
  
    
