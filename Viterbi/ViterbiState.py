__author__ = 'Panther'
"""
This class defines the state of a HMM model
Each state contains:
    -Transition probability matrix - Defines the prob of moving to other states of a HMM model
    -Observation Probability matrix - Defines the prob of observing 'o' in a given state
    -Timestamp - A subclass that is evaluated during the evaluation phase.
        -Contains the value of delta of a given state and lists the state it has been reached from
    -Methods to return various parameters of a given state
"""

class State:
    number_of_states = 0  # Number of states in this HMM model
    unique_observations = {}  # Number of unique observations in this model

    class Timestamp:  # Subclass used during the evaluation phase

        def __init__(self, delta, prev_state=None):
            self.prev_state = prev_state  # Previous state this has been reached from
            self.delta = delta  # Value of the delta at this timestamp

    def __init__(self, name):
        self.name = name  # Name of this state
        self.transition = []  # Transition prob of this matrix
        self.transition.append(0)  # Let the states start from 1
        self.observation = {}  # Observation prob of a state. It is a dictionary
        self.initial_value = 0  # Initial probability of this state
        self.timestamp = []  # List of timestamps used during the evaluation phase
        self.timestamp.append(None)  # Timestamp starts from 1

    def __str__(self):
        return self.name  # Returns the name of this state

    """
    Returns the transitional prob to a given state from this state
    """
    def get_transition_to(self, other_state):
        return self.transition[int(other_state)]

    """
    Assigns the transitional prob to a given state from this state
    """
    def set_transition_to(self, other_state, value):
        self.transition.append(float(value))
    """
    Returns the observational prob of o in this state
    """
    def get_observation(self, o):
        return self.observation[o]

    """
    Sets the observational prob of o of this state
    """
    def set_observation(self, key, value):
        self.observation[key] = float(value)
        return
    """
    Sets the initial prob of this state
    """
    def set_initial_prob(self, value):
        self.initial_value = float(value)

    """
    Returns the initial prob of this state
    """
    def get_initial_prob(self):
        return self.initial_value

    """
    Sets the delta of this state for a given timestamp
    """
    def set_delta(self, delta, prev_state):
        self.timestamp.append(State.Timestamp(delta, prev_state))
    """
    Sets the delta of this state for timestamp=1
    """
    def set_delta1(self, o):
        self.timestamp.append((State.Timestamp(float(self.initial_value * self.observation[o]), None)))

    """
    Returns the delta of this state for a given timestamp
    """
    def get_delta(self, tick):
        if len(self.timestamp) >= tick:
            try:
                return self.timestamp[tick].delta
            except:
                print()
    """
    Returns the prev state of this state for a given timestamp
    """
    def get_prev_state(self, tick):
        if(len(self.timestamp) >= tick):
            return self.timestamp[tick].prev_state
    """
    Resets the timestamp to None. Usually done before the start/end of the evaluation phase
    """
    def reset_delta(self):
        self.timestamp = []
        self.timestamp.append(None)

    @staticmethod
    def set_observation_values(key):
        State.unique_observations[key] = len(State.unique_observations)

    @staticmethod
    def get_observation_values():
        return State.unique_observations.keys()