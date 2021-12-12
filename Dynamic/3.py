class prob:                                                                 # Backtracking Probability class
    def __init__(self, pr, prev=None):                                      # Constructor
        self.pr = pr                                                        # Probability
        self.prev = prev                                                    # Previous state

class HMM:                                                                  # Hidden Markov Model class
    def __init__(self, p, a, b):                                            # Constructor
        self.p = p                                                          # Initial probability
        self.a = a                                                          # Transition probability
        self.b = b                                                          # Emission probability
        self.all = p.keys()                                                 # All states

speech = HMM(                                                               # Object of HMM
    # Initial Probabilities                                                 --> self.p
    {'au': 0.5, 'to': 0, 'o': 0.5, 'tter': 0, 'mo': 0, 'bile': 0},

    # Transition Probabilities                                              --> self.a
    {
        'au':   {'au': 0, 'to': 1, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},
        'to':   {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 1, 'bile': 0},

        'o':    {'au': 0, 'to': 0, 'o': 0, 'tter': 1, 'mo': 0, 'bile': 0},
        'tter': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},

        'mo':   {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 1},
        'bile': {'au': 0, 'to': 0, 'o': 0, 'tter': 0, 'mo': 0, 'bile': 0},
    },

    # Emission Probabilities                                                --> self.b   
    {
        'au': {
            'sound-au': 0.7,
            'sound-o': 0.3,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'to': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0.7,
            'sound-tter': 0.3,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'o': {
            'sound-au': 0.3,
            'sound-o': 0.7,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'tter': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0.3,
            'sound-tter': 0.7,
            'sound-mo': 0,
            'sound-bile': 0
        },

        'mo': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 1,
            'sound-bile': 0
        },

        'bile': {
            'sound-au': 0,
            'sound-o': 0,
            'sound-to': 0,
            'sound-tter': 0,
            'sound-mo': 0,
            'sound-bile': 1
        }
    }
)

def greedy(hmm, ob):                                                        # Greedy algorithm 
    return [max(hmm.all, key=lambda s: hmm.b[s][z]) for z in ob]

def viterbi(hmm, ob):                                                       # Viterbi algorithm
    grid = [{} for _ in ob]
    for s in hmm.all:                                                       # For each state
        grid[0][s] = prob(hmm.p[s] * hmm.b[s][ob[0]])                       # Take Initial and Emission probabilities, save result to grid

    for t in range(1, len(ob)):                                             # For each time step
        for s in hmm.all:                                                   # For each state
            pos = [(grid[t-1][r].pr * hmm.a[r][s], r) for r in hmm.all]     # Take previous state and Transition probability
            mtp, bps = max(pos, key=lambda x: x[0])                         # Get Maximum Transition probability from best previous state
            grid[t][s] = prob(mtp * hmm.b[s][ob[t]], bps)                   # Calculate Final probability, save to grid with best previous state

    path, l = [], max(hmm.all, key=lambda s: grid[-1][s].pr)                # Get last state and initialize path
    for t in range(len(ob)-1, -1, -1):                                      # For each time step
        path.append(l)                                                      # Add last state to path
        l = grid[t][l].prev                                                 # Get previous state using backtracking
    return reversed(path)                                                   # Return reversed path

samples = [['sound-o', 'sound-tter'],
    ['sound-o', 'sound-tter', 'sound-mo', 'sound-bile']]                    # Samples

for s in samples:                                                       
    print()
    print(f"SAMPLE  :  {' : '.join(s)}")                                    # Name of the sample
    print(f"GREEDY  :  {' : '.join(greedy(speech, s))}")                    # Greedy algorithm output   
    print(f"VITERBI :  {' : '.join(viterbi(speech, s))}")                   # Viterbi algorithm output