# Facebook
import matplotlib.pyplot as plt
import scipy.stats as s
import matplotlib.style as jj
jj.use('ggplot')


class Facebook:
    def __init__(self,years,users):
        self.years = years
        self.users = users
        
    def showGraph(self):
        return plt.plot(self.years,self.users,'r',label='Facebook',linewidth = 1.5,marker='o')

    
    
    

class Snapchat:
    def __init__(self,years,users):
        self.years = years
        self.users = users
        
    def showGraph(self):
        return plt.plot(self.years,self.users,'b',label='SnapChat',linewidth = 1.5,marker='o')


    

class Instagram:
    def __init__(self,years,users):
        self.years = years
        self.users = users
        
    def showGraph(self):
        return plt.plot(self.years,self.users,'y',label='Instagram',linewidth = 1.5,marker='o')
    
    

class Twitter:
    def __init__(self,years,users):
        self.years = years
        self.users = users
        
    def showGraph(self):
        return plt.plot(self.years,self.users,'g',label='Twitter',linewidth = 1.5,marker='o')


    
    
years =  [2015,2015.5,2016,2016.5,2017,2017.5,2018]
sc =  [235.4,363.8,547.2,798,959.4,1156.2,1179]
insta =[620.6,620.6,524.4,547.2,565.8,590.4,681.2]
twitter = [449.4,385.2,364.8,296.4,270.6,172.2,235.8]
fb = [256.8,278.2,342,296.4,270.6,221.2,209.6]



f1 = Facebook(years,fb)
sc1 = Snapchat(years,sc)
t1 = Twitter(years,twitter)
i1 = Instagram(years,insta)

f1.showGraph()
sc1.showGraph()
t1.showGraph()
i1.showGraph()


plt.ylabel("Users(in millions)")
plt.xlabel("Year")
plt.title("Decline of Facebook(Red)")
plt.legend()


plt.show()




#CODE BY SHUBHAM BERI AND SAHIL JASWAL
