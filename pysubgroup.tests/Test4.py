import cProfile
import heapq
import time

import SGDUtils
from Selectors import NominalSelector
import SubgroupDiscoveryTask, Selectors, BSD, SimpleDFS
import numpy as np
import pandas as pd


# Create some data
d = np.array([[1, 'test', 'true', 2], \
               [2, 'test2', 'true', 5], \
               [5, 'test', 'False', 1], \
               [3, 'test', 'False', 100]])
df = pd.DataFrame(d)
df.columns = ['intTest', 'strTest', 'trg', 'weights']

df['intTest'] = df['intTest'].astype(int)
df['weights'] = df['weights'].astype(int)
data = df.to_records(False, True)

# print meta['class']
target = NominalSelector ('trg', 'False')

# sel2 = NominalSelector ('checking_status', 'no checking')

# sg = Subgroup(NominalSelector ('class', "bad"), [NominalSelector ('checking_status', "'no checking'")])
# qf = WRAccQF()
# print qf.evaluateFromDataset(data, sg)
# print sel.covers(data[0])
# print sum(1 for i in data if sel.covers(i))


print (type(target.covers(data)))
# print WRAccQF().evaluateFromDataset(data, Subgroup(target, []))