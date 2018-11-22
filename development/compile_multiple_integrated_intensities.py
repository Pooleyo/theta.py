def run(gsqr_bins, phi_bins, image_list):

    import numpy as np
    from copy import deepcopy

    compiled_gsqr = deepcopy(gsqr_bins)

    compiled_integrated_intensity = [0.0] * len(gsqr_bins)

    for iterator, current_image in enumerate(image_list):

        output_folder = "output_" + current_image[:-4]

        integrated_intensity_filename = output_folder + "/integrated_intensity_vs_gsqr.dat"

        current_gsqr, current_integrated_intensity = np.loadtxt(integrated_intensity_filename, delimiter=",", unpack=True)

        if iterator is 0:

            gsqr_counter = np.zeros(np.shape(current_gsqr))

        for i, intensity in enumerate(current_integrated_intensity):

            compiled_integrated_intensity[i] += intensity

            if intensity == min(current_integrated_intensity):

                continue

            else:

                gsqr_counter[i] += 1

    for i, intensity in enumerate(compiled_integrated_intensity):

        if gsqr_counter[i] < 1:

            compiled_integrated_intensity[i] = intensity

        else:

            compiled_integrated_intensity[i] = intensity / gsqr_counter[i]

    return compiled_gsqr, compiled_integrated_intensity
