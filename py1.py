class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def getArea(self):
        return self.width*self.length

rec=[]
n=int(input("enter no of rectangles"))
for i in range(n):
    width=int(input("enter the width"))
    length=int(input("enter the height"))
    obj=Rectangle(width,length)
    rec.append(obj)

lst=sorted(rec,key=Rectangle.getArea)

print("least rectanglw has width ",lst[0].width," and height ",lst[0].length)