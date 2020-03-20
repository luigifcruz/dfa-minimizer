from minimizer import DFA

dfa = DFA()

# Add DFA States
dfa.add_state(1)
dfa.add_state(2)
dfa.add_state(3)
dfa.add_state(4)
dfa.add_state(5)

# Set Initial and Final(s) State
dfa.add_start_state(1)
dfa.add_final_state(1)
dfa.add_final_state(5)

# Register Alphabet
dfa.add_symbol('a')
dfa.add_symbol('b')

# Register Transitions
dfa.add_transition(1, 'a', 3)
dfa.add_transition(1, 'b', 2)
dfa.add_transition(2, 'b', 1)
dfa.add_transition(2, 'a', 4)
dfa.add_transition(3, 'b', 4)
dfa.add_transition(3, 'a', 5)
dfa.add_transition(4, 'a', 4)
dfa.add_transition(4, 'b', 4)
dfa.add_transition(5, 'a', 3)
dfa.add_transition(5, 'b', 2)

# Print and Draw Before Diagram
print('=' * 10, 'Before Minimization', '=' * 10)
dfa.print()
dfa.draw("dfa_before")

# Minimize
dfa.minimize()

# Print and Draw After Diagram
print('=' * 10, 'After Minimization', '=' * 10)
dfa.print()
dfa.draw("dfa_after")