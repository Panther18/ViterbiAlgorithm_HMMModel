# ViterbiAlgorithm_HMMModel
This projects implements a Viterbi algorithm for a given HMM model.
To know more about Viterbi Algorithm, please read http://en.wikipedia.org/wiki/Viterbi_algorithm
For a given observation sequence, this program outputs all the possible most likely paths.

Design:
Two python files.\n
ViterbiState.py
  This python file has the class called 'State'
  This reflects the state of a HMM model
  Each State has the following:
    -Transition probability matrix - Defines the prob of moving to other states of a HMM model
    -Observation Probability matrix - Defines the prob of observing 'o' in a given state
    -Timestamp - A subclass that is evaluated during the evaluation phase.
        -Contains the value of delta of a given state and lists the state it has been reached from
    -Methods to return various parameters of a given state
    -Two static variables
      -number_of_states = Holds the number of states of this HMM mode. A list.
      -number_of_observations = Holds the number of observations possible in this HMM model. A dictionary object
    -Two static methods
      -set_observation_values() - Sets the unique observation values of this HMM model
      -get_observation_values() - Returns the observation values of this HMM model
Input:
  A text file which provides details about the HMM model
  A test file 
