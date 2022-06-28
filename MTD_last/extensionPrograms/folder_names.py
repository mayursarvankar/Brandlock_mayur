import os
import csv
import shutil


with open( r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\programs\Screenshot\Reports\selcectors_img_count.csv", "a", newline="", encoding="UTF-8") as fp:
    writer=csv.writer(fp)
    writer.writerow(["Sr.no","Web_id","Img_count","Img_names"])

path=r'C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\programs\Screenshot\all_ss_images'

dir_list = os.listdir(path)


foldr_names=[i for i in dir_list if "xlsx" not in i and "csv" not in i]
print(f'ss_list -- > {len(foldr_names)} --> {foldr_names}')



sr_no=0
for j in foldr_names:
    sr_no = sr_no + 1
    path2=path + '\\' +str(j)
    dir_list2 = os.listdir(path2)
    print(f'{j} -- > {len(dir_list2)} --> {dir_list2}')

    with open(r"C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\programs\Screenshot\Reports\selcectors_img_count.csv", "a", newline="", encoding="UTF-8") as fp:
        writer = csv.writer(fp)
        writer.writerow([sr_no, j, len(dir_list2), dir_list2])

        # renaming_file
        for i in dir_list2:
            if ".PNG" in i:
                # print(f'{j} -- > {len(dir_list2)} --> {i}')
                path3 = path2 + '\\' + str(i)
                new_path = path3.replace(".PNG", ".png")
                os.rename(path3, new_path)

        # copy_pasting_file
        for k in dir_list2:
            og_path = path2 + '\\' + str(k)
            # print(f"copy og path -> {og_path}")
            og_path_split = og_path.split('\\')
            cline_name, img_nos = og_path_split[-2], og_path_split[-1]
            paste_file_name = cline_name + "_" + img_nos
            paste_path = r'C:\Users\Admin\PycharmProjects\db_conection_screenshot\MTD_Monthly\programs\Screenshot\All' + '\\' + paste_file_name

            shutil.copyfile(og_path, paste_path)




