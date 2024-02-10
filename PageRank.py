# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)

def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    
    #eVals, eVecs = la.eig(linkMatrix) # Gets the eigenvalues and vectors
    #order = np.absolute(eVals).argsort()[::-1] # Orders them by their eigenvalues
    #eVals = eVals[order]
    #eVecs = eVecs[:,order]
    #r = eVecs[:, 0] # Sets r to be the principal eigenvector
    #100 * np.real(r / np.sum(r)) # Make this eigenvector sum to one, then multiply by 100 Procrastinating Pats
    
    M = d * linkMatrix + (1-d)/n * np.ones([n, n])
    r = 100 * np.ones(n) / n # Sets up this vector (n entries of 1/n × 100 each)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        i += 1
    print(str(i) + " iterations to convergence.")
    r
    return r