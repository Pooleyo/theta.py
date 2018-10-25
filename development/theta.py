# This code will unwrap diffraction image plate scans into G^2-phi space.

import in_theta_2 as ip
import work_out_common_results
import calc_plane_from_two_vectors
import loop_through_pixels
import make_bins_for_theta_phi
import populate_theta_phi_bins
import make_image_from_array
import compensate_for_filters
import integrate_along_phi
import make_simple_plot
import write_data_to_file
import compensate_for_sample_attenuation
import compensate_for_polarisation
import make_subpixel_array
import compile_multiple_integrated_intensities

import numpy as np
from skimage import io


def run():

    for k, current_image in enumerate(ip.image_filename):

        ####################################################################################################################
        # The following section opens the image and sets up some data structures that are required for the code to function.

        output_folder = "output_" + current_image[:-4]

        raw_pixel_value = io.imread(current_image)

        working_pixel_value = raw_pixel_value

        subpixel_value = make_subpixel_array.run(working_pixel_value, ip.num_subpixels_height, ip.num_subpixels_width)

        make_image_from_array.run(subpixel_value, "subpixel_image.png", "viridis", "none", output_folder)

        working_pixel_value = subpixel_value

        working_height, working_width = np.shape(working_pixel_value)

        filter_angles_deg = np.empty((working_height, working_width))
        gsqr = np.empty((working_height, working_width))
        phi = np.empty((working_height, working_width))
        attenuation_correction = np.empty((working_height, working_width))
        pixel_value_corrected_for_attenuation = np.empty((working_height, working_width))
        polarisation_angles_deg = np.empty((working_height, working_width))

        vector_origin_to_pixels = [int(0)] * working_height * working_width

        ####################################################################################################################
        # The following section assigns gsqr and phi values to each of the pixels.

        print "Initialised..."

        central_point, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, \
        unit_vector_source_to_origin, adjust_to_centre_of_pixel = work_out_common_results.run(
            working_width, working_height, ip.x_scale[k], ip.y_scale[k], ip.view_x[k], ip.view_y[k], ip.offset[k], ip.normal[k],
            ip.source_position[k])

        phi0_plane_normal = calc_plane_from_two_vectors.run(vector_origin_to_central_pixel, [0.0, 0.0, 1.0])

        print "Calculating gsqr and phi for each pixel..."

        filter_angles_deg, gsqr, phi, vector_origin_to_pixels, polarisation_angles_deg = loop_through_pixels.run(
            working_height, working_width, ip.wavelength, ip.a_lattice, norm_view_x, norm_view_y,
            central_point, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel,
            unit_vector_source_to_origin, adjust_to_centre_of_pixel, phi0_plane_normal, ip.normal[k], filter_angles_deg,
            gsqr, phi, vector_origin_to_pixels, polarisation_angles_deg, working_pixel_value)

        make_image_from_array.run(gsqr, "gsqr_map.png", "viridis", "none", output_folder)

        make_image_from_array.run(phi, "phi_map.png", "viridis", "none", output_folder)

        make_image_from_array.run(filter_angles_deg, "filter_angle_map.png", "viridis", "none", output_folder)

        make_image_from_array.run(polarisation_angles_deg, "polarisation_angle_map.png", "viridis", "none", output_folder)

        ####################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to attenuation by any filters.

        if ip.correct_for_filter_attenuation is True:

            pixel_value_corrected_for_attenuation, attenuation_correction = compensate_for_filters.run(
                working_height, working_width, filter_angles_deg, working_pixel_value, ip.filter_attenuation_length_at_90_deg[k],
                ip.filter_thickness[k], attenuation_correction, pixel_value_corrected_for_attenuation)

            working_pixel_value = pixel_value_corrected_for_attenuation

            make_image_from_array.run(attenuation_correction, "filter_attenuation_correction_map.png", "viridis", "none", output_folder)

        ####################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to sample attenuation.

        if ip.correct_for_sample_attenuation is True:

            pixel_value_corrected_for_sample_attenuation, sample_attenuation_correction = compensate_for_sample_attenuation.run(
                working_pixel_value, ip.sample_normal[k], ip.source_position[k], vector_origin_to_pixels)

            working_pixel_value = pixel_value_corrected_for_sample_attenuation

            make_image_from_array.run(sample_attenuation_correction, "sample_attenuation_correction_map.png", "viridis", "none", output_folder)

        ####################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to polarisation.

        if ip.correct_for_polarisation is True:

            pixel_value_corrected_for_polarisation, polarisation_correction = compensate_for_polarisation.run(
                working_pixel_value, working_height, working_width, polarisation_angles_deg)

            working_pixel_value = pixel_value_corrected_for_polarisation

            make_image_from_array.run(polarisation_correction, "polarisation_correction_map.png", "viridis", "none", output_folder)

        ####################################################################################################################
        # The following section sorts the pixels from the original image into bins according to the gsqr and phi values
        # determined previously.

        gsqr_phi_bins, gsqr_phi_bin_pixel_counter, gsqr_bins, phi_bins = make_bins_for_theta_phi.run(
            ip.num_gsqr_bins, ip.num_phi_bins, ip.gsqr_limit[k], ip.phi_limit[k])

        gsqr_phi_bins, gsqr_phi_bin_pixel_counter, dumped_pixel_counter = populate_theta_phi_bins.run(
            working_width, working_height, gsqr, phi, gsqr_bins, phi_bins, gsqr_phi_bins, gsqr_phi_bin_pixel_counter,
            working_pixel_value, subpixel_value, ip.gsqr_limit[k], ip.phi_limit[k])

        make_image_from_array.run(gsqr_phi_bins, "phi_vs_gsqr.png", "viridis", "none", output_folder)

        ####################################################################################################################
        # The following section integrates along phi.

        intensity_integrated_along_phi, intensity_summed_along_phi = integrate_along_phi.run(
            gsqr_phi_bins, gsqr_phi_bin_pixel_counter)

        make_simple_plot.run(
            gsqr_bins, intensity_integrated_along_phi[0], "c", "$|G^2|$", "Intensity $(arb.)$",
            "Integrated intensity vs. $|G^2|$", "integrated_intensity_vs_phi.png", output_folder)

        make_simple_plot.run(
            gsqr_bins, intensity_summed_along_phi[0], "r", "$|G^2|$", "Intensity $(arb.)$", "Summed intensity vs. $|G^2|$",
            "summed_intensity_vs_phi.png", output_folder)

        write_data_to_file.run("integrated_intensity_vs_gsqr.dat", gsqr_bins, intensity_integrated_along_phi, output_folder)

        write_data_to_file.run("summed_intensity_vs_gsqr.dat", gsqr_bins, intensity_summed_along_phi, output_folder)

        print "Completed image " + str(k) + "..."

        ####################################################################################################################

    output_folder = "output_all"

    gsqr, intensity = compile_multiple_integrated_intensities.run(gsqr_bins, phi_bins, ip.image_filename)

    make_simple_plot.run(
        gsqr, intensity, "c", "$|G^2|$", "Intensity $(arb.)$",
        "Integrated intensity vs. $|G^2|$", "integrated_intensity_vs_phi.png", output_folder)

    print "Finished!"


run()
