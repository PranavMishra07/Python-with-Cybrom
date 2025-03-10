# for i in range(1,6):
#     for j in range(1,i+1):
#            print(i,end=" ")
#     print()
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# for i in range(1,6):
#     for j in range(1,i+1):
#            print("*",end=" ")
#     print()
# * 
# * *
# * * *
# * * * *
# * * * * *
   

# for i in range(1,6):
#     for j in range(1,i+1):
#            print(chr(120),end=" ")
#     print()
# x 
# x x
# x x x
# x x x x
# x x x x x


# for r in range(1,6): # r=1,2,3,4,5
#     for c in range(1,r+1):          #1,2,3,4,5
#         print("*",end=" ")
#     print()
# * 
# * *
# * * *
# * * * *
# * * * * *



# for r in range(6,0,-1):
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *





# for r in range (1,6):
#     for c in range(1,r+1):
#         print(r,end=" ")
#     print()
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5





# for r in range (1,6):
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for r in range (6,1,-1):
#     for c in range(1,r):
#         print(c,end=" ")
#     print()
# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1



# n=1
# for r in range (1,6):   
#     for c in range(1,r+1):        
#         print(n,end=" ")  
#         n+=1  
#     print()
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15





# for r in range(1,6):
#     for c in range(1,r+1):
#         print(chr(64+r),end=" ")
#     print()
# A 
# B B
# C C C
# D D D D
# E E E E E




# for r in range(1,6):
#     for c in range(1,r+1):
#         print(chr(64+c),end=" ")
#     print()
# A 
# A B
# A B C
# A B C D
# A B C D E

# for i in range(65,71):
#      for j in range(65,i+1):
#           print(chr(j),end=" ")
#      print()
        


# n=1
# for r in range(1,8):
#     for c in range(1,r+1):
#         print(chr(64+n),end=" ")
#         if(n==26):
#             break
        
#         else:
#                n+=1        
#     print()
# A 
# B C
# D E F
# G H I J
# K L M N O
# P Q R S T U
# V W X Y Z 




# for r in range(1,6):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#           print("*",end=" ")
#     print()
#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *



# n=1
# for r in range(1,6):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,r+1):
#         print(chr(64+n),end=" ")
#         n+=1
#     print()
#           A 
#         B C
#       D E F
#     G H I J
#   K L M N O


# for r in range(1,6):
#     for c in range(1,r+1):
#         print((r+c)%2,end=" ")
#     print()
# 0 
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0



# for r in range(1,6):
#     for c in range(1,r+1):
#         if (r+c)%2==0 :
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()
# 0 
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0


# for r in range(1,6):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,2*r):
#         print("*",end=" ")
#     print()
#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *



# for r in range(5,0,-1):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,2*r):
#         print("*",end=" ")
#     print()
#   * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *




# for r in range(1,6):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,2*r):
#         print("*",end=" ")
#     print()

# for r in range(6,0,-1):
#         for c in range(6,r,-1):
#             print(" ",end=" ")
#         for c in range(1,2*r):
#             print("*",end=" ")
#         print()

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *







# for r in range(1,6):
#     for c in range(6,r,-1):
#         print(" ",end=" ")
#     for c in range(1,2*r):
#         print("*",end=" ")
#     print()

# for r in range(6,0,-1):
#         for c in range(6,r,-1):
#             print(" ",end=" ")
#         for c in range(1,2*r):
#             print("*",end=" ")
#         print()




# for i in range(5):
#      for j in range(0,i+1):
#           print(j,end=" ")
#      print()


# for i in range(5):
#      for k in range(5-(i+1)):
#           print("",end=" ")
#      for j in range(0,i+1):
#           print("*",end=" ")
#      print()


# for i in range(5,0,-1):  # i=5,4   
#      for k in range(5-i):  #k= 0 0  space print,1 1 space print,2 2space print
#           print("",end=" ")
#      for j in range(0,i):  #j=5  5star print,4 4 star print,3 3star print
#           print("*",end=" ")
#      print()

# for row in range(7):
#     for col in range(5):
#           if (row==0 or row==3 or row==6) or (col==0 or col==4):
#             print("*",end=" ")  
#           else:
#             print(" ",end=" ")              
#     print()
    

# for row in range(10):
#     for col in range(10):
#           if ( row==0 or row==4  or row==9) or (col==0 or col==6  or col==):
#             print("*",end=" ")  
#           else:
#             print("",end=" ")              
#     print()
    
for row in range(10):
    for col in range(10):
          if ( row==0 or row==4  or row==9) or (col==0 or col==6  or col==5):
            print("*",end=" ")  
          else:
            print("",end=" ")              
    print()