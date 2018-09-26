def run(image_array, filename, colourmap, interpolation_type):

    import matplotlib.pyplot as plt
    import os

    print "Building image from array..."

    if os.path.exists("output") is False:

        os.makedirs("output")

    plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type)
    plt.colorbar()
    plt.savefig("output/" + filename)
    plt.close()

    return
