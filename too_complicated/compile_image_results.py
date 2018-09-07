def run(master_bin_list, all_image_bin_lists):

    print "Compiling individual image bins into master bins..."

    for i in range(len(all_image_bin_lists)):

        for j in range(len(all_image_bin_lists[i])):

            pixel_indices = all_image_bin_lists[i][j][2]

            pixel_value = all_image_bin_lists[i][j][3]

            master_bin_list[j][2].append(pixel_indices)

            master_bin_list[j][3] += pixel_value

    return master_bin_list


