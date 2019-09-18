use_previous_pixel_loop = False
image_filename = ["masked_PSL_plate_1_s10268_BBXRD.tif", "masked_PSL_plate_2_s10268_BBXRD.tif", "masked_PSL_plate_3_s10268_BBXRD.tif", "masked_PSL_plate_4_s10268_BBXRD.tif"] # "3x4_test_image_0_to_12_thru_columns.tif" "s10260_PSL_forward_scatter_plate.tif" #"PSL_plate_4_s10268_BBXRD.tif" #"test_forward_scatter.tif"

source_position = [[45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204], [45.45194777, 0.0, 54.16752204]]  # In mm
offset = [[0.0, 11.7, 180], [0.0, 12.4677, 90], [0.0, 11.7, 0], [0.0, 11.7, 270]]  # X offset (mm), Y offset (mm), rotation (degrees)
sample_normal = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]


normal = [[-1.01101, 23.5, 11.5559], [22.0, -0.15, 12.0], [-1.1, -24.0, 11.0], [-25.6, 0.0, 9.4]]  # The normal to the plane of the image plate with units mm.

x_scale = [56.9, 53.65, 57.1, 55.75]  # In mm
y_scale = [42.55, 42.5, 42.3, 42.5]  # In mm

view_x = [[1.00, 0.0, 0.09], [-0.01, -1.0, 0.00], [-1.00, 0.0, -0.10], [0.0, 1.0, 0.00]]  # "normalised"
view_y = [[-0.08, -0.44, 0.89], [-0.48, -0.0, 0.88], [-0.09, 0.42, 0.90], [0.34, 0.0, 0.94]]  # "normalised"


wavelength = 1.3825  # In Angstroms
a_lattice = 3.3  # In Angstroms

num_subpixels_height = 1
num_subpixels_width = 1

correct_for_filter_attenuation = True
filter_thickness = [10.0, 10.0, 10.0, 10.0]  # [10.0, 6.0]
filter_attenuation_length_at_90_deg = [34.1, 34.1, 34.1, 34.1]  # [34.1, 109.7] # The attenuation length(s) of filter(s) used, in microns.
# Enter a new list element for each filter; the order doesn't matter. Zn, at 9 keV, has attenuation length of 34.1
# microns. Al, at 9 keV, has attenuation length of 109.7 microns.

correct_for_sample_attenuation = True

correct_for_polarisation = True

correct_for_lorentz_factor = False  # This correction is not of the right form currently.

correct_for_atomic_form_factor = True

gsqr_limit = [[6.0, 23.0], [6.0, 23.0], [6.0, 23.0], [6.0, 23.0]]
phi_limit = [[-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0], [-180.0, 180.0]]

num_gsqr_bins = 500
num_phi_bins = 500
minimum_pixels_per_bin = 6

minimum_pixels_in_column = 10


plot = True
debug = False
