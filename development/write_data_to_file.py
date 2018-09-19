def run(filename, x, y):

    import os

    if os.path.exists("output") is False:

        os.makedirs("output")

    f = open("output/" + filename, 'w')

    for i, val in enumerate(x):

        f.write(str(x[i]) + "," + str(y[0][i]) + "\n")
        
    f.close()
    
    return
