use_previous_pixel_loop = False
image_filename = ["masked_PSL_plate_1_s10268_BBXRD.tif", "masked_PSL_plate_2_s10268_BBXRD.tif", "masked_PSL_plate_3_s10268_BBXRD.tif", "masked_PSL_plate_4_s10268_BBXRD.tif"] # "3x4_test_image_0_to_12_thru_columns.tif" "s10260_PSL_forward_scatter_plate.tif" #"PSL_plate_4_s10268_BBXRD.tif" #"test_forward_scatter.tif"

source_position = [[50.0, 0.0, 49.8], [50.0, 0.0, 49.8], [50.0, 0.0, 49.8], [50.0, 0.0, 49.8]]  # In mm
offset = [[0, 11.7, 180], [0, 15.5, 90], [0.2, 11.7, 0], [0, 12.0, 270]]  # X offset (mm), Y offset (mm), rotation (degrees)
sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]


normal = [[0.0, 23.2682, 13.2961], [26.4333, 0.0, 9.7], [0.0, -22.7259, 12.4235], [-25.6, 0.0, 12.9]]  # The normal to the plane of the image plate with units mm.

x_scale = [56, 56, 56, 56]  # In mm
y_scale = [44, 44, 44, 44]  # In mm

view_x = [[1.0, 0.0, 0.00], [0.0, -1.0, 0.00], [-1.0, 0.0, 0.00], [0.0, 1.0, 0.00]]  # "normalised"
view_y = [[0.0, -0.5, 0.87], [-0.34, -0.0, 0.94], [0.0, 0.48, 0.88], [0.45, 0.0, 0.89]]  # "normalised"


wavelength = 1.39  # In Angstroms
a_lattice = 3.3  # In Angstroms

num_subpixels_height = 2
num_subpixels_width = 2

correct_for_filter_attenuation = True
filter_thickness = [10.0, 10.0, 10.0, 10.0]  # [10.0, 6.0]
filter_attenuation_length_at_90_deg = [34.1, 34.1, 34.1, 34.1]  # [34.1, 109.7] # The attenuation length(s) of filter(s) used, in microns.
# Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1
# microns. Al, at 9 keV, has attenuation length of 109.7 microns.

correct_for_sample_attenuation = True

correct_for_polarisation = True

correct_for_lorentz_factor = True

correct_for_atomic_form_factor = True

gsqr_limit = [[3.0, 25.0], [3.0, 25.0], [3.0, 25.0], [3.0, 25.0]]
phi_limit = [[-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0]]

num_gsqr_bins = 1000
num_phi_bins = 500
minimum_pixels_in_gsqr_bin = 10


plot = True
debug = False
