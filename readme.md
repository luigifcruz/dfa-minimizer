# Deterministic Finite Automaton (DFA) Minimizer 
### Based on Hopcroft's Algorithm

This is a Python 3 script made to minimize a Deterministic Finite Automaton (DFA) using Hopcroft's Algorithm. This was made as an assignment for my university.

<p align="center">
<img src="https://github.com/luigifreitas/dfa-minimizer/raw/master/logo.png" />
</p>

## Installation
Pre-compiled binary packages won't be available. If you want to try the pre-release version of the app, you should compile it yourself by following the instructions below.

### System Dependencies
- Graphviz
- Python 3.5+
- Pip

#### Ubuntu/Debian
Install the direct dependencies with `apt`:
```bash
$ apt install graphviz
```

##### macOS
Use `brew` to install the dependencies:
```bash
$ brew install graphviz
```

### Python Dependencies
```
$ git clone https://github.com/luigifreitas/dfa-minimizer
$ cd dfa-minimizer
$ pip3 install -r requirements.txt
```

## Usage 
You can find examples of DFA on both `example.py` files.

```bash
$ python3 example1.py
$ python3 example1.py
```

#### Declaring a Automata
``` python
dfa.add_state(1) # Adds a new state.
dfa.add_start_state(0) # Add the initial state.
dfa.add_final_state(1) # Add the final state.
dfa.add_symbol('a') # Add a symbol in the alphabet.
dfa.add_transition(1, 'a', 3) # Declare a transition.
```

#### Minimizing
``` python
dfa.minimize()
```

#### Meta
``` python
dfa.print() # Prints a summary about the DFA.
dfa.draw("dfa_after") # Draw the current DFA.
```

## License
This module is distributed under a [GPL-3.0 License](https://github.com/luigifreitas/dfa-minimizer/blob/master/LICENSE).