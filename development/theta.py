# This code will unwrap diffraction image plate scans into theta-phi space.

import in_theta as ip
import work_out_common_results
import give_gsqr_value
import calc_plane_from_two_vectors
import calc_angle_between_vectors
import make_theta_phi_plot
import build_image_skeleton
import make_bins_for_theta_phi
import populate_theta_phi_bins
import sum_pixel_values
import build_theta_phi_image
import compensate_for_filters
import sum_along_theta
import plot_integrated_intensity
import write_data_to_file


import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image

######################################

im = Image.open(ip.forward_scatter_filename)
width, height = im.size
pix = im.load()

print im.size

# PIL pixel access objects have size = (width, height)
# numpy arrays have shape = (height, width)

filter_angles_deg = np.empty((height, width))
gsqr = np.empty((height, width))
pixel_value = np.empty((height, width))
phi = np.empty((height, width))
attenuation_correction = np.empty((height, width))
pixel_value_corrected_for_attenuation = np.empty((height, width))

print gsqr.shape


print "Initialised..."

central_pixel, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel = work_out_common_results.run(width, height, ip.x_scale, ip.y_scale, ip.view_x, ip.view_y, ip.offset, ip.normal, ip.source_position)

phi0_plane_normal = calc_plane_from_two_vectors.run(vector_origin_to_central_pixel, [0.0, 0.0, 1.0])

print "Calculating gsqr and phi for each pixel..."

for i in range(height):

    if ip.debug == True: print "\n###### COLUMN " + str(i) + " ############"

    for j in range(width):

        # numpy arrays have shape = (height, width)
        # PIL pixel access objects have size = (width, height)
        current_pixel_value = pix[j, i]

        current_gsqr, vector_origin_to_current_pixel = give_gsqr_value.run(i, j, ip.wavelength, ip.a_lattice, ip.normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, width, height)

        current_normal_to_plane = calc_plane_from_two_vectors.run(vector_origin_to_current_pixel, [0.0, 0.0, 1.0])

        current_phi_deg = calc_angle_between_vectors.run(current_normal_to_plane, phi0_plane_normal)

        current_filter_angle_deg = calc_angle_between_vectors.run(vector_origin_to_current_pixel, ip.normal)

        if current_phi_deg >= ip.phi_limit[0] and current_phi_deg <= ip.phi_limit[1]:  # Enforces the phi limits.

            filter_angles_deg[i, j] = abs(current_filter_angle_deg)
            gsqr[i, j] = current_gsqr
            phi[i, j] = abs(current_phi_deg)
            pixel_value[i, j] = current_pixel_value

        else:

            continue


print filter_angles_deg
print gsqr
print phi
print pixel_value

pixel_value_corrected_for_attenuation, attenuation_correction = compensate_for_filters.run(height, width, filter_angles_deg, pixel_value, ip.filter_attenuation_length_at_90_deg, ip.filter_thickness,
        attenuation_correction, pixel_value_corrected_for_attenuation)

im_theta_phi = build_image_skeleton.run(ip.theta_phi_n_pixels_width, ip.theta_phi_n_pixels_height)

gsqr_phi_bins, gsqr_phi_bin_pixel_counter, gsqr_bins, phi_bins = make_bins_for_theta_phi.run(ip.theta_phi_n_pixels_width, ip.theta_phi_n_pixels_height, ip.gsqr_limit, ip.phi_limit)  # outputs: gsqr_bin_list, phi_bin_list, image_bin_list, gsqr_bin_width, phi_bin_height

exit()
image_bin_list = populate_theta_phi_bins.run(gsqr, phi, pixel_value, gsqr_bin_list, phi_bin_list, image_bin_list, gsqr_bin_width, phi_bin_height)


image_bin_list = sum_pixel_values.run(image_bin_list, pixel_value)

gsqr_integrated_intensity = sum_along_theta.run(image_bin_list, gsqr_bin_list, phi_bin_list)

plot_integrated_intensity.run(gsqr_bin_list, gsqr_integrated_intensity)

write_data_to_file.run("integrated_intensity_vs_gsqr.dat", gsqr_bin_list, gsqr_integrated_intensity)

im_theta_phi = build_theta_phi_image.run(image_bin_list, im_theta_phi, gsqr_bin_list, phi_bin_list)

im_theta_phi.show()
im_theta_phi.save('gsqr_vs_phi.png')

if ip.plot == True:
    plt.scatter(gsqr, pixel_value, 1)
    plt.xlabel("$G^2$")
    plt.ylabel("PSL")
    plt.savefig('gsqr_vs_intensity.png')
    plt.plot()
    
print "Finished!"
