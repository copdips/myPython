def resolution(a,b,c):
    if not {type(i) for i in [a,b,c]} <= {int, float}:
        print("entrée de valeurs non correctes ")
        return None
    else:
        if a*b*c != 0:
            delta = b**2-4*a*c
            if delta<0:
                return [0,{}]
            elif delta == 0:
                return [1,{-b/(2*a)}]
            else:
                sqrt=delta**(0.5)
                return [2, {(-b-sqrt)/(2*a), (-b+sqrt)/(2*a)}]
        else:
            if {a,b,c} == {0.}:
                print('tout reel x est solution')
                return None
            elif b*c != 0:
                return [1,{-c/b}]
            elif a*b!=0:
                return [2,{0, -b/a}]
            else:
                if a == 0 :
                    return [0,{}]
                if a*c<0:
                    return [0,{}]
                else:
                    sqrt = (c/a)**(0.5)
                    if sqrt ==0:
                        return [1,{sqrt, -sqrt}]
                    else:
                        return [2,{sqrt, -sqrt}]
