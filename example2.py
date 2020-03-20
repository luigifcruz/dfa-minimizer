from minimizer import DFA

dfa = DFA()

# Add DFA States
dfa.add_state(0)
dfa.add_state(1)
dfa.add_state(2)
dfa.add_state(3)
dfa.add_state(4)

# Set Initial and Final(s) State
dfa.add_start_state(0)
dfa.add_final_state(0)

# Register Alphabet
dfa.add_symbol('0')
dfa.add_symbol('1')

# Register Transitions
dfa.add_transition(0, '0', 0)
dfa.add_transition(0, '1', 2)
dfa.add_transition(2, '1', 0)
dfa.add_transition(2, '0', 3)
dfa.add_transition(3, '0', 1)
dfa.add_transition(1, '1', 0)
dfa.add_transition(1, '0', 3)
dfa.add_transition(3, '1', 4)
dfa.add_transition(4, '1', 4)
dfa.add_transition(4, '0', 1)

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