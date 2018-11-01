def run(array_filenames, list_filenames, binary_directory):

    import numpy as np
    import pickle

    loaded_data = [0] * (len(list_filenames) + len(array_filenames))

    for i in range(len(array_filenames)):

        loaded_data[i] = np.load(binary_directory + "/" + array_filenames[i] + ".npy")

    for i in range(len(list_filenames)):

        with open(binary_directory + "/" + list_filenames[i]) as f:

            loaded_data[i + len(array_filenames)] = pickle.load(f)

    return loaded_data
