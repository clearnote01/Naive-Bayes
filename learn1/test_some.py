import re
import pickle
import math
class MyDict(dict):
    def __getitem__(self,key):
        if key in self:
            return self.get(key)
        return 0

p1 = MyDict()

tot_p, p = pickle.load(open('naive\\pos_file','rb'))
tot_p, p1 = pickle.load(open('naive\\pos_file','rb'))

print p['sdaff']
print type(p)
print tot_p
print p1['sdaff']
