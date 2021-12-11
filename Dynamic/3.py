class HMM:                                                                  # Hidden Markov Model
    def __init__(self, p, a, b):
        self.p = p                                                          # Initial probability
        self.a = a                                                          # Transition probability
        self.b = b                                                          # Emission probability
        self.all = p.keys()                                                 # All states

speech = HMM(
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

class PathProbabilityWithBackPointer:
    def __init__(self, probability, previous_state=None):
        self.probability = probability
        self.previous_state = previous_state


def greedy(hmm, ob):                                                        # Greedy algorithm 
    return [max(hmm.all, key=lambda s: hmm.b[s][z]) for z in ob]


def viterbi(hmm, ob):                                                       # Viterbi algorithm
    v_grid = [{} for _ in ob]

    for s in hmm.all:
        v_grid[0][s] = PathProbabilityWithBackPointer(
            hmm.p[s] * hmm.b[s][ob[0]]
        )

    for t in range(1, len(ob)):
        for s in hmm.all:
            possible_transition_probabilities = [
                (
                    v_grid[t - 1][r].probability * hmm.a[r][s],
                    r
                )
                for r in hmm.all
            ]

            max_transition_probability, best_previous_state = max(
                possible_transition_probabilities,
                key=lambda probability_and_state: probability_and_state[0]
            )

            v_grid[t][s] = PathProbabilityWithBackPointer(
                max_transition_probability * hmm.b[s][ob[t]],
                best_previous_state
            )

    max_end_state = max(
        hmm.all,
        key=lambda s: v_grid[-1][s].probability
    )

    path_states = []
    last_state = max_end_state
    for t in range(len(ob) - 1, -1, -1):
        path_states.append(last_state)
        last_state = v_grid[t][last_state].previous_state

    path_states.reverse()

    return path_states

samples = [['sound-o', 'sound-tter'],
    ['sound-o', 'sound-tter', 'sound-mo', 'sound-bile']]                    # Samples

for s in samples:                                                       
    print()
    print(f"SAMPLE  :  {'  '.join(s)}")                                     # Sample name
    print(f"GREEDY  :  {'  '.join(greedy(speech, s))}")                     # Greedy algorithm output   
    print(f"VITERBI :  {'  '.join(viterbi(speech, s))}")                    # Viterbi algorithm output