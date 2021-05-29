from python_imp import FiniteStateMachine

''' This is the main python program. Run the state machine and define new states here. 
This file keeps the FSM code and the state code modularized and easy to manage and maintain.

Tests can be included in this file. If required, the finite state machine can be imported as its own module
for use in other projects.
'''

fsm = FiniteStateMachine()
fsm.add_state("START", "1234567890", "SECOND_DIGIT_ONWARDS*")
fsm.add_state("START", "-", "AFTER_MINUS")
fsm.add_state("AFTER_MINUS", "1234567890", "SECOND_DIGIT_ONWARDS*")
fsm.add_state("SECOND_DIGIT_ONWARDS*", "1234567890", "SECOND_DIGIT_ONWARDS*")
fsm.add_state("SECOND_DIGIT_ONWARDS*", ".", "AFTER_DOT")
fsm.add_state("AFTER_DOT", "1234567890", "MANTISSA*")
fsm.add_state("MANTISSA*", "1234567890", "MANTISSA*")

fsm.run("3.14")
fsm.run("-")
