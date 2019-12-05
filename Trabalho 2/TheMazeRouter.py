#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TheMazeRouter():
    def __init__(self):
        self.matriz = self.readFile()
    
    def readFile(self):
        with open("Matriz.txt") as file: # Use file to refer to the file object
            matriz = []
            lines = file.readlines()
            for line in lines:
                elementsLine = line.replace(" ", "").replace("\n","")
                matrizLine = []
                for element in elementsLine:
                    matrizLine.append(element)
                matriz.append(matrizLine)
            return matriz
        
    def printMatriz(self):
        for linha in self.matriz:
            for val in linha:
                print('{:4}'.format(val), end="")
            print()
        
    def isDestiny(self, line, column):
        try:
            if self.matriz[line-1][column] == "T" or self.matriz[line+1][column] == "T" or self.matriz[line][column-1] == "T" or self.matriz[line][column+1] == "T":
                return True
            else:
                return False
        except:
            return False
    
    def canFill(self, line, column):

        
        
        if (self.matriz[line][column] != "X" and self.matriz[line][column] != "-" and 
            self.matriz[line][column] == "0"):

            return True
        else:

            return False
            
    def fillNeighbor(self, home):
        pointerReturn = "" 
        
        for line in range(0, len(self.matriz)):
            for column in range(0, len(self.matriz)):
                if self.matriz[line][column] == home:
                    if home == "S":
                        if (not(self.isDestiny(line, column))):
                            try:
                                self.matriz[line][column] = "1"
                            except IndexError:
                                pass
                            pointerReturn = "1"
                        else:
                            print("Comprimento: 1")
                            return "T"
                            
                    else:
                        if(not(self.isDestiny(line, column))):
                            try:
                                
                                if (self.canFill(line-1, column)):
                                    self.matriz[line-1][column] = str(int(home)+1)
                                    
                                if (self.canFill(line+1, column)):
                                    self.matriz[line+1][column] = str(int(home)+1)
                                    
                                if (self.canFill(line, column-1)):
                                    self.matriz[line][column-1] = str(int(home)+1)
                                    
                                if (self.canFill(line, column+1)):
                                    self.matriz[line][column+1] = str(int(home)+1)
                                    
                                    
                                
                            except IndexError:
                                pass
                            pointerReturn = str(int(home)+1)
                        else:
                            print("Comprimento: \n", home)
                            return "T"
                            

        return pointerReturn
                
                        
     
    def algorithm(self):
        home = "S"
        result = self.fillNeighbor(home)
        while(result != "T"):
            result = self.fillNeighbor(result) 
    
    def writeFile(self):
        with open("Output.txt", "w") as f: 
            for linha in self.matriz:
                for val in linha:
                    #{:>12}  {:>12}  {:>12}'.format(word[0], word[1], word[2])
                    f.write("{:>3}".format(val))

                f.write("\n\n")
        


# In[2]:


TMR = TheMazeRouter()


# In[3]:


TMR.algorithm()
#TMR.printMatriz()
TMR.writeFile()


# In[ ]:




