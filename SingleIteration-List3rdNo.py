def large3():
    l = []
    for i in range(8):
        num = int(input("\nEnter number: "))
        l.append(num)
    m1 = l[0]
    m2 = l[1]
    m3 = l[2]
    
    for e in l:
        if e>m1:
            m3 = m2
            m2 = m1
            m1 = e
            
        elif e>m2:
            m3 = m2
            m2 = e
        elif e>m3:
            m3 = e
        
        else:
            
            pass
    print("\nRight! 3rd Largest Number is: ",m3)
#main environment
large3()