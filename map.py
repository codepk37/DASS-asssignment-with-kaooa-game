import math as m
import matplotlib.pyplot as  plt
dir={
    "N":[0,1],
    "S":[0,-1],
    "W":[-1,0],
    "E":[1,0],
    "NW":[-1/m.sqrt(2),1/m.sqrt(2)],
    "NE":[1/m.sqrt(2),1/m.sqrt(2)],
    "SW":[-1/m.sqrt(2),-1/m.sqrt(2)],
    "SE":[1/m.sqrt(2),-1/m.sqrt(2)]  #add required vectors
}



class Path:
    globalx=0
    globaly=0
    globalP=[(0,0)] #initially at origin, to plott
    
    def __init__(self):
        self.Vectors=[]  #represent contribution of each (3,"NE") magnitude 
    
    def add_path(self,x,y):
        m=(x,y)
        self.Vectors.append(m)

        self.globalx=self.globalx+x
        self.globaly=self.globaly+y

        mm=(self.globalx,self.globaly)
        self.globalP.append(mm)
    
    def saveVectors(self,data):        
        for tup in data:
            measure=tup[0]  #0 arg
            direction=tup[1]
            num=""

            for i in measure:  #getting float out of "4.5mm"
                if(str(i).isdigit() or (i)=="." ):
                    num=num+i
            
            # templ={float(num):dir[direction]}
            # print(templ)

            x= float(num)* dir[direction][0]
            y= float(num)* dir[direction][1]

            # print(x,"  ",y)
            self.add_path(x,y)

    def printpath(self):
        for tup in self.Vectors:
            x=tup[0]
            y=tup[1]
            # print("  :",x,"  ",y)


    def getlistV(self):
        return self.Vectors
    
    def getlistP(self):
        return self.globalP
    
    
    def ds(self,endx,endy):
        if(endx==0 and endy==0):
            return "Same location at origin"
        elif(endx==0):
            if(endy>0):
                return "North"
            else:
                return "South"
        elif(endy==0):
            if(endx>0):
                return"East"
            else:
                return "West"
        else:
            if(endx>0 and endy>0) :
                return "North-East"
            elif(endx<0 and endy>0) :
                return "North-West"
            elif(endx<0 and endy<0) :
                return "South-West"
            elif(endx>0 and endy<0) :
                return "South-East"
            




#INPUT 
##### format  issue ,therefore used ast  
import ast
file1 = open("input_2.txt", "r+")   #input file has: [("3cm", "N"), ("4.5mm", "NW"),("2mm", "SE")]
print("Output of Read function is ")
data_file=file1.read()   

# convert string representation actual list
try:
    data = ast.literal_eval(data_file)
except ValueError:
    print("Error: Invalid data format in the file.")
    data = []

print(data)
########



# data = [("3cm", "N"), ("4.5mm", "NW"), ("2mm", "SE")] #input


path = Path()  #object of class
path.saveVectors(data)
path.printpath()

#TESTING
print("V  to move  ",path.getlistV())
print("Pos after move  ",path.getlistP()) ##PLOT


####################33
# Matplotbit code
coordinate=path.getlistP()

xvalue, yvalue= zip(*coordinate) #seperates into seperate list

plt.scatter(xvalue, yvalue, color='blue', marker='o', label='Points') #plot points

plt.plot(xvalue, yvalue, color='red', linestyle='--', linewidth=2, label='Lines') #plotting lines connecting consecutive points


plt.xlabel('West   ---------  East ')
plt.ylabel('North  ---------  South') #axis label

plt.title('Origin is Start(0,0)')#plot title

plt.axis('equal') #scales x and y axix in between accordingly

plt.axhline(0, color='black', linewidth=0.5) #drawing x and y axis
plt.axvline(0, color='black', linewidth=0.5)

plt.legend() #shows notations of point and box ,top right

plt.show()       #show plot display
print("\n------------------------------\n\n")
##########################3




####### 2nd and 3rd claculations
endx=path.globalx
endy=path.globaly
print(endx,"  ",endy)        
print("WRT starting point direction:    ",path.ds(endx,endy)) #returns direction


tot_distance= m.sqrt( (endx*endx) + (endy*endy) )
print("WRT starting point distance:    ",tot_distance)
##########

