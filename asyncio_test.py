from multiprocessing import Pool
import numpy as np
def square(x):
    i, d = x
    # calculate the square of the value of x
    return d*d

if __name__ == '__main__':

    # Define the dataset
    dataset = enumerate(np.arange(1, 100))

    # Output the dataset
    print ('Dataset: ' + str(dataset))

    # Run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 5
    chunksize = 3
    with Pool(processes=agents) as pool:
        result = pool.map(square, dataset, chunksize)

    # Output the result
    print ('Result:  ' + str(result))