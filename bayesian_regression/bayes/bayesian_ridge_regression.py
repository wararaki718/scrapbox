'''
code sample
https://nbviewer.jupyter.org/github/amber-kshz/PRML/blob/master/notebooks/LinReg_Bayes.ipynb
'''

import numpy as np


class BayesianRidgeRegression:
    
    def __init__(self, alpha=1.0, beta=1.0):
        self.alpha = alpha
        self.beta = beta
        self.m = None # posterior mean
        self.s = None # posterior covariancematrix

    def calc_posterior_param(self, phi, t):
        '''
        this method calculates posterior mean and covariance matrix from the training data phi and t.

        params
        phi: 2-d numpy array
             (n, m) array, representing desing matrix
        t: 1-d numpy array
             (N,) array, respresenting target values
        '''
        self.s = np.linalg.inv(self.alpha*np.identity(len(phi[0])) + self.beta*phi.T@phi)
        self.m = self.beta*(self.s@phi.T@t)

    def predict(self, phi, return_std=False):
        '''
        this method makes prediction on the input phi, and returns predictive mean (and standard devision)

        params
        phi: 2-d numpy array
             (N_test, M) numpy array. M must be equal to "M" (the length in the second dimension) of the training data.
        return_std: boolean, default False
                    if true, the method also returns predictive standard devision
        
        returns
        pred_mean: 1-d numpy array
                   (N_test,) numpy array representing predictive mean
        pred_std: 1-d numpy array
                   (N_test,) numpy array representing predictive standard scaler
        '''
        pred_mean = phi @ self.m
        if return_std:
            pred_std = np.sqrt(1.0/self.beta + np.diag(phi@self.s@phi.T))
            return pred_mean, pred_std
        
        return pred_mean

    def calc_evidence(self, phi, t):
        '''
        This method calculates the evidence with respect to the data phi and t

        param
        phi: 2-d numpy array
             (N, M) array, representing design matrix
        t : 1-d numpy array
            (N,) array, representing target values
        
        return
        evidence: float
        '''
        n, m = np.shape(phi)
        evidence = 0.5*m*np.log(self.alpha) + 0.5*n*np.log(self.beta) \
            - 0.5*self.beta*np.linalg.norm(t - phi@self.m)**2 - 0.5*self.alpha*(self.m@self.m) \
            - 0.5*np.log(np.linalg.det(self.alpha*np.identity(M) + self.beta*phi.T@phi)) \
            - 0.5*n*np.log(2*np.pi)
        return evidence
