
#Neuron program
import random.random as randomNumber
import math

class cells(object):
    def __init__(self, num, layers=1):
        self.neurons = [] #List structure is [layer_no[neuron_wieghts(index=num)]] contained within a list
        #I really want to get this to be something stored in disk and only load each layer
        #self.state = []
        self.Input_neurons = []
        self.Output_neurons = []

    def build(self, num, layers):
        self.each_lay = num // layers
        weights = []
        self.layers = layers
        del num
        del layers

        for i in range(self.each_lay):
            weights = [randomNumber for i in range(self.each_layer)]
        
        for i in range(self.layers):
            self.neurons.append([]) #adds a list
            for n in range(self.each_lay):
                self.neurons[i].append([])
                self.neurons[i][n].extend(weights) #Could be better (more random for each one)

        del weights

    def Input(self, inputs): #This is really bad Runs HOLE program effectivly.
        state = []
        for neuron, i in enumerate(self.Input_neurons):
            state.append([])
            for wieght, it in enumerate(neuron):
                state[i].append([])
                state[i][it].append(wieght*inputs[i])

        for i in range(len(state)): #adds all together
            state[i] = self.sigmore(sum(state[i]))
            
        return self.output(self.run(state))

    def run(self, state):
        new_state = []
        for x in range(self.layers):
            for s, x in enumerate(state):
                for layer_no in range(self.each_layer):
                    new_state.append([i * s for i in self.neurons[x][layer_no]])
                    new_state[layer_no] = sum(new_state[layer_no])
                    
            state= new_state
            new_state = []

        del new_state
        return state

    
    def output(self, output): 
        state = []
        for neuron, i in enumerate(self.Output_neurons):
            state.append([])
            for wieght, it in enumerate(neuron):
                state[i].append([])
                state[i][it].append(wieght*inputs[i])

        for i in range(len(state)): #adds all together
            state[i] = self.sigmore(sum(state[i]))
                
    def sigmore(self, x):
        y = 1+math.e**-x # Math a matical function. e is a mathamatical constant and is not the error value
        y = 1/y
        return y  # It creates a slow curve it may also been known as an "activation" function

        
            
            
            
            
        

