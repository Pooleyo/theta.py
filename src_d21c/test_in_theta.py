# This file is only used when test_mode is True in 'in_theta.py'.
# This test geometry can be visualised using lp-diffract with the "test_geometry_1.dpf" file.

image_files = ['3x4_pixel_value_1.tif', '3x4_pixel_value_1.tif']  # "PSL_plate4_s10257_BBXRD.tif"#"3x3_white_test_image.tif"##"Nb_test_image.png"
#  #"PSL_plate4_s10257_BBXRD.tif"#"Nb_test_image.png"#

source_position = [[100.0, 0.0, 100.0], [100.0, 0.0, 100.0]]  # In mm

normal = [[-70.7107, 0.0, 70.7107], [0.0, 70.7107, 70.7107]]  # [-10.0, 0.0, 10.0] # The normal to the plane of the image plate with units mm.

sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]  # This is used to correct for attenuation in the diffracting sample.

offset = [[0.0, 0.0, 270.0], [-40.0, -10.0, 180]]  # X offset (mm), Y offset (mm), rotation (degrees); note that rotation is not actually used
# in this code, it is included simply to indicate which sonOfHoward parameters are being reference here.

x_scale = [60, 60]  # In mm

y_scale = [80, 80]  # In mm

view_x = [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]  # [-0.71, 0.0, -0.71] # "normalised"

view_y = [[0.71, 0.0, 0.71], [0.0, -0.71, 0.71]]  # [0.0, 1.0, 0.0] # "normalised"

wavelength = 1.378  # In Angstroms

a_lattice = 3.3  # In Angstroms

filter_thickness = [[2.0, 10.0], [2.0, 10.0]]

filter_attenuation_length = [[10.0, 2.0], [10.0, 2.0]]  # The attenuation length(s) of filter(s) used, in microns. Enter a new list
# element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1 microns. Al, at 9 keV,
#  has attenuation length of 109.7 microns.

phi_0_definer = [0.0, 0.0, 1.0]

phi_limit = [-180.0, 180.0]

gsqr_limit = [0.0, 100.0]

theta_phi_n_pixels_width = 3

theta_phi_n_pixels_height = 3

num_width_subpixels = 2
num_height_subpixels = 2

plot = True

debug = False

name_plot_integrated_intensity = 'integrated_intensity_vs_gsqr.png'
