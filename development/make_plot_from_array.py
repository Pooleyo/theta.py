def run(image_array, filename, colourmap, interpolation_type, output_folder, use_log_scale):

    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    import os

    print "Building image from array..."

    if os.path.exists(output_folder) is False:

        os.makedirs(output_folder)

    if use_log_scale is True:

        plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type, norm=LogNorm())

    else:

        plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type)

    plt.rcParams.update({'font.size': 17})

    plt.colorbar()

    plt.savefig(output_folder + "/" + filename)

    plt.close()

    return
