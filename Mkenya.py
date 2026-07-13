import random

def reservoir_sampling(stream, k):
    reservoir = []
    
    for i, item in enumerate(stream):
        # Step 1 & 2: Fill the reservoir with the first k elements
        if i < k:
            reservoir.append(item)
        else:
            # Step 3: For subsequent elements, pick a random index from 0 to i
            j = random.randint(0, i)
            
            # If the random index falls within the reservoir size, replace it
            if j < k:
                reservoir[j] = item
                
    return reservoir

# Example usage:
data_stream = range(1, 10001) # A stream of 10,000 items
sample_size = 5
print(reservoir_sampling(data_stream, sample_size))