# complexoberations
import math
class complexoperatinins:
 def compadd(self,a,b,c,d):
    m1=(a+c),"+i",(b+d)
    return (m1)
 def compdif(self,a,b,c,d):
    m1=(a-c),"+i",(b-d)
    return (m1)
 def compmulti(self,a,b,c,d):
    m1=(a*c)-(b*d),"+i",(a*d)+(c*b)
    return (m1)
 def compdiv(self,a,b,c,d):
    dena=(c*c)+(d*d)
    print("denaminator=",dena)
    m1=(co.compmulti(a,b,c,-d))
    return (m1)
 def compconju(self,a,b):
    m1=(a,"+i",-b)
    return (m1)
 def compconjuadd(self,a,b,c,d):
    n0=co.compconju(a,b)
    n1=co.compconju(c,d)
    print("the conjucate of first complex is=",n0)
    print("the conjucate of second complex is=",n1)
    n=float(input("enter the real part in 1st complex"))
    h=float(input("enter the imagenary part in 1st complex"))
    o=float(input("enter the real part in 2st complex"))
    l=float(input("enter the imagenary part in 2st complex"))
    l0=co.compadd(n,h,o,l)
    return  (l0)
 def compconjudif(self,a,b,c,d):
    n0=co.compconju(a,b)
    n1=co.compconju(c,d)
    print("the conjucate of first complex is=",n0)
    print("the conjucate of second complex is=",n1)
    n=float(input("enter the real part in 1st complex"))
    h=float(input("enter the imagenary part in 1st complex"))
    o=float(input("enter the real part in 2st complex"))
    l=float(input("enter the imagenary part in 2st complex"))
    l0=co.compdif(n,h,o,l)
    return  (l0)
 def compconjumulti(self,a,b,c,d):
    n0=co.compconju(a,b)
    n1=co.compconju(c,d)
    print("the conjucate of first complex is=",n0)
    print("the conjucate of second complex is=",n1)
    n=float(input("enter the real part in 1st complex"))
    h=float(input("enter the imagenary part in 1st complex"))
    o=float(input("enter the real part in 2st complex"))
    l=float(input("enter the imagenary part in 2st complex"))
    l0=co.compmulti(n,h,o,l)
    return  (l0)
 def compconjudiv(self,a,b,c,d):
    n0=co.compconju(a,b)
    n1=co.compconju(c,d)
    print("the conjucate of first complex is=",n0)
    print("the conjucate of second complex is=",n1)
    n=float(input("enter the real part in 1st complex"))
    h=float(input("enter the imagenary part in 1st complex"))
    o=float(input("enter the real part in 2st complex"))
    l=float(input("enter the imagenary part in 2st complex"))
    l0=co.compdiv(n,h,o,l)
    return  (l0)
 def compmodulas(self,a,b):
    m0=(a*a)+(b*b)
    m1= math.sqrt(m0)
    return (m1)
 def compmodulasadd(self,a,b,c,d):
    n0=co.compadd(a,b,c,d)
    print(n0)
    e=float(input("enter the real part in complex number"))
    r=float(input("enter the imagenary part in complex number"))
    m1=co.compmodulas(e,r)
    return (m1)
 def compmodulasdif(self,a,b,c,d):
    n0=co.compdif(a,b,c,d)
    print(n0)
    e=float(input("enter the real part in complex number"))
    r=float(input("enter the imagenary part in complex number"))
    m1=co.compmodulas(e,r)
    return (m1)
 def compmodulasmulti(self,a,b,c,d):
    n0=co.compmulti(a,b,c,d)
    print(n0)
    e=float(input("enter the real part in complex number"))
    r=float(input("enter the imagenary part in complex number"))
    m1=co.compmodulas(e,r)
    return (m1)
 def compmodulasdiv(self,a,b,c,d):
    n0=co.compdiv(a,b,c,d)
    print(n0)
    e=float(input("enter the real part in complex number"))
    r=float(input("enter the imagenary part in complex number"))
    m1=co.compmodulas(e,r)
    return (m1)
 def convertingpolarform(self,a,b):
    m0=math.cos(a)
    m1=math.sin(b)
    l0=m0,"+i",m1
    return(l0)
co=complexoperatinins
