def run(all_gsqr_phi_bins):

    import numpy as np

    print all_gsqr_phi_bins
    height, width = np.shape(all_gsqr_phi_bins[0])
    print height
    print width
    master_gsqr_phi_bins = np.zeros((height, width))
    pixel_counter = np.zeros((height, width))
    print master_gsqr_phi_bins

    for i, gsqr_phi_bins in enumerate(all_gsqr_phi_bins):

        for col in range(height):

            for row in range(width):

                master_gsqr_phi_bins[col][row] += gsqr_phi_bins[col][row]

                if gsqr_phi_bins[col][row] > 0.0:

                    pixel_counter[col][row] += 1

    for col in range(height):

        for row in range(width):

            if pixel_counter[col][row] < 1.0:

                master_gsqr_phi_bins[col][row] = master_gsqr_phi_bins[col][row]

            else:

                master_gsqr_phi_bins[col][row] = master_gsqr_phi_bins[col][row] / pixel_counter[col][row]

    return master_gsqr_phi_bins