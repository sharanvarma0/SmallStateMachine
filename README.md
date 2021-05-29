This is a small project for a finite state machine. Nothing complex for now. The tests included involve validating floating point numbers.

I have written the program in modules to keep it organized and if required, to import these in other projects if necessary.

State - state.py, represents the states of the machine. Each state has a name, the tokens which are valid for the state and the next state to proceed to if validation is successful.

FiniteStateMachine - python_imp.py, the state machine itself. Takes input and passes it through State objects and determines if given input is good or not for the defined state machine.

main.py - the test and execution program, I have written a small test program involving tests for number validation. Each state ending with a * represents a good state. This represents a state which could be an ending state for successful validation. If the state machine stops on any other state, the validation is unsuccessful.

I will try to expand on it or find creative uses for this whenever I find the time to do so.
