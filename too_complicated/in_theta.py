test_mode = False

image_files = ["PSL_plate_1_s10268_BBXRD.tif", "PSL_plate_2_s10268_BBXRD.tif", "PSL_plate_3_s10268_BBXRD.tif", "PSL_plate_4_s10268_BBXRD.tif"]

source_position = [[50.0, 0.0, 49.8], [50.0, 0.0, 49.8], [50.0, 0.0, 49.8], [50.0, 0.0, 49.8]]  # In mm

normal = [[0.0, 23.5, 11.7], [23.0, 0.0, 11.6], [0.05, -23.5, 11.6], [-25.6, 0.0, 12.7078]]  # [-10.0, 0.0, 10.0] # The normal to the plane of the image plate with units mm.

sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]  # This is used to correct for attenuation in the diffracting sample.

offset = [[0.0, 11.7, 182], [0.5, 11.0, 90], [1.0, 11.7, -1], [-25.6, 0.0, 12.7078]]  # X offset (mm), Y offset (mm), rotation (degrees); note that rotation is not actually used
# in this code, it is included simply to indicate which sonOfHoward parameters are being reference here.

x_scale = [56, 56, 56, 56]  # In mm

y_scale = [44, 44, 44, 44]  # In mm

view_x = [[1.00, 0.02, -0.03], [0.0, -1.00, -0.0], [-1.0, 0.01, 0.02], [0.01, 1.00, 0.02]]  # [-0.71, 0.0, -0.71] # "normalised"

view_y = [[0.03, -0.45, 0.89], [-0.45, -0.0, 0.89], [0.02, 0.44, 0.9], [0.44, -0.02, 0.9]]  # [0.0, 1.0, 0.0] # "normalised"

wavelength = 1.378  # In Angstroms

a_lattice = 3.3  # In Angstroms

filter_thickness = [[10.0, 6.0], [10.0, 6.0], [10.0, 6.0], [10.0, 6.0]]

filter_attenuation_length = [[34.1, 109.7], [34.1, 109.7], [34.1, 109.7], [34.1, 109.7]]  # The attenuation length(s) of filter(s) used, in microns. Enter a new list
# element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1 microns. Al, at 9 keV,
#  has attenuation length of 109.7 microns.

phi_0_definer = [0.0, 0.0, 1.0]

phi_limit = [-180.0, 180.0]

gsqr_limit = [0.0, 20.0]

num_gsqr_bins = 100
num_phi_bins = 100

num_width_subpixels = 1
num_height_subpixels = 1

plot = True

debug = False

name_plot_integrated_intensity = 'integrated_intensity_vs_gsqr.png'

name_plot_master_normalised_gsqr_vs_phi = 'master_normalised_gsqr_vs_phi.tif'

name_plot_master_preserved_gsqr_vs_phi = 'preserved_gsqr_vs_phi.tif'

name_plot_integrated_intensity_per_phi = 'intensity_per_phi_vs_gsqr.png'
