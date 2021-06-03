from scipy.integrate import odeint

def denominator(x,y):
        return (x**2+y**2)**1.5

def fx(x,y,GM,ph):
        return(-1*(x)*GM/denominator(x,y))

def fy(x,y,GM,ph):
    return(-1*(GM*y)/denominator(x,y))
class Satelite:
    x=0
    y=0
    R=1
    Rs=1
    GM=5
    
    def Satellite(self,x,y,R,Rs,G,M):
        self.x=x
        self.y=y
        self.R=R
        self.Rs=Rs
        self.GM=G*M
            
    def calculateX(self,time):
        return odeint(fx,self.y,time,(self.GM,0))
        
    def calculateY(self,time):
        return odeint(fy,self.x,time,(self.GM,0))
        
    def set_x(self,x):
        self.x=x+self.R+self.Rs
    
    def set_y(self,y):
        self.y=y+self.R+self.Rs
        
    def set_R(self,R):
        self.R=R
    
    def set_Rs(self,Rs):
        self.Rs=Rs
        
    def set_GM(self,G,M):
        self.GM=G*M
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_R(self):
        return self.R
    
    def get_Rs(self):
        return self.Rs
    
    def get_GM(self):
        return self.GM