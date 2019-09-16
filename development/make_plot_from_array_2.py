def run(image_array, filename, colourmap, interpolation_type, output_folder, use_log_scale, extent):

    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm
    import os

    print "Building image from array..."

    if os.path.exists(output_folder) is False:

        os.makedirs(output_folder)

    if use_log_scale is True:

        plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type, norm=LogNorm(), extent=extent, aspect='auto')

    else:

        plt.imshow(image_array, cmap=colourmap, interpolation=interpolation_type, extent=extent, aspect='auto')

    plt.xlabel('$|G^2|$')
    plt.ylabel('$\phi$ (degrees)')

    plt.rcParams.update({'font.size': 15})

    plt.colorbar()

    plt.savefig(output_folder + "/" + filename)

    plt.close()

    return
