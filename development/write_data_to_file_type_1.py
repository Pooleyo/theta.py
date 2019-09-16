def run(filename, x, y, output_folder):

    import os

    if os.path.exists(output_folder) is False:

        os.makedirs(output_folder)

    f = open(output_folder + "/" + filename, 'w')

    for i, val in enumerate(x):

        f.write(str(x[i]) + "," + str(y[0][i]) + "\n")
        
    f.close()
    
    return
