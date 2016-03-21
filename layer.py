from copy import *
from neuron import *

class Layer:
    """
    This class represents a layer of neurons, as defined here:
    https://en.wikipedia.org/wiki/Artificial_neural_network

    Neurons in a same layer do not communicate with each other.
    Note that they all take the same list of inputs. Thus, the main purpose of a layer
    of neurons is to take a list of input (of the size of neuron's input), and to
    yield the result of every neuron of the layer, in the form of a list.
    """

    def __init__(self, arg1, arg2 = None):
        """
        Method 1 : my_layer = Layer(nbr_neuron, nbr_input)
            Inits a layer that has 'nbr_neuron' neurons that all take 'nbr_input' inputs
            :param nbr_neuron: nbr of neurons in the layer
            :param nbr_input: nbr of input every neuron takes
            if this layer is an intermediate layer, then 'nbr_input' has to be equal
            to the number of neurons in the previous layer, for each of these neurons
            yieldsone output.
        Method 2 : my_layer = Layer(list_neurons)
            Inits a layer from a list of existing neuron.
            All neurons have to take the same number of input.
        """

        if isinstance(arg1, int) and isinstance(arg2, int):
            #method 1
            self.nbr_neuron = arg1
            self.nbr_input = arg2
            self.neurons = []
            for i in range(self.nbr_neuron):
                self.neurons.append(Neuron(self.nbr_input))
        elif arg2 == None and isinstance(arg1, list):
            #check if arg1 is a list of neurons
            for a in arg1:
                if not isinstance(a, Neuron):
                    raise TypeError("In 'Layer.__init__()' : The list you provided does not only contain neurons. It should.")
            #method 2
            self.neurons = deepcopy(arg1)
            self.nbr_neuron = len(self.neurons)
            self.nbr_input = self.neurons[0].nbr_input

            #check if every neuron has the same number of input
            for neuron in self.neurons:
                if neuron.nbr_input != self.nbr_input:
                    raise ValueError("In 'Layer.__init__()' : the neurons you provided do not all take the same number of input.\n")
        else:
            raise TypeError("In 'Layer.__init__()' : wrong arguments passed.\n")

    def get_output(self, list_input):
        """
        This function feeds every neuron of the layer with 'list_input', and returns
        the result of each neuron in form of a list.
        """

        #protection
        if(len(list_input) != self.nbr_input):
            raise ValueError("In Layer.output() (id : " + str(id(self)) + " : list_input has wrong size.\n")

        #calculation
        output = []
        for neuron in self.neurons:
            output.append(neuron.output(list_input))

        return output

    def mutate(self, level):
        """
        randomly changes weights of neurons.
        level 1 : chooses one neuron randomly and changes one of its weight randomly
        level 2 : chooses one neuron randomly and resets it.
        level 3 : for each neuron, changes one of its weight randomly
        """

        if(level == 1):
            i = randrange(self.nbr_input)
            self.neurons[i].mutation()
        elif(level == 2):
            i = randrange(self.nbr_input)
            self.neurons[i] = Neuron(self.nbr_input)
        elif(level == 3):
            for neuron in self.neurons:
                neuron.mutation()
        else:
            raise ValueError("In Layer.mutate() (id : " + str(id(self)) + " : given level unknown.\n")

    def __repr__(self):
        res = ""
        for neuron in self.neurons:
            for i in range(self.nbr_input):
                res += str(neuron.list_weight[i]) + "\n"
            res += "\n"

        return res

    #The following functions were created in order to meet python's protocol for
    #sequences. (protocol = interface in python)
    #with the following function, 'Layer' will act as a "sequence" (like a list)
    #of neurons. eg: 'for neurons in layer:'
    def __len__(self):
        """called when len() is called on a Layer object"""
        return self.nbr_neuron

    def __getitem__(self, key):
        """called when you use the 'object[key]' notation"""
        if(key >= self.nbr_neuron):
            raise ValueError("in 'Layer.__getitem__()' : No such neuron. There is only " + str(nbr_neuron) + ", you asked for 'layer[" + str(key) + "]'.\n")
        return self.neurons[key]

    def __setitem__(self, key, value):
        """called when you use the 'object[key] = value' notation"""
        if(key >= self.nbr_neuron):
            raise ValueError("in 'Layer.__setitem__()' : No such neuron. There is only " + str(nbr_neuron) + ", you asked for 'layer[" + str(key) + "]'.\n")
        if isinstance(value, Neuron):
            raise TypeError("in 'Layer.__setitem__()' : layer only contains Neurons, not " + str(type(value)) + "s.\n")

        self.neurons[key] = value

    def __delitem__(self, key):
        """called when you 'del' an object"""
        return self.neurons.__delitem__()

    def __iter__(self):
        return self.neurons.__iter__()

    def __reversed__(self):
        return self.neurons.__reversed__()