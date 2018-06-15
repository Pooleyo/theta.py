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
import calc_theta_phi
import compensate_for_thomson_factor
import make_mask_image


import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image

######################################

im = Image.open(ip.image_filename)
width, height = im.size
pix = im.load()

print "Initialised..."

central_pixel, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel = work_out_common_results.run(width, height, ip.x_scale, ip.y_scale, ip.view_x, ip.view_y, ip.offset, ip.normal, ip.source_position)

phi0_plane_normal = calc_plane_from_two_vectors.run(vector_origin_to_central_pixel, [0.0, 0.0, 1.0])

filter_angles_list_deg, thomson_angles_list_deg, gsqr, pixel_value, phi = calc_theta_phi.run(width, height, pix, ip.phi_limit, ip.gsqr_limit, ip.wavelength, ip.a_lattice, ip.normal,norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, phi0_plane_normal)

# The following functions apply corrections for thomson polarisation and filter attenuation.

pixel_value, filter_attenuation_correction_factor_list = compensate_for_filters.run(filter_angles_list_deg, pixel_value, ip.filter_attenuation_length, ip.filter_thickness)

pixel_value, thomson_attenuation_correction_factor_list = compensate_for_thomson_factor.run(thomson_angles_list_deg, pixel_value)


##########################################
# This section makes the images of masks for filter and thomson corrections.

make_mask_image.run("filter_angles_mask.png", "degrees", filter_angles_list_deg, width, height)

make_mask_image.run("thomson_angles_polarisation_mask.png", "degrees", thomson_angles_list_deg, width, height)

for i in range(len(ip.filter_thickness)):
    print len(filter_attenuation_correction_factor_list[i])
    make_mask_image.run("filter_" + str(i) + "_attenuation_factor_mask.png", "attenuation_factor", filter_attenuation_correction_factor_list[i], width, height)

make_mask_image.run("thomsons_attenuation_factor_mask.png", "attenuation_factor", thomson_attenuation_correction_factor_list, width, height)

############################################

im_theta_phi = build_image_skeleton.run(ip.theta_phi_n_pixels_width, ip.theta_phi_n_pixels_height)

gsqr_bin_list, phi_bin_list, image_bin_list, gsqr_bin_width, phi_bin_height = make_bins_for_theta_phi.run(im_theta_phi, gsqr, phi)

image_bin_list = populate_theta_phi_bins.run(gsqr, phi, pixel_value, gsqr_bin_list, phi_bin_list, image_bin_list, gsqr_bin_width, phi_bin_height)

image_bin_list = sum_pixel_values.run(image_bin_list, pixel_value)

gsqr_integrated_intensity = sum_along_theta.run(image_bin_list, gsqr_bin_list, phi_bin_list)

plot_integrated_intensity.run(gsqr_bin_list, gsqr_integrated_intensity)

write_data_to_file.run("integrated_intensity_vs_gsqr.dat", gsqr_bin_list, gsqr_integrated_intensity)

build_theta_phi_image.run(image_bin_list, im_theta_phi, gsqr_bin_list, phi_bin_list)

if ip.plot == True:
    plt.scatter(gsqr, pixel_value, 1)
    plt.xlabel("$G^2$")
    plt.ylabel("PSL")
    plt.savefig('gsqr_vs_intensity.png')
    
print "Finished!"
