x = 0
y = 0
z = 0
w = 0 

def print_registers() :
    print('x = ' , x, 'y = ' , y, 'z = ' , z, 'w = ' , w)

def eql( x, w ) :
    if x == w : return 1
    return 0

def step1(n) : # Inc Z = w + 16
    global w, x, y, z
    w = n
    x = 1
    y = w + 16
    z = y

def step2(n) : # Inc z = z * 26 + w + 11
    global w, x, y, z
    w = n
    x=1
    y=26
    z=z*y
    y=w+11
    y=y*x
    z=z+y

def step3(n) :  # Inc z = z * 26 + w + 12
    global w, x, y, z
    w = n
    x = 1
    y = 26  
    z = z * y
    y = w + 12
    z = z + y

def step4(n) :  # Dec z = z // 26 ; w skall vara z % 26 -5
    global w, x, y, z
    w = n
    x = z % 26 -5 
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = ( w + 12 ) * x
    z = z + y

def step5(n) :  # Dec z = z // 26 ; w skall vara z % 26 -3
    global w, x, y, z
    w = n
    x = z % 26 - 3
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = ( w + 12 ) * x
    z = z + y

def step6(n) :  # Inc z = z * 26 + w + 2
    global w, x, y, z
    w = n
    x = z % 26 + 14
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 2) * x
    z = z + y

def step7(n) : # Inc z = z * 26 + w + 11
    global w, x, y, z
    w = n
    x = z % 26 + 15
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 11) * x
    z = z + y

def step8(n) : # Dec z = z // 26 ; w skall vara z % 26 -16
    global w, x, y, z
    w = n
    x = z % 26 - 16
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 4) * x
    z = z + y

def step9(n) : # Inc z = z * 26 + w + 12
    global w, x, y, z
    w = n
    x = z % 26 + 14
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 12) * x
    z = z + y

def step10(n) : # Inc z = z * 26 + w + 9
    global w, x, y, z
    w = n
    x = z % 26 + 15
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 9) * x
    z = z + y

def step11(n) : # Dec z = z // 26 ; w skall vara z % 26 -7
    global w, x, y, z
    w = n
    x = z % 26 -7
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 10) * x
    z = z + y

def step12(n) : # Dec z = z // 26 ; w skall vara z % 26 -11
    global w, x, y, z
    w = n
    x = z % 26 - 11
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 11) * x
    z = z + y

def step13(n) : # Dec z = z // 26 ; w skall vara z % 26 -6
    global w, x, y, z
    w = n
    x = z % 26 - 6
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 6) * x
    z = z + y

def step14(n) : # Dec Z = 0 om n= 1..9 och z = 11 + n ; z = z // 26 ; w skall vara z % 26 -11
    global w, x, y, z
    w = n
    x = z % 26 - 11
    z = z // 26
    x = eql(x, w)
    x = eql(x, 0)
    y = 25 * x + 1
    z = z * y
    y = (w + 15) * x
    z = z + y


def find_large() : 
    global z
    for n1 in range(9,0,-1) : 
        z = 0
        step1(n1)
        z1 = z
        for n2 in range(9,0,-1) :
            z = z1
            step2(n2)
            z2 = z
            for n3 in range(9,0,-1) :
                z = z2
                step3(n3)
                n4 = z % 26 -5
                if ( n4 > 9 or n4 < 1  ) : continue
                step4( n4)
                n5 = z % 26 -3
                if ( n5 > 9 or n5 < 1 ) : continue
                step5(n5)
                z5 = z
                for n6 in range(9,0,-1) :
                    z = z5
                    step6(n6)
                    z6 = z
                    for n7 in range(9,0,-1) :
                        z = z6
                        step7(n7)
                        n8 = z % 26 -16
                        if ( n8 > 9 or n8 < 1  ) : continue
                        step8(n8)
                        z8 = z
                        for n9 in range(9,0,-1) :
                            z = z8
                            step9(n9)
                            z9 = z
                            for n10 in range(9,0,-1) :
                                z = z9
                                step10(n10)
                                n11 = z % 26 - 7
                                if ( n11 > 9 or n11 < 1  ) : continue
                                step11(n11)
                                n12 = z % 26 - 11
                                if ( n12 > 9 or n12 < 1  ) : continue
                                step12(n12)
                                n13 = z % 26 - 6
                                if ( n13 > 9 or n13 < 1  ) : continue
                                step13(n13)
                                n14 = z % 26 - 11
                                if ( n14 > 9 or n14 < 1  ) : continue
                                step14(n14)
                                if z == 0 : 
                                    # Valid number
                                    print( 'Number is : ',n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14)
                                    return

def find_small() : 
    global z
    for n1 in range(1,10) : 
        z = 0
        step1(n1)
        z1 = z
        for n2 in range(1,10) :
            z = z1
            step2(n2)
            z2 = z
            for n3 in range(1,10) :
                z = z2
                step3(n3)
                n4 = z % 26 -5
                if ( n4 > 9 or n4 < 1  ) : continue
                step4( n4)
                n5 = z % 26 -3
                if ( n5 > 9 or n5 < 1 ) : continue
                step5(n5)
                z5 = z
                for n6 in range(1,10) :
                    z = z5
                    step6(n6)
                    z6 = z
                    for n7 in range(1,10) :
                        z = z6
                        step7(n7)
                        n8 = z % 26 -16
                        if ( n8 > 9 or n8 < 1  ) : continue
                        step8(n8)
                        z8 = z
                        for n9 in range(1,10) :
                            z = z8
                            step9(n9)
                            z9 = z
                            for n10 in range(1,10) :
                                z = z9
                                step10(n10)
                                n11 = z % 26 - 7
                                if ( n11 > 9 or n11 < 1  ) : continue
                                step11(n11)
                                n12 = z % 26 - 11
                                if ( n12 > 9 or n12 < 1  ) : continue
                                step12(n12)
                                n13 = z % 26 - 6
                                if ( n13 > 9 or n13 < 1  ) : continue
                                step13(n13)
                                n14 = z % 26 - 11
                                if ( n14 > 9 or n14 < 1  ) : continue
                                step14(n14)
                                if z == 0 : 
                                    # Valid number
                                    print( 'Number is : ',n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14)
                                    exit()



find_large()                           
find_small()