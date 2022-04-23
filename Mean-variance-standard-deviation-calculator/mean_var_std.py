import numpy as np

def calculate(list):
  
  try:
    l = np.array(list).reshape(3, 3)
    
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  
  lmean = [l.mean(axis=0).tolist(), l.mean(axis=1).tolist() ,l.mean()]
  lvar = [l.var(axis=0).tolist(), l.var(axis=1).tolist(), l.var()]
  lstd = [l.std(axis=0).tolist(), l.std(axis=1).tolist(), l.std()]
  lmax = [l.max(axis=0).tolist(), l.max(axis=1).tolist(), l.max()]
  lmin = [l.min(axis=0).tolist(), l.min(axis=1).tolist(), l.min()]
  lsum = [l.sum(axis=0).tolist(), l.sum(axis=1).tolist(), l.sum()]

  calculations = {
    'mean': lmean,
    'variance': lvar,
    'standard deviation': lstd,
    'max': lmax,
    'min': lmin,
    'sum': lsum
  }
  
  return calculations