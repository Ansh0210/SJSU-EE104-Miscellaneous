# Author: Shivansh Shukla
# I have combined question 9 and 10 of the final exam in this code which includes the FSM logic and the test

# This code has a FSM class which handles the FSM logic. At the end of the class, I am initializing the class with certain values. 
# I provide the operation and then depending on the operation logic gets executed. 


class FSM:
    def __init__(self, value1, value2):
        # Initialize the FSM with initial state 'start' and two input values.
        self.state = "start"
        self.value1 = value1
        self.value2 = value2

    def transition(self, input):
        # Define the transitions based on the current state and input.

        # In the 'start' state, check the input and transition accordingly.
        if self.state == "start":
            if input == "00":
                self.state = "add"
            elif input == "01":
                self.state = "subtract"
            elif input == "10":
                print("Hello")
                self.state = "start"
            elif input == "11":
                print("Goodbye")
                self.state = "start"
            else:
                raise ValueError(f"Invalid input: {input}")

        # If in the 'add' state, perform addition and transition back to 'start'.
        if self.state == "add":
            result = self.value1 + self.value2
            print(f"{self.value1} + {self.value2} = {result}")
            self.state = "start"

        # If in the 'subtract' state, perform subtraction and transition back to 'start'.
        if self.state == "subtract":
            result = self.value1 - self.value2
            print(f"{self.value1} - {self.value2} = {result}")
            self.state = "start"

# Example usage of the test case
# Initialize the FSM with values 8 and 6.
fsm = FSM(8, 6)

# Provide different inputs to trigger different transitions.
fsm.transition("00")  # Adds the values (8 + 6)
fsm.transition("01")  # Subtracts the values (8 - 6)
fsm.transition("10")  # Prints "Hello" and transitions to 'start'
fsm.transition("11")  # Prints "Goodbye" and transitions to 'start'
