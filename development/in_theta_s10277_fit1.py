use_previous_pixel_loop = False
image_filename = ["masked_PSL_plate_1_s10268_BBXRD.tif", "masked_PSL_plate_2_s10268_BBXRD.tif", "masked_PSL_plate_3_s10268_BBXRD.tif", "masked_PSL_plate_4_s10268_BBXRD.tif"] # "3x4_test_image_0_to_12_thru_columns.tif" "s10260_PSL_forward_scatter_plate.tif" #"PSL_plate_4_s10268_BBXRD.tif" #"test_forward_scatter.tif"

source_position = [[45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204]]  # In mm
offset = [[0.0, 12.0, 180], [0.2, 13.7, 90], [0.0, 11.7, 0], [-0.4, 11.0, 270]]  # X offset (mm), Y offset (mm), rotation (degrees)
sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]


normal = [[-1.1709, 24.3938, 11.5139], [21.0, 0.0, 10.0], [-0.8594, -24.3, 11.0], [-24.4845, 3.8, 9.36425]]  # The normal to the plane of the image plate with units mm.

x_scale = [57.2, 58.7, 58.1, 57.3]  # In mm
y_scale = [43.2, 42.9, 43.5, 42.7]  # In mm

view_x = [[0.99, 0.0, 0.1], [0.00, -1.0, -0.00], [-1.00, 0.0, -0.08], [0.13, 0.99, -0.05]]  # "normalised"
view_y = [[-0.09, -0.43, 0.9], [-0.43, -0.0, 0.9], [-0.07, 0.41, 0.91], [0.36, 0.0, 0.93]]  # "normalised"


wavelength = 1.8505111  # 1.3825  # In Angstroms
a_lattice = 3.3  # In Angstroms

num_subpixels_height = 1
num_subpixels_width = 1

correct_for_filter_attenuation = True
filter_thickness = [10.0, 10.0, 10.0, 10.0]  # [10.0, 6.0]
filter_attenuation_length_at_90_deg = [20.8513, 20.8513, 20.8513, 20.8513]  # [34.1, 109.7] # The attenuation length(s) of filter(s) used, in microns.
# Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1
# microns. Al, at 9 keV, has attenuation length of 109.7 microns. At 6.667 keV Fe has attenuation length of 20.8513.

correct_for_sample_attenuation = True

correct_for_polarisation = True

correct_for_lorentz_factor = True

correct_for_atomic_form_factor = True

gsqr_limit = [[6.0, 23.0], [6.0, 23.0], [6.0, 23.0], [6.0, 23.0]]
phi_limit = [[-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0]]

num_gsqr_bins = 500
num_phi_bins = 500
minimum_pixels_per_bin = 6

minimum_pixels_in_column = 10


plot = True
debug = False
