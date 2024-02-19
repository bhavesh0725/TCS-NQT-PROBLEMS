import math

def rootOfQE(a,b,c):
  d=(b**2) - (4*a*c)
  x1=0
  x2=0
  
  if d ==0 :
    print("Roots are real and equal")
    x1 = ((-b + math.sqrt(d))// 2*a)
    x2 = ((-b - math.sqrt(d))// 2*a)
  elif d >0:
    print("Roots are real and different")
    x1 = ((-b + math.sqrt(d))// 2*a)
    x2 = ((-b - math.sqrt(d))// 2*a)
  else:   # this part needs to be modified, not giving desired result.
    print("Roots are complex and different")
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(d)) / (2 * a)
    x1 = complex(real_part, imag_part)
    x2 = complex(real_part, -imag_part)
    
   


  return x1,x2

if __name__=="__main__":
  print("The standard form of a quadratic equation is:ax2 + bx + c = 0")
  a= int(input("Enter the value of a: "))
  b= int(input("Enter the value of b: "))
  c= int(input("Enter the value of c: "))

  x1,x2= rootOfQE(a,b,c)
  print("The roots are : ", x1,x2)
  
  
  