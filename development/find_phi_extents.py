def run(master_bins, phi_bins, gsqr_bins):

    import numpy as np

    print "Finiding phi populations..."

    gsqr_bin_shape = np.shape(gsqr_bins)

    min_phi = np.zeros(gsqr_bin_shape)
    max_phi = np.zeros(gsqr_bin_shape)

    rows, cols = np.shape(master_bins)

    for i in range(cols):

        col = master_bins[:, i]

        populated_col = np.nonzero(col)

        if np.size(populated_col) <= 1:

            continue

        else:

            min_phi_ind = np.min(populated_col)
            max_phi_ind = np.max(populated_col)

            min_phi[i] = phi_bins[min_phi_ind]
            max_phi[i] = phi_bins[max_phi_ind]


    return min_phi, max_phi