#magicMethod(param) adında bir metod yazın.Bu ele bir metod olsun ki argument olaraq verilən param
#arraydirsə onun içindəki bütün elementləri ekrana çap elesin
#obyektdirsə onun properylerini ekrana cap etsin
#rəqəmdirsə kvadratını ekrana çap etsin
#stringdirsə cüt yerdə duran hərfləri böyük hərfə çevirsin



#1)rəqəmdirsə kvadratını ekrana çap etsin
def magicMethod(param):
  for x in param:
    print(x**2)

param = [1,2,3,4]

magicMethod(param)

#2)arraydirsə onun içindəki bütün elementləri ekrana çap elesin
def magicMethod1(param):
  for s in param:
    print()

param = set([1, 3, 5 ,7,9,11,13,15])
s = "backend developer"
print("".join(c.upper() if i in param else c for i, c in enumerate(s)))


magicMethod1(param)


#3)stringdirsə cüt yerdə duran hərfləri böyük hərfə çevirsin
def magicMethod2(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
A = [1, 2, 3, 4, 5, 6]
print(A)

#4)obyektdirsə onun properylerini ekrana cap etsin
def magicMethod3( name, age = 18 ):
   print ("Name: ", name)
   print ("Age ", age)
   return;

magicMethod3( age=56, name="Xanim" )
magicMethod3( name="Fatima" )