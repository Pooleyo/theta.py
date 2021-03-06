# This code will unwrap diffraction image plate scans into theta-phi space.

# These are all files that contain functions written for this project.
import work_out_common_results
import make_bins_for_theta_phi
import populate_theta_phi_bins
import sum_pixel_values_in_bins
import build_tif_theta_phi_image
import build_png_theta_phi_image
import compensate_for_filters
import sum_along_theta
import plot_integrated_intensity
import write_data_to_file
import calc_theta_phi
import compensate_for_thomson_factor
import make_mask_image
import initialise
import check_image_total_pixel_value
import make_subpixels
import define_phi_0
import compensate_for_sample_attenuation
import sort_data_files
import compile_image_results
import sort_master_files
import calc_integrated_intensity_per_phi

# These modules are standard python modules.
import matplotlib.pyplot as plt
import copy

# This segment determines whether or not test mode is enabled.

from in_theta import test_mode

if test_mode is False:
    import in_theta as ip

elif test_mode is True:
    import t_in_theta as ip


def main():

    # The following value keeps track of whether phi_0 has been defined yet for the transformation. After the first
    # iteration this variable is set to true, which skips the define_phi_0 function.

    occurrence_phi_0_definition = False

    # These lists are collected for checking by pytest.

    all_initial_pixel_value_lists = []
    all_subpixel_lists = []
    all_filter_attenuation_correction_lists = []
    all_sample_attenuation_correction_lists = []
    all_thomson_attenuation_correction_lists = []
    all_final_pixel_values_lists = []
    all_image_bin_lists = []
    all_zeros_list = []

    # The bins must be defined before the images are looped over. This is because the bins must be consistent between
    # different images.
    template_gsqr_bin_list, template_phi_bin_list, template_image_bin_list = \
        make_bins_for_theta_phi.run(
            ip.num_gsqr_bins, ip.num_phi_bins, ip.gsqr_limit, ip.phi_limit, ip.debug)

    for i in range(len(ip.image_files)):

        ######################################
        # This section performs a transformation into theta-phi space.

        im, width, height, pix, initial_pixel_values, initial_total_pixel_value = \
            initialise.run(
                ip.image_files[i], ip.debug, i)

        subpixel_list = []
        """
        pix, subpixel_list, working_width, working_height = \
            make_subpixels.run(
                pix, working_width, working_height, ip.num_width_subpixels, ip.num_height_subpixels, ip.debug)
        """
        central_pixel, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, \
        vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel = \
            work_out_common_results.run(
                width, height, ip.x_scale[i], ip.y_scale[i], ip.view_x[i], ip.view_y[i], ip.offset[i], ip.normal[i],
                ip.source_position[i], ip.debug)

        if occurrence_phi_0_definition is False:
            unit_phi_plane_normal, phi_0_vector = define_phi_0.run(
                ip.source_position[i], ip.phi_0_definer, ip.debug)
            occurrence_phi_0_definition = True

        else:
            unit_phi_plane_normal = unit_phi_plane_normal
            phi_0_vector = phi_0_vector

        filter_angles_list_deg, thomson_angles_list_deg, gsqr, pixel_value, phi, complete_filter_angles_list_deg, \
        complete_thomson_angles_list_deg, complete_gsqr, complete_pixel_value, complete_phi = \
            calc_theta_phi.run(
                width, height, pix, ip.phi_limit, ip.gsqr_limit, ip.wavelength, ip.a_lattice, ip.normal[i], norm_view_x,
                norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel,
                unit_vector_source_to_origin, adjust_to_centre_of_pixel, unit_phi_plane_normal, phi_0_vector, ip.debug)

        ##########################################
        # The following functions apply corrections for thomson polarisation, filter attenuation, and the sample
        # absorption.

        pixel_value, filter_attenuation_correction_factor_list = \
            compensate_for_filters.run(
                filter_angles_list_deg, pixel_value, ip.filter_attenuation_length[i], ip.filter_thickness[i], ip.debug)

        # The thomson_angles_list_deg is the angle from source -> origin -> pixel, and is the same list of angles
        #  required by the sample attenuation correction.
        pixel_value, sample_attenuation_correction_factor_list = \
            compensate_for_sample_attenuation.run(
                thomson_angles_list_deg, pixel_value, ip.source_position[i], ip.sample_normal[i])

        pixel_value, thomson_attenuation_correction_factor_list = \
            compensate_for_thomson_factor.run(
                thomson_angles_list_deg, pixel_value, ip.debug)

        ##########################################
        # This section makes the images of masks for filter and thomson corrections.

        make_mask_image.run(
            "filter_angles_mask.png", "degrees", complete_filter_angles_list_deg, width, height,
            [min(filter_angles_list_deg), max(filter_angles_list_deg)], ip.debug)

        make_mask_image.run(
            "thomson_angles_polarisation_mask.png", "degrees", complete_thomson_angles_list_deg, width, height,
            [min(thomson_angles_list_deg), max(thomson_angles_list_deg)], ip.debug)
            
        all_filter_attenuation_correction_lists.append(filter_attenuation_correction_factor_list)
        all_sample_attenuation_correction_lists.append(sample_attenuation_correction_factor_list)
        all_thomson_attenuation_correction_lists.append(thomson_attenuation_correction_factor_list)

        ############################################
        # This section bins the pixels according to their gsqr-phi values calculated above.

        gsqr_bin_list = copy.deepcopy(template_gsqr_bin_list)
        phi_bin_list = copy.deepcopy(template_phi_bin_list)
        image_bin_list = copy.deepcopy(template_image_bin_list)

        image_bin_list, zeros_list = \
            populate_theta_phi_bins.run(
                gsqr, phi, pixel_value, gsqr_bin_list, phi_bin_list, image_bin_list, ip.debug)

        image_bin_list = \
            sum_pixel_values_in_bins.run(
                image_bin_list, pixel_value, ip.debug)

        gsqr_integrated_intensity = \
            sum_along_theta.run(
                image_bin_list, gsqr_bin_list, phi_bin_list, ip.debug)

        plot_integrated_intensity.run(
            gsqr_bin_list, gsqr_integrated_intensity, ip.name_plot_integrated_intensity, ip.debug)

        write_data_to_file.run(
            "integrated_intensity_vs_gsqr.dat", gsqr_bin_list, gsqr_integrated_intensity, ip.debug)

        build_tif_theta_phi_image.run(
            'normalised_gsqr_vs_phi.tif', image_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
            gsqr_bin_list, phi_bin_list, True, ip.debug)

        build_png_theta_phi_image.run(
            'normalised_gsqr_vs_phi.png', image_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
            gsqr_bin_list, phi_bin_list, True, ip.debug)

        build_tif_theta_phi_image.run(
            'preserved_gsqr_vs_phi.tif', image_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
            gsqr_bin_list, phi_bin_list, False, ip.debug)

        check_image_total_pixel_value.run(
            initial_total_pixel_value, 'preserved_gsqr_vs_phi.tif', ip.debug)

        # TODO Turn this into a function
        if ip.plot is True:
            plt.scatter(gsqr, pixel_value, 1)
            plt.xlabel("$G^2$")
            plt.ylabel("PSL")
            plt.savefig('gsqr_vs_intensity.png')
            plt.close()

        sort_data_files.run(ip.image_files, i)

        all_initial_pixel_value_lists.append(initial_pixel_values)
        all_subpixel_lists.append(subpixel_list)
        all_final_pixel_values_lists.append(pixel_value)
        all_image_bin_lists.append(image_bin_list)
        all_zeros_list.append(zeros_list)

        print "Finished with " + ip.image_files[i] + "\n"

    master_bin_list = \
        copy.deepcopy(
            template_image_bin_list)

    master_bin_list = \
        compile_image_results.run(
            master_bin_list, all_image_bin_lists)

    build_tif_theta_phi_image.run(
        ip.name_plot_master_normalised_gsqr_vs_phi, master_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
        template_gsqr_bin_list, template_phi_bin_list, True, ip.debug)

    build_png_theta_phi_image.run(
        'master_gsqr_vs_phi.png', master_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
        gsqr_bin_list, phi_bin_list, True, ip.debug)

    build_tif_theta_phi_image.run(
        ip.name_plot_master_preserved_gsqr_vs_phi, master_bin_list, ip.num_gsqr_bins, ip.num_phi_bins,
        template_gsqr_bin_list, template_phi_bin_list, False, ip.debug)

    integrated_intensity_per_phi = \
        calc_integrated_intensity_per_phi.run(
            template_gsqr_bin_list, template_phi_bin_list, master_bin_list)

    plot_integrated_intensity.run(
        template_gsqr_bin_list, integrated_intensity_per_phi, ip.name_plot_integrated_intensity_per_phi, ip.debug)

    plot_names = [ip.name_plot_master_normalised_gsqr_vs_phi, ip.name_plot_master_preserved_gsqr_vs_phi, ip.name_plot_integrated_intensity_per_phi, 'master_gsqr_vs_phi.png']

    data_names = ["integrated_intensity_per_phi_vs_gsqr.dat"]

    write_data_to_file.run("integrated_intensity_per_phi_vs_gsqr.dat", template_gsqr_bin_list, integrated_intensity_per_phi, ip.debug)

    sort_master_files.run(plot_names, data_names)

    print "Finished!\n"

    return all_initial_pixel_value_lists, all_subpixel_lists, all_filter_attenuation_correction_lists


main()
