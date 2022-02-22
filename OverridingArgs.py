

# from multipledispatch import dispatch 

#========FOR Interger Numbers: with different amount of arguments==============================
# @dispatch(int,int)
# def sum(a,b):
#          return a+b
# @dispatch(int,int,int)
# def sum(a,b,c):
#     return a+b+c


# print(sum(20,20))
# print(sum(20,20,100))


#====================*args for unlimited amount  of arguments=====================================
def sum1(*args):
    s=0
    for item in args:
       s+=item  
    return s
print(sum1(20,45,58,89))
print(sum1(20,45,58,89,200))
print(sum1(20,45,58,89,500,789))








#========FOR  STRING ==============================

# def sum(datatype , *args):
#     if(datatype=='int'):
#         return f"THIS IS  INTEGER"
#     elif(datatype=='str'):
#         return f"THIS IS  STRING"    
            
        
# print(sum('str',"andy","Dany"))
# print(sum('int',15,58))









