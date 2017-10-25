# perceptron.py
# -------------

# Perceptron implementation
import util
PRINT = True

class PerceptronClassifier:
  """
  Perceptron classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  '''
   w_: 1d arry 
     weights after fitting
   errors: list
     Number of miscalssification in every epoch
   '''
  def __init__( self, legalLabels, max_iterations):
    self.legalLabels = legalLabels
    self.type = "perceptron"
    self.max_iterations = max_iterations
    self.weights = {}
    for label in legalLabels: # for each legal label, e.g.,temperature... or nope
      # The weight for each label, meaning............
      self.weights[label] = util.Counter() # this is the data-structure you should use

  def setWeights(self, weights):
    assert len(weights) == len(self.legalLabels);
    self.weights = weights;

  # trainingData as X = {[pixels], [0 or 1]}, trainingLabels as y', validationData as x, validationLabels as y


  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    '''

    :param trainingData: {dictionary-like}, shape = [n_samples, n_features]
        Training vectors, where 'n_sample' is the number of samples and 'n_features' is the number of features.
    :param trainingLabels: {array-like}, shape = [n_samples]
        Target values y.
    :param validationData:
    :param validationLabels:
    :return: self: object
    '''
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details. 
    
    Use the provided self.weights[label] data structure so that 
    the classify method works correctly. Also, recall that a
    datum is a counter from features to values for those features
    (and thus represents a vector of values).
    """
    
    self.features = trainingData[0].keys() # could be useful later
    # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING

    # each error = y' - y initialization
    self.errors = []
    for iteration in range(self.max_iterations):
      print "Starting iteration ", iteration, "..."
      # for each piece of training data, we need to calculate the score of (x,y)
      # initialize score
      score = 1
      for i in range(len(trainingData)):
        "*** YOUR CODE HERE ***"

        #self.weights[i] *= trainingData[i]
        validationData = self.classify(trainingData)
      for datum in validationData:
        self.weights[i] += trainingData[i]

        util.raiseNotDefined()
    return self

# for i in xrange(n):
#  x, expected = choice(training_data)
# result = dot(w, x)
# error = expected - unit_step(result)
#errors.append(error)
#w += eta * error * x
    
  def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    
    Recall that a datum is a dictionary of location to value (0 or 1)...
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
    return guesses

  
  def findHighWeightFeatures(self, label):
    """
    Returns a list of the 100 features with the greatest weight for some label
    """
    featuresWeights = []

    "*** YOUR CODE HERE ***"
    for i in range(0,100):
      pass

    util.raiseNotDefined()

    return featuresWeights

