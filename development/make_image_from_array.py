def run(image_array, filename, colourmap, interpolation_type, output_folder):

    import matplotlib.pyplot as plt
    import os

    print "Building image from array..."

    if os.path.exists(output_folder) is False:

        os.makedirs(output_folder)

    plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type)
    plt.colorbar()
    plt.savefig(output_folder + "/" + filename)
    plt.close()

    return
