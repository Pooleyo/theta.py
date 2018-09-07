def run(gsqr_bins, phi_bins, master_bin_list):

    print "Calculating integrated intensity per phi..."

    contributing_phi_bins_list = []

    intensity_integrated_along_phi = []

    for gsqr in gsqr_bins:

        num_phi_bins_at_this_gsqr = 0

        num_empty_phi_bins_at_this_gsqr = 0

        total_gsqr_intensity = 0.0

        for master_bin in master_bin_list:

            if gsqr == master_bin[0]:

                num_phi_bins_at_this_gsqr += 1

                total_gsqr_intensity += master_bin[3]

                if master_bin[3] == 0.0:

                    num_empty_phi_bins_at_this_gsqr += 1

        num_contributing_bins = num_phi_bins_at_this_gsqr - num_empty_phi_bins_at_this_gsqr

        contributing_phi_bins_list.append(num_contributing_bins)

        intensity_integrated_along_phi.append(total_gsqr_intensity)

    phi_per_bin = phi_bins[1] - phi_bins[0]

    integrated_intensity_per_phi = []

    for i in range(len(contributing_phi_bins_list)):

        if contributing_phi_bins_list[i] == 0:

            integrated_intensity_per_phi.append(0.0)

            pass

        else:

            total_phi_contributing_at_this_gsqr = contributing_phi_bins_list[i] * phi_per_bin

            normalised_integrated_intensity = intensity_integrated_along_phi[i] / total_phi_contributing_at_this_gsqr

            integrated_intensity_per_phi.append(normalised_integrated_intensity)

    return integrated_intensity_per_phi
