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
 
filter_angles_list_deg = []  
gsqr = []
pixel_value = []
phi = []

print "Initialised..."

central_pixel, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel = work_out_common_results.run(width, height, ip.x_scale, ip.y_scale, ip.view_x, ip.view_y, ip.offset, ip.normal, ip.source_position)

phi0_plane_normal = calc_plane_from_two_vectors.run(vector_origin_to_central_pixel, [0.0, 0.0, 1.0])

print "Calculating gsqr and phi for each pixel..."

for i in range(width):
    if ip.debug == True: print "\n###### COLUMN " + str(i) + " ############"
    for j in range(height):
    
        current_pixel_value = pix[i,j]

        current_gsqr, vector_origin_to_current_pixel = give_gsqr_value.run(i, j, ip.wavelength, ip.a_lattice, ip.normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, width, height)
        
        
        current_normal_to_plane = calc_plane_from_two_vectors.run(vector_origin_to_current_pixel, [0.0, 0.0, 1.0])

        
        current_phi_deg = calc_angle_between_vectors.run(current_normal_to_plane, phi0_plane_normal)
    
        current_filter_angle_deg = calc_angle_between_vectors.run(vector_origin_to_current_pixel, ip.normal)
       
        if current_phi_deg >= ip.phi_limit[0] and current_phi_deg <= ip.phi_limit[1]: # Enforces the phi limits.
        
            filter_angles_list_deg.append(abs(current_filter_angle_deg))   
            gsqr.append(current_gsqr)        
            phi.append(current_phi_deg)        
            pixel_value.append(current_pixel_value)
            
        else:
            continue

pixel_value = compensate_for_filters.run(filter_angles_list_deg, pixel_value, ip.filter_attenuation_length, ip.filter_thickness)

im_theta_phi = build_image_skeleton.run(ip.num_gsqr_bins, ip.num_phi_bins)

gsqr_bin_list, phi_bin_list, image_bin_list, gsqr_bin_width, phi_bin_height = make_bins_for_theta_phi.run(im_theta_phi, gsqr, phi)

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
