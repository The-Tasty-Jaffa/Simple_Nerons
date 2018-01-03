import numpy
import random
import operator
import functools as reduce #For some odd reason i cannot do "import random.uniform"

class network:
    def __init__(self, input_layer, hidden_layers, nodes_per_layer, output_layer):
        """initalises the network, nodes_per_layer = nodes in the hidden layer"""
        self.layers = []
        
        #Matrix multiplcation is not commutative
        self.build_input(input_layer, nodes_per_layer)
        self.build_hidden(hidden_layers, nodes_per_layer)
        self.build_output(output_layer, nodes_per_layer)

    def build_hidden(self, hidden_layers, nodes_per_layer):
        """Builds the hidden nodes"""
        weight = []

        #generates a uniform network
        for layer in range(hidden_layers-1): # one is added in build_output but there are less coloums in that one
            for node in range(nodes_per_layer): #Weight matrix per layer
                weight.append([random.uniform(-2,2) for i in range(nodes_per_layer)])
                #List addition
                #Colom = node in next layer
                #row = node in current layer
                #print(weight)

            self.layers.append(numpy.matrix(weight)) # Adds
            #print(self.layers)
            weight = []

        #Self.layers now contains all the matrices of the hidden neurons


    def build_input(self, input_layer, nodes_per_layer):
        """Builds the Input nodes"""

        weight = []
        
        for inp_node in range(input_layer):
            weight.append( [random.uniform(-2,2) for i in range(nodes_per_layer)] )
            # Fewer lines in python is quicker
            # Adds the input layer
        self.layers.append(numpy.matrix(weight))

    def build_output(self, output_layer, nodes_per_layer):
        """Builds the output nodes"""
        
        weight = []
        
        for x in range(nodes_per_layer): # Rows
            weight.append([random.uniform(-2,2) for i in range(output_layer)]) #coloums

        self.layers.append(numpy.matrix(weight))
            
    def run(self, inputs):
        """Runs the network once"""
        state = numpy.matrix(inputs)
        
        
        for layer in self.layers:
            state*=layer
            
        return state
        #Matrix multiplcation is assosiative
