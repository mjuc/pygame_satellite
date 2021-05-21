from scipy import integrate

class Satelite:
    def Satellite(self,x,y,R,Rs,G,M):
        self.x=x
        self.y=y
        self.R=R
        self.Rs=Rs
        self.GM=G*M
            
    def denominator(self):
        return (self.x**2+self.y**2)**1.5
    
    def calculateX(self):
        self.x=integrate(integrate(-1*(self.GM*self.x)/self.denominator()))
    
    def calculateY(self):
        self.x=integrate(integrate(-1*(self.GM*self.y)/self.denominator()))