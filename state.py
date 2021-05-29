''' This file defines a token class that represents a single entry of state in the Finite State machine
Each state recorded by the machine is stored in a dictionary with the name and value which is a State object.

This class defines parameters like 
  - name of the state 
  - valid token input to a state 
  - the state which would
'''

class State:
    def __init__(self, state_name, input_tokens, nextstate): 
        self._name = state_name
        self._input_tokens = input_tokens
        self._nextstate = nextstate
    
    ''' define getter methods. There is no need of setter methods as only defination is required.
    To delete a state, we can remove it from the state machine's states. No need to set the state '''

    def get_name(self):
        return self._name

    def get_tokens(self):
        return self._input_tokens

    def get_nextstate(self):
        return self._nextstate
