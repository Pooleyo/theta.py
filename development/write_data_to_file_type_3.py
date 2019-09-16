def run(filename, x, y, z, output_folder):

    import os

    if os.path.exists(output_folder) is False:

        os.makedirs(output_folder)

    f = open(output_folder + "/" + filename, 'w')

    for i, val in enumerate(x):

        f.write(str(x[i]) + "," + str(y[i]) + "," + str(z[i]) + "\n")
        
    f.close()
    
    return
