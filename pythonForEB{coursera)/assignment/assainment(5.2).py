largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break 
     
#to check if its a number or not    
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    
    
     #for largest number      
    for the_num in [num]:
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
           
    #for smallest number
    for the_num in [num]:
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = the_num
            
        
    
    
    
print("Maximum is", largest)
print("Minimum is", smallest)