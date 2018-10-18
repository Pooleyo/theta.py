def run(gsqr_bins, phi_bins, image_list):

    import numpy as np
    from copy import deepcopy

    compiled_gsqr = deepcopy(gsqr_bins)

    compiled_integrated_intensity = [0.0] * len(gsqr_bins)

    print compiled_gsqr
    print len(compiled_gsqr)
    print compiled_integrated_intensity
    print len(compiled_integrated_intensity)

    for current_image in image_list:

        output_folder = "output_" + current_image[:-4]

        integrated_intensity_filename = output_folder + "/integrated_intensity_vs_gsqr.dat"

        current_gsqr, current_integrated_intensity = np.loadtxt(integrated_intensity_filename, delimiter=",", unpack=True)

        for i, intensity in enumerate(current_integrated_intensity):
            compiled_integrated_intensity[i] += intensity

    return compiled_gsqr, compiled_integrated_intensity