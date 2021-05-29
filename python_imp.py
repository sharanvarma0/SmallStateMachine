from state import State 

''' This defines the FSM (Finite State Machine) class. It uses the state object and a dictionary for storage.
Each state accepts a single token, checks whether the current character matches its token/tokens.
If match is successful, the next state is returned and the finite state machine proceeds to it.
Else, the state is switched to ERROR indicating that the input was invalid for the states for this machine

initialize the dictionary. 
Add states to the dictionary which represent next states for a particular state.
For each character input, check if the char matches the tokens for the state,
    if match, proceed to next state.
    else ERROR, print bad input
'''

class FiniteStateMachine:
    def __init__(self):
        self.tok_next = {}

    def add_state(self, name, tokens, next_state):
        if name not in self.tok_next:
            self.tok_next[name] = []
        self.tok_next[name].append(State(name, tokens, next_state))

    def run(self, input):
        input_num = input
        current_state = "START"
        while True:
            if len(input) > 0:
                current_token = input[0]
                input = input[1:]
                found = False
                for machine_state in self.tok_next[current_state]:
                    if current_token in machine_state.get_tokens():
                        current_state = machine_state.get_nextstate()
                        found = True
                        break
               
                if not found:
                    err_msg = "Got %s in state %s" %(token, state)
                    current_state = "ERROR"

            else:
                if "*" in current_state:
                    current_state = "GOOD"
                else:
                    current_state = "ERROR"
                    err_msg = "More needed"
        
            if current_state == "GOOD":
                print("%s is good" % (input_num))
                break
            if current_state == "ERROR":
                print("%s is bad" %(input_num))
                break
