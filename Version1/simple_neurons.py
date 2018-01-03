import math, random

class cell(object): # This is the class object cell - note this is not very effcient but should be clear and consice enough for beginers into the field of AI

    def __init__(self, wieght, learning_value=0.5): #This is called imediatly when the class is called
        self.wieghts = wieght # Wieghts do the "learning" as they change the values.
        self.learning_value = learning_value

        
    def Input(self, inputs):
        value = 0
        for x in range(len(inputs)):
            value +=  self.wieghts[x]*inputs[x] #Multiplying the Wieghts of the "Synapses" by the "signal strength" ie the input values
            
        self.output = self.Sig(value) #gives output

    def Sig(self, x):
        y = 1+math.e**-x # Math a matical function. e is a mathamatical constant and is not the error value
        y = 1/y
        return y  # It creates a slow curve it may also been known as an "activation" function


    def Backpropagation(self, error): #Correct the mistake/make it more accuate use a "training set" which is 10 times greater than the number of "synapes" aka wieghts
        """This is not how it's done for a whole network or mulitple synapes as you need to
           say how much each synapse accounted for the error however the same maths applt"""
        for x in range(self.wieghts):
            DeltaW = error/self.wieghts #Delta Wieght (change in wieght) is directly proptional to error and origonal wieght as error = (A-A^[the value that would mean that it was corrct - the desired value]) and the origonal line being Ax the new one A^X
            # ^ = hat so A^ is A hat. (not a)
            # View/think of it as a stright line and work out how to work out the differnce between the too lines. The differce between the two lines is the error value
            DeltaW *= self.learning_value #This moderates the value other wise it will always learn exactly from the last set of data you gave it.
            self.wieghts[x] += DeltaW #This adds the Delta (change in) wieght to the current wieght (which is a list)



wieghts = {
    'NeuronAW': [random.random(), random.random()],
    'NeuronBW': [random.random()],
    }



neurons = {
    'NeuronA': cell(wieght = wieghts['NeuronAW']),
    'NeuronB': cell(wieght = wieghts['NeuronBW']),
    }

x =  neurons['NeuronA'].Input(inputs=(9,3)) #example of how to use Can also use a list but Tuplets are *slightly* more quicker when processing :P
print(neurons['NeuronA'].output) #Easly scalable.
