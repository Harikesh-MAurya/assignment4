# (question-1).........................................................
from turtle import width


a=input("Enter your name : ")
print(a)


# (question-2).........................................................
a=int(input("Enter number : "))
print(a)


# (question-3).......................................................
a,b=input("Enter two number : ").split(",")
a,b=int(a),int(b)
print(a+b)


# (question-4).......................................................
r=int(input("ENter radius : "))
radius=3.14*(r*r)
print(radius)


# (question-5).......................................................
x=int(input("ENter number : "))
print(x*x)


# (question-6).........................................................
height,width=input("ENter height and width : ").split(",")
area_of_trangle=1/2*height*width
print(area_of_trangle)


# (question-7).......................................................
a,b,c=input("enter three number : ").split(",")
a,b,c=int(a),int(b),int(c)
print((a+b+c)/3)


#(question-8)........................................................
p,r,t=1000,0.25,5
print((p*r*t)/1000)


# (question-9).......................................................
a=int(input("enter a : "))
volume_of_cube=a*a*a
print(volume_of_cube)


# (question-10).....................................................
h,w=int(input("enter h  :")),int(input("enter w : "))
print(h*w)