import pickle

def save(d, f):                             # Define function to save data
    with open(f, 'wb') as file:             # Open file in write binary mode
        pickle.dump(d, file)                # Dump data into file
    
def load(f):                                # Define function to load data
    with open(f, 'rb') as file:             # Open file in read binary mode
        return pickle.load(file)            # Return data from file

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}        # Sample
save(d, 'file.pickle')                      # Save dictionary to file
new = load('file.pickle')                   # Load dictionary from file
print(new)                                  # Print loaded dictionary