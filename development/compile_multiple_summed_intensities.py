def run(gsqr_bins, image_list):

    import numpy as np
    from copy import deepcopy

    print "Compiling multiple summed intensities..."

    compiled_gsqr = deepcopy(gsqr_bins)

    compiled_summed_intensity = [0.0] * len(gsqr_bins)

    for iterator, current_image in enumerate(image_list):

        output_folder = "output_" + current_image[:-4]

        summed_intensity_filename = output_folder + "/summed_intensity_vs_gsqr.dat"

        current_gsqr, current_summed_intensity = np.loadtxt(summed_intensity_filename, delimiter=",", unpack=True)

        for i, intensity in enumerate(current_summed_intensity):

            compiled_summed_intensity[i] += intensity

    return compiled_gsqr, compiled_summed_intensity
