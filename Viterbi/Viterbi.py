from __future__ import print_function
__author__ = 'Panther'
__version__ = 1.0
__email__ = 'mail2pavanyr@gmail.com'

import sys
import ViterbiState
# Read the input file and initialize the required number of states
# Pass the state transition and observational values


class Viterbi:

    def __init__(self):
        self.state_list = []
        self.sequence = []
        self.sequence_length = []
        return

    def read_input(self, file_path):
        try:
            with open(file_path, "r") as input_file:
                return self.define_states(input_file)
        except IOError:
            print('Error in reading the file')
            exit(1)


    def define_states(self, input_file):
        n = int(input_file.next())  # Find the number of states
        ViterbiState.State.number_of_states = n
        self.state_list = [ViterbiState.State('S'+str(_)) for _ in xrange(n+1)]
        self.state_list[0] = None  # Start the states from 1
        i = 1
        for p in input_file.next().strip('\n').split():  # Assign the initial probabilities of each state
            self.state_list[i].set_initial_prob(p)
            i += 1

        prob = input_file.next().strip('\n').split()
        index = 0
        for states in self.state_list[1:]:  # Assign transition values to each state
            for transition in xrange(1, n + 1):
                states.set_transition_to(transition, float(prob[index]))  # Set the transition value
                index += 1

        o = int(input_file.next())  # Read number of observations
        for char in input_file.next().strip('\n').split():  # Read the values of observations
            ViterbiState.State.set_observation_values(char)

        observations = ViterbiState.State.get_observation_values()
        index = 0
        observation_prob = input_file.next().strip('\n').split()
        for states in self.state_list[1:]:  # Read the observation matrix of each state
            for key in observations:
                states.set_observation(key, observation_prob[index])
                index += 1

        return self.state_list

    @staticmethod
    def visit(path):
        for p in path:
            print(p, end=' -> ')
        print(' End\n')

    def trace_path(self, state, path, tick_covered):
        if tick_covered == 0:
            Viterbi.visit(path)
            return

        for each in state:
            path[tick_covered - 1] = each.__str__()
            self.trace_path(each.get_prev_state(tick_covered), path, tick_covered - 1)

    def print_path(self):
        # Get the list of deltas of last timestamps of each state
        last_timestamp = [states.get_delta(self.sequence_length) for states in self.state_list[1:]]
        max_delta = reduce(lambda x1, x2: max(x1, x2), last_timestamp)  # Find the max. delta of all the last states
        last_state = []
        for t, index in zip(last_timestamp, xrange(1, len(self.state_list) + 1)):
            if max_delta == t:
                last_state.append(self.state_list[index])  # Identify the states that has the largest timestamp

        # Trace the most likely path
        self.trace_path(last_state, ['']*self.sequence_length, self.sequence_length)


    def find_most_likely_path(self, sequence):
        self.sequence = sequence.strip('\n').split()
        self.sequence_length = len(self.sequence)
        [states.set_delta1(self.sequence[0]) for states in self.state_list[1:]]  # Find the initial deltas of each state

        if self.sequence_length > 1:  # Continue if # of observations is more than 1
            # For each observation
            for observation, timestamp in zip(self.sequence[1:], xrange(2, self.sequence_length + 1)):
                for state1, index1 in zip(self.state_list[1:], xrange(1, len(self.state_list) + 1)):  # For each state
                    o = state1.get_observation(observation)  # Find the observation prob of this state
                    prev_state = []
                    max_delta = -1
                    # find the best prev. state
                    for state2, index2 in zip(self.state_list[1:], xrange(1, len(self.state_list) + 1)):
                        delta = state2.get_transition_to(index1)  # Get the transition prob.
                        delta *= state2.get_delta(timestamp - 1)  # Get the delta of the state at previous timestamp
                        if delta > max_delta:  # Check if this is the best state seen so far
                            prev_state = []
                            prev_state.append(state2)
                            max_delta = delta
                        elif delta == max_delta:  # More than one best state is possible
                            prev_state.append(state2)

                    state1.set_delta(max_delta * o, prev_state)  # Set the delta for this state
        self.print_path()
        [states.reset_delta() for states in self.state_list[1:]]  # Reset the delta of each state
        self.sequence = []
        self.sequence_length = []


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Please the path to locate the HMM model data and the test data')
        raise IOError

    try:
        v = Viterbi()
        v.read_input(sys.argv[1])  # Read the HMM model data and initialize the required # of states and its values
        with open(sys.argv[2], 'r') as test_file:
            for s in test_file:
                v.find_most_likely_path(s)
    except IOError:
        print('Path to training data is incorrect. Please give the correct path. ' + str(sys.argv[1]))