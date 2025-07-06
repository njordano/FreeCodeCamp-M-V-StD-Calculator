import numpy as np

# Goal: elaborate a calculator that, based on a 3x3 numpy array provides you a dictionary with:

# Variance
# Standard Deviation
# Max
# Min
# Sum

# the resulting dictionary must give (as value) an answer with the following logic:

# Horizontal lines; Vertical lines; Total

# In case of less than 9 numbers being provided, the calculator must raise a ValueError

def calculate(numbers):

# Check if the value provided is valid:

    if ((len(numbers)) < 9):
        raise ValueError('Exactly 9 numbers (int or float) must be provided.') 
    
    elif not all(isinstance(i, (int, float)) for i in numbers):
        raise ValueError('Only float or int, provided in a list, can be accepted.')
    
    else:
        
        numbers = np.array(numbers).reshape(3,3) #Create and shape the array bsed of the list provided

        # Compute the relevant values
        mean = [numbers.mean(axis= 0).tolist(), numbers.mean(axis= 1).tolist(), numbers.mean().tolist()]
        variance = [numbers.var(axis= 0).tolist(), numbers.var(axis= 1).tolist(), numbers.var().tolist()] 
        std = [numbers.std(axis= 0).tolist(), numbers.std(axis= 1).tolist(), numbers.std().tolist()]
        maxi = [numbers.max(axis= 0).tolist(), numbers.max(axis= 1).tolist(), numbers.max().tolist()]
        mini = [numbers.min(axis= 0).tolist(), numbers.min(axis= 1).tolist(), numbers.min().tolist()]
        summ = [numbers.sum(axis= 0).tolist(), numbers.sum(axis= 1).tolist(), numbers.sum().tolist()] 
        #Combine it into a dict
        values = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': maxi,
            'min': mini,
            'sum': summ
            }
        return values
    
calculate([1,2,3,4,5,6,7,8,9])