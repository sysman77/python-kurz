from abc import ABC, abstractmethod
import os

# Define an abstract base class for output types


class OutputType(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass

# Implement the console output type


class ConsoleOutput(OutputType):
    def display(self):
        print(self.data)

# Implement the file output type


class FileOutput(OutputType):
    def display(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_dir)

        with open('output.txt', 'w') as f:
            f.write(self.data)

# The Output class uses the output type classes


class Output:
    def __init__(self, data, output_type):
        self.data = data
        self.output_type = output_type(data)

    def display(self):
        self.output_type.display()

# Example usage


console_output = Output("some string", ConsoleOutput)
console_output.display()

file_output = Output("some string", FileOutput)
file_output.display()
