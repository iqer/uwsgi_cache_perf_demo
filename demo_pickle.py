import pickle

filename = 'data.pkl'

with open(filename, 'rb') as f:
    obj = pickle.load(f)

print(obj)