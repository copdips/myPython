print("ok")


lambda fct : dict( (x,[k for k in range(len(L)) if L[k] == x]) for x in set(L) )
