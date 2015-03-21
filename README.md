# **ViterbiAlgorithm_HMMModel**
##Author: Panther (Pavan Yadiki)
* Version: 1.0
* Date of release: March 20, 2015  
* Development Environment:    
	* Language- Python (2.7.3)  
	* Operating System - Windows 8.1  
######**This project is developed during the Machine Learning course study at University of Texas at Dallas**  
###**This project implements a Viterbi algorithm for a given HMM model **  
###**To know more about Viterbi Algorithm, please read http://en.wikipedia.org/wiki/Viterbi_algorithm **  

* Input Format:  
	* A text file that provides details of the HMM Model
		* Number of states in HMM - N
		* Initial probabilities of each state - N values separated by spaces
		* Transition probabilities (N*N values) Separated by spaces
		* Number of observations - M
		* Observation values - M values separated by spaces
		* Observation Probability Matrix -(N*M values)
	* A text file that contains the Test data 
		* Each observation sequence in one line  
	* Sample Input to HMM model is available with title, Input_Model.txt
	* Sample Input to Test data is available with title, Input_Test.txt
		
* Output:  
	* Possible most likely paths for each of the given sequence
	
* Project descriptions file is titled ProjectDescription.pdf

* How to run?
	* Clone the project
	* `python Viterbi.py path_to_model_data path_to_test_data`
	
* Implementation Design Details:
	* ViterbiState.py - Contains a class 'State' which reflects the states of a HMM model. State Class contains the following:  	
		* Transition probability matrix - Defines the prob of moving to other states of a HMM model  
		* Observation Probability matrix - Defines the prob of observing 'o' in a given state  
		* Timestamp - A subclass that is evaluated during the evaluation phase.  
			* Contains the value of delta of a given state and lists the state it has been reached from  
				* Methods to return various parameters of a given state  
		* Two static variables  
			* number_of_states = Holds the number of states of this HMM mode. A list.  
			* number_of_observations = Holds the number of observations possible in this HMM model. A dictionary object  
		* Two static methods  
			* set_observation_values() - Sets the unique observation values of this HMM model  
			* get_observation_values() - Returns the observation values of this HMM model  
	*Viterbi.py - Contains the driver program to build a HMM model for the provided input