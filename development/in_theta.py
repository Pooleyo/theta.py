test_mode = True

image_files = ['3x3_pixel_value_1.tif']  # "PSL_plate4_s10257_BBXRD.tif"#"3x3_white_test_image.tif"##"Nb_test_image.png"
#  #"PSL_plate4_s10257_BBXRD.tif"#"Nb_test_image.png"#

source_position = [[50.0, 0.0, 49.8]]  # In mm

normal = [[-25.6, 0.0, 12.7078]]  # [-10.0, 0.0, 10.0] # The normal to the plane of the image plate with units mm.

sample_normal = [[0.0, 0.0, 1.0]]  # This is used to correct for attenuation in the diffracting sample.

offset = [[0.0, 12.0, 0.0]]  # X offset (mm), Y offset (mm), rotation (degrees); note that rotation is not actually used
# in this code, it is included simply to indicate which sonOfHoward parameters are being reference here.

x_scale = [56]  # In mm

y_scale = [44]  # In mm

view_x = [[0.01, 1.0, 0.02]]  # [-0.71, 0.0, -0.71] # "normalised"

view_y = [[0.44, -0.02, 0.90]]  # [0.0, 1.0, 0.0] # "normalised"

wavelength = 1.378  # In Angstroms

a_lattice = 3.3  # In Angstroms

filter_thickness = [[10.0, 6.0]]

filter_attenuation_length = [[34.1, 109.7]]  # The attenuation length(s) of filter(s) used, in microns. Enter a new list
# element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1 microns. Al, at 9 keV,
#  has attenuation length of 109.7 microns.

phi_0_definer = [0.0, 0.0, 1.0]

phi_limit = [-180.0, 180.0]

gsqr_limit = [0.0, 18.0]

theta_phi_n_pixels_width = 1

theta_phi_n_pixels_height = 1

num_width_subpixels = 1
num_height_subpixels = 1

plot = True

debug = False

name_plot_integrated_intensity = 'integrated_intensity_vs_gsqr.png'

