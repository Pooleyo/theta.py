def run(im, gsqr, phi):

    import numpy as np

    gsqr_diff = max(gsqr) - min(gsqr)
    width = im.size[0]
    
    width_bin_size = gsqr_diff / width
    phi_diff = max(phi) - min(phi)

    height = im.size[1]

    height_bin_size = phi_diff / height    
    
    new_image_bins = []# This list will contain the theta_phi images' gsqr value at [0], phi value at [1], a list of pixel indices falling into this bin at [2], and the sum of the pixel values currently in this bin at [3].
    
    gsqr_range = np.linspace(min(gsqr), max(gsqr), width)
    
    phi_range = np.linspace(min(phi), max(phi), height)

    for i in range(len(gsqr_range)):
        for j in range(len(phi_range)):

            current_list_value = [gsqr_range[i], phi_range[j], [], [0]]
            new_image_bins.append(current_list_value)

    return gsqr_range, phi_range, new_image_bins, width, height
