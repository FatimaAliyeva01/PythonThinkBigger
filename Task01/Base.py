# Base classımız var və tərkibində iki property var
#class Base:
    #prop1='Something'
    #prop2='Somtehing2'
# Derived classımız var Base class-ından miras alır və tərkibində property yoxdur
#class Derived(Base):

#Base classını elə dəyişdirməyiniz lazımdır ki . 
#obj=Derived() 
#obj obyektində sadəcə prop1 property-sinin nəticəsi görənə bilsin amma prop2 görünməsin. 
#Qısaca Base classının daxilindəki 2 property-dən sadəcə birinin miras olaraq Derived class-a ötürülməsini təmin edin

# class Base:
#     def __init__(self):
#         self.prop1 = "something1"
#         self.__prop2 = "something2"

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print(self.prop1)
#         print(self.__prop2)
        
# obj=Derived()

class Base(object):
    def __init__(self,name,prop1,prop2):
        self.name=name
        self.prop1=prop1
        self.__prop2=prop2



a1=Base("something1", "","")
a2=Base("something2","","" )

print(a1.name,a1.prop1)
print(a2.name,a2.prop2)