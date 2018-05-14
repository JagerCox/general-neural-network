from perceptron import *


class NeuralNetwork:

    debug = False
    perceptrons = []

    # Constructor

    def __init__(self, number_perceptrons, function_perceptron="medium.snippet"):
        self.perceptrons = []
        for i in range(number_perceptrons):
            self.perceptrons.append(Perceptron(function_perceptron))
            self._message("Create perceptron: " + function_perceptron + str(self.perceptrons[len(self.perceptrons)-1]))

    # Private

    def _message(self, message):
        if self.debug:
            print(message)

    # Public

    def all_sigmas(self, test_values=[]):
        total_sigma = 0
        for i in range(len(self.perceptrons)):
            total_sigma += self.perceptrons[i].sigma_value(test_values[i])
            self._message("Perceptron "+ str(self.perceptrons[i]) + " , sigma value : " + str(self.perceptrons[i].sigma_value(test_values[i])))
        return total_sigma

    def all_sigmas_as_list(self, test_values=[]):
        total_sigma = []
        for i in range(len(self.perceptrons)):
            total_sigma.append(self.perceptrons[i].sigma_value(test_values[i]))
        return total_sigma

    # Public properties

    def get_number_perceptrons(self):
        return len(self.perceptrons)

    def set_weight_perceptrons(self, values=[]):
        for i in range(len(self.perceptrons)):
            self.perceptrons[i].set_weight(values[i])

    def get_weight_perceptrons(self):
        weight_perceptrons = []
        for i in range(len(self.perceptrons)):
            weight_perceptrons.append(self.perceptrons[i].get_weight())
        return weight_perceptrons

    def set_memory_raw_perceptrons(self, values=[]):
        # values=[] as list of list
        for i in range(len(self.perceptrons)):
            self.perceptrons[i].set_memory_raw(values[i])

    def get_memory_raw_perceptrons(self):
        memories_raw = []
        for i in range(len(self.perceptrons)):
            memories_raw.append(self.perceptrons[i].get_memory_raw())
        return memories_raw

    def set_bia_perceptrons(self, values=[]):
        for i in range(len(self.perceptrons)):
            self.perceptrons[i].set_bias(values[i])

    def get_bia_perceptrons(self):
        bia_perceptrons = []
        for i in range(len(self.perceptrons)):
            bia_perceptrons.append(self.perceptrons[i].get_bias())
        return bia_perceptrons

    # Public add values training and evaluate

    def add_values_by_perceptron(self, values=[]):
        self._message("Number perceptrons: " + str(len(self.perceptrons)))
        self._message("Number values: " + str(len(values)))
        for i in range(len(self.perceptrons)):
            self.perceptrons[i].add_value_raw(values[i])

    # Public properties by index

    def set_weight_perceptron(self, i, value):
        self.perceptrons[i].set_weight(value)

    def get_weight_perceptron(self, i):
        return self.perceptrons[i].get_weight()

    def set_memory_raw_perceptron(self, i, values=[]):
        self.perceptrons[i].set_memory_raw(values)

    def get_memory_raw_perceptron(self, i):
        self.perceptrons[i].get_memory_raw()

    def set_bia_perceptron(self, i, value):
        self.perceptrons[i].set_bias(value)

    def get_bia_perceptron(self, i):
        return self.perceptrons[i].get_bias()

    # Public IO file

    def write_sigmas_as_csv(self, path_output, test_values=[]):
        v = self.all_sigmas_as_list(test_values)
        f = open(path_output, "w")
        for i in range(len(v)):
            f.write(str(i)+","+str(v[i])+"\n")
        f.close()
