# svm.py
# -------------

# svm implementation
import util
from sklearn import svm as Svm
PRINT = True

class SVMClassifier:
  """
  svm classifier
  """
  def __init__( self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "svm"
    self.svmmodel = Svm.SVC(kernel='linear', c=1, gamma=1)

  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    print "Starting iteration ",  "..."
    for i in range(len(trainingData)):
        "*** YOUR CODE HERE ***"
        

        util.raiseNotDefined()
    
  def classify(self, data ):
    guesses = []
    for datum in data:
      # fill predictions in the guesses list
      "*** YOUR CODE HERE ***"
      self.svmmodel.fit(data,self.legalLabels)
      self.svmmodel.score(data,self.legalLabels)
      guesses = self.svmmodel.predict(data)
      util.raiseNotDefined()
      
    return guesses

