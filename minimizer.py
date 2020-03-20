import networkx as nx
from graphviz import Source

class DFA:

    def __init__(self):
        self.states = set()
        self.start_state = 0
        self.final_states = set()
        self.transitions = {}
        self.alphabet = set()

    def add_state(self, state):
        self.states.add(state)

    def add_start_state(self, state):
        self.start_state = state

    def add_final_state(self, state):
        self.final_states.add(state)

    def add_symbol(self, symbol):
        self.alphabet.add(symbol)

    def add_transition(self, f_state, symbol, t_state):
        if f_state not in self.transitions:
            self.transitions.update({f_state: {}})

        if t_state not in self.transitions[f_state]:
            self.transitions[f_state].update({t_state: set()})

        self.transitions[f_state][t_state].add(symbol)

    def print(self):
        print("States:", self.states)
        print("Start State:", self.start_state)
        print("Final States:", self.final_states)
        print("Transitions:", self.transitions)
        print("Alphabet:", self.alphabet)

    def draw(self, filename=None):
        G = nx.DiGraph()

        for i in self.states:
            s = 'doublecircle' if i in self.final_states else 'circle'
            f = 'grey' if i == self.start_state else 'white'
            G.add_node(i, shape=s, fillcolor=f, style='filled')

        for i, d in self.transitions.items():
            for k, v in d.items():
                l = ','.join(v)
                G.add_edge(i, k, label=l)

        plot = Source(nx.drawing.nx_agraph.to_agraph(G))

        if not filename:
            return plot

        plot.render(filename, format='png')    

    def hopcroft(self):
        P = [ self.final_states, self.states.difference(self.final_states) ]
        W = [ self.final_states ]

        while len(W) > 0:
            A = W.pop()
            
            for c in self.alphabet:
                X = set()
                for f_state, t_state in self.transitions.items():
                    for k, s in t_state.items():
                        if c in s and k in A:
                            X.update(set([f_state]))

                for Y in P:
                    if X.intersection(Y) != set() and Y.difference(X) != set():
                        P.append(X.intersection(Y))
                        P.append(Y.difference(X))
                        P.remove(Y)

                        if Y in W:
                            W.append(X.intersection(Y))
                            W.append(Y.difference(X))
                            W.remove(Y)
                        else:
                            if len(X.intersection(Y)) <= len(Y.difference(X)):
                                W.append(X.intersection(Y))
                            else:
                                W.append(Y.difference(X))

        return P

    def minimize(self):
        min_states = self.hopcroft()

        for state_set in min_states:
            if len(state_set) > 1:
                min_state = min(state_set)

                for state in state_set:
                    self.transitions[min_state].update(self.transitions[state])
                    if state != min_state:
                        self.transitions.pop(state)
                        self.states.discard(state)

                changes = []
                for s, _ in self.transitions.items():
                    for t, _ in self.transitions[s].items():
                        if t in state_set and t != min_state:
                            changes.append((t, s))
                
                for t, s in changes:
                    self.transitions[s][min_state] = self.transitions[s].pop(t)

                if self.start_state in state_set:
                    self.start_state = min_state
                
                changes = []
                for fs in self.final_states:
                    if fs in state_set:
                        changes.append(fs)

                for s in changes:
                    self.final_states.discard(fs)
