import math
class Fraction:
    def __init__(self,n,d):
        if d==0:
            raise Exception("Division by 0")
        else:
            k=math.gcd(n,d)
            self.numerator=n//k
            self.denominator=d//k
    
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def __add__(self,other):
        n=other.numerator*self.denominator+other.denominator*self.numerator
        d=self.denominator*other.denominator
        k=math.gcd(n,d)
        n=n//k
        d=d//k
        return Fraction(n,d)

    def inverse(self):
        return Fraction(self.denominator,self.numerator)

    def __eq__(self,other):
        if self.numerator==other.numerator and self.denominator==other.denominator:
            return True
        return False
    
    def __mul__(self,other):
        n=self.numerator*other.numerator
        d=self.denominator*other.denominator
        k=math.gcd(n,d)
        n=n//k
        d=d//k
        return Fraction(n,d)

if __name__ == "__main__":
    f=Fraction(4,3)
    print(f)
    f2=Fraction(8,16)
    print(f==f2)