# This code will unwrap diffraction image plate scans into G^2-phi space.

import in_theta_s10260_fit1 as ip
import work_out_common_results
import loop_through_pixels
import make_bins_for_theta_phi
import populate_theta_phi_bins
import make_plot_from_array
import compensate_for_filters
import integrate_along_phi
import make_simple_plot
import write_data_to_file
import write_data_to_file_type_2
import compensate_for_sample_attenuation
import compensate_for_polarisation
import make_subpixel_array
import compile_multiple_integrated_intensities
import save_pixel_data_to_binary_files
import load_pixel_data_from_binary_files
import find_vector_component_in_phi_plane
import compile_multiple_gsqr_vs_phi
import make_tif_from_array
import compensate_for_lorentz_factor
import compensate_for_NIOBIUM_atomic_form_factor
import compile_multiple_summed_intensities

import numpy as np
from skimage import io

def run():

    vector_define_phi0 = [0.0, 0.0, 1.0]

    phi_plane_normal = ip.source_position[0]

    phi0_vector = find_vector_component_in_phi_plane.run(vector_define_phi0, phi_plane_normal)

    all_gsqr_phi_bins = []

    for k, current_image in enumerate(ip.image_filename):

        ################################################################################################################
        # The following section opens the image and sets up some data structures that are required for the code to function.

        output_folder = "output_" + current_image[:-4]

        raw_pixel_value = io.imread(current_image)

        working_pixel_value = raw_pixel_value

        working_pixel_value = np.nan_to_num(working_pixel_value)

        subpixel_value = make_subpixel_array.run(working_pixel_value, ip.num_subpixels_height, ip.num_subpixels_width)

        make_plot_from_array.run(subpixel_value, "subpixel_image.png", "viridis", "none", output_folder, False)

        make_plot_from_array.run(subpixel_value, "subpixel_image_log.png", "viridis", "none", output_folder, True)

        working_pixel_value = subpixel_value

        working_height, working_width = np.shape(working_pixel_value)

        filter_angles_deg = np.empty((working_height, working_width))
        gsqr = np.empty((working_height, working_width))
        phi = np.empty((working_height, working_width))
        attenuation_correction = np.empty((working_height, working_width))
        pixel_value_corrected_for_attenuation = np.empty((working_height, working_width))
        polarisation_angles_deg = np.empty((working_height, working_width))
        bragg_angles_deg = np.empty((working_height, working_width))
        vector_origin_to_pixels = [int(0)] * working_height * working_width

        ################################################################################################################
        # The following section assigns gsqr and phi values to each of the pixels.

        print "Initialised..."

        central_point, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, \
        unit_vector_source_to_origin, adjust_to_centre_of_pixel = work_out_common_results.run(
            working_width, working_height, ip.x_scale[k], ip.y_scale[k], ip.view_x[k], ip.view_y[k], ip.offset[k], ip.normal[k],
            ip.source_position[k])

        binary_directory = "binaries/" + output_folder

        array_data_filenames = ["filter_angles", "gsqr", "phi", "polarisation_angles"]

        array_data_list = [filter_angles_deg, gsqr, phi, polarisation_angles_deg]

        list_data_filenames = ["vector_origin_to_pixels"]

        list_data = [vector_origin_to_pixels]

        if ip.use_previous_pixel_loop is False:

            print "Calculating values for each pixel..."

            filter_angles_deg, gsqr, phi, vector_origin_to_pixels, polarisation_angles_deg, bragg_angles_deg = \
                loop_through_pixels.run(
                working_height, working_width, ip.wavelength, ip.a_lattice, norm_view_x, norm_view_y,
                central_point, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel,
                unit_vector_source_to_origin, adjust_to_centre_of_pixel, phi_plane_normal, ip.normal[k], filter_angles_deg,
                gsqr, phi, vector_origin_to_pixels, polarisation_angles_deg, phi0_vector, bragg_angles_deg)

            save_pixel_data_to_binary_files.run(array_data_filenames, array_data_list, list_data_filenames, list_data,
                                                binary_directory)
        else:

            print "Loading values for each pixel..."

            filter_angles_deg, gsqr, phi, polarisation_angles_deg, vector_origin_to_pixels = \
                load_pixel_data_from_binary_files.run(array_data_filenames, list_data_filenames, binary_directory)

        make_plot_from_array.run(gsqr, "gsqr_map.png", "viridis", "none", output_folder, False)

        make_plot_from_array.run(phi, "phi_map.png", "viridis", "none", output_folder, False)

        make_plot_from_array.run(filter_angles_deg, "filter_angle_map.png", "viridis", "none", output_folder, False)

        make_plot_from_array.run(polarisation_angles_deg, "polarisation_angle_map.png", "viridis", "none",
                                 output_folder, False)

        make_plot_from_array.run(bragg_angles_deg, "bragg_angle_map.png", "viridis", "none",
                                 output_folder, False)

        ################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to attenuation by any filters.

        if ip.correct_for_filter_attenuation is True:

            pixel_value_corrected_for_attenuation, attenuation_correction = compensate_for_filters.run(
                working_height, working_width, filter_angles_deg, working_pixel_value, ip.filter_attenuation_length_at_90_deg[k],
                ip.filter_thickness[k], attenuation_correction, pixel_value_corrected_for_attenuation)
            working_pixel_value = pixel_value_corrected_for_attenuation

            make_plot_from_array.run(attenuation_correction, "filter_attenuation_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to sample attenuation.

        if ip.correct_for_sample_attenuation is True:

            pixel_value_corrected_for_sample_attenuation, sample_attenuation_correction = compensate_for_sample_attenuation.run(
                working_pixel_value, ip.sample_normal[k], ip.source_position[k], vector_origin_to_pixels)

            working_pixel_value = pixel_value_corrected_for_sample_attenuation

            make_plot_from_array.run(sample_attenuation_correction, "sample_attenuation_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to polarisation.

        if ip.correct_for_polarisation is True:

            pixel_value_corrected_for_polarisation, polarisation_correction = compensate_for_polarisation.run(
                working_pixel_value, working_height, working_width, polarisation_angles_deg)

            working_pixel_value = pixel_value_corrected_for_polarisation

            make_plot_from_array.run(polarisation_correction, "polarisation_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to the lorentz factor.

        if ip.correct_for_lorentz_factor is True:

            pixel_value_corrected_for_lorentz_factor, lorentz_correction = compensate_for_lorentz_factor.run(
                working_pixel_value, working_height, working_width, bragg_angles_deg)

            working_pixel_value = pixel_value_corrected_for_lorentz_factor

            make_plot_from_array.run(lorentz_correction, "lorentz_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # The following section applies a correction to the intensity for each pixel due to the lorentz factor.

        if ip.correct_for_atomic_form_factor is True:

            pixel_value_corrected_for_atomic_form_factor, atomic_form_factor_correction = compensate_for_NIOBIUM_atomic_form_factor.run(
                working_pixel_value, working_height, working_width, bragg_angles_deg, output_folder, ip.wavelength)

            working_pixel_value = pixel_value_corrected_for_atomic_form_factor

            make_plot_from_array.run(atomic_form_factor_correction, "atomic_form_factor_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # This section makes an image with all the applied corrections.

        make_tif_from_array.run(working_pixel_value, "corrections_applied_" + current_image, output_folder)

        total_correction_array = np.ones((working_height, working_width))

        if ip.correct_for_filter_attenuation is True:

            total_correction_array *= attenuation_correction

        if ip.correct_for_sample_attenuation is True:

            total_correction_array *= sample_attenuation_correction

        if ip.correct_for_polarisation is True:

            total_correction_array *= polarisation_correction

        if ip.correct_for_lorentz_factor is True:

            total_correction_array *= lorentz_correction

        if ip.correct_for_atomic_form_factor is True:

            total_correction_array *= atomic_form_factor_correction

        make_tif_from_array.run(total_correction_array, "total_corrections.tif", output_folder)

        #make_plot_from_array.run(total_correction_array, "total_correction_map.png", "viridis", "none", output_folder, False)

        ################################################################################################################
        # The following section sorts the pixels from the original image into bins according to the gsqr and phi values
        # determined previously.

        gsqr_phi_bins, gsqr_phi_bin_pixel_counter, gsqr_bins, phi_bins = make_bins_for_theta_phi.run(
            ip.num_gsqr_bins, ip.num_phi_bins, ip.gsqr_limit[k], ip.phi_limit[k])

        gsqr_phi_bins, gsqr_phi_bin_pixel_counter, dumped_pixel_counter = populate_theta_phi_bins.run(
            working_width, working_height, gsqr, phi, gsqr_bins, phi_bins, gsqr_phi_bins, gsqr_phi_bin_pixel_counter,
            working_pixel_value, subpixel_value, ip.gsqr_limit[k], ip.phi_limit[k])

        all_gsqr_phi_bins.append(gsqr_phi_bins)

        make_plot_from_array.run(gsqr_phi_bins, "phi_vs_gsqr.png", "viridis", "none", output_folder, False)
        make_plot_from_array.run(gsqr_phi_bins, "phi_vs_gsqr_log.png", "viridis", "none", output_folder, True)

        ################################################################################################################
        # The following section integrates along phi.

        intensity_integrated_along_phi, intensity_summed_along_phi = integrate_along_phi.run(
            gsqr_phi_bins, gsqr_phi_bin_pixel_counter, ip.minimum_pixels_in_gsqr_bin)

        make_simple_plot.run(
            gsqr_bins, intensity_integrated_along_phi[0], "c", "$|G^2|$", "Intensity $(arb.)$",
            "Integrated intensity vs. $|G^2|$", "integrated_intensity_vs_gsqr.png", output_folder)

        make_simple_plot.run(
            gsqr_bins, intensity_summed_along_phi[0], "r", "$|G^2|$", "Intensity $(arb.)$", "Summed intensity vs. $|G^2|$",
            "summed_intensity_vs_gsqr.png", output_folder)

        write_data_to_file.run("integrated_intensity_vs_gsqr.dat", gsqr_bins, intensity_integrated_along_phi, output_folder)

        write_data_to_file.run("summed_intensity_vs_gsqr.dat", gsqr_bins, intensity_summed_along_phi, output_folder)

        print "Completed image " + str(k) + "..."

        ################################################################################################################

    output_folder = "output_all"

    gsqr, integrated_intensity = compile_multiple_integrated_intensities.run(gsqr_bins, phi_bins, ip.image_filename)

    gsqr, summed_intensity = compile_multiple_summed_intensities.run(gsqr_bins, ip.image_filename)

    master_gsqr_phi_bins = compile_multiple_gsqr_vs_phi.run(all_gsqr_phi_bins)

    make_simple_plot.run(
        gsqr, integrated_intensity, "c", "$|G^2|$", "Intensity $(arb.)$",
        "Integrated intensity vs. $|G^2|$", "integrated_intensity_vs_gsqr.png", output_folder)

    make_simple_plot.run(
        gsqr, summed_intensity, "c", "$|G^2|$", "Summed Intensity $(arb.)$",
        "Summed intensity vs. $|G^2|$", "summed_intensity_vs_gsqr.png", output_folder)

    write_data_to_file_type_2.run("integrated_intensity_vs_gsqr.dat", gsqr, integrated_intensity, output_folder)

    write_data_to_file_type_2.run("summed_intensity_vs_gsqr.dat", gsqr, summed_intensity, output_folder)

    make_plot_from_array.run(master_gsqr_phi_bins, "phi_vs_gsqr.png", "viridis", "none", output_folder, False)

    make_plot_from_array.run(master_gsqr_phi_bins, "phi_vs_gsqr_log.png", "viridis", "none", output_folder, True)

    print "Finished!"


run()
