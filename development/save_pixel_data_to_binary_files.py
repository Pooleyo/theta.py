def run(array_filenames, array_data, list_filenames, list_data, binary_directory):

    import numpy as np
    import pickle
    import os

    if os.path.exists(binary_directory) is True:

        pass

    else:

        os.makedirs(binary_directory)

    for filename, array in zip(array_filenames, array_data):

        np.save(binary_directory + "/" + filename, array)

    for filename, lst in zip(list_filenames, list_data):

        with open(binary_directory + "/" + filename, "wb") as f:

            pickle.dump(lst, f)

    return
