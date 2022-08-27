# code 
import glob
import json
list_file = glob.glob("./ann/*.json")

# label config
array_label = {
    "blue": 0,
    "yellow": 1,
    "orange": 2
}


# read json file
def doc_json(file_name):
    # print(file_name)
    f = open(file_name,)
    jdata = json.loads(f.read())

    image_w = jdata['size']['width']
    image_h = jdata['size']['height']

    list_obj = []

    for item in jdata['objects']:
        label = item['classTitle']
        left = item['points']['exterior'][0][0]
        top = item['points']['exterior'][0][1]
        right = item['points']['exterior'][1][0]
        bottom = item['points']['exterior'][1][1]

        
        # convert supervisely format to coco format 
        width = abs(left - right)
        height = abs(bottom - top)

        x_center = abs(left + width/2)
        y_center = abs(top + height/2)

        n_width = width / image_w
        n_height = height / image_h
        n_x_center = x_center / image_w
        n_y_center = y_center / image_h


        str1 = f"{array_label[label]} {n_x_center} {n_y_center} {n_width} {n_height}\n"
        list_obj.append(str1)
    
    f.close()

    return list_obj

# rename file
def process_file_name(file_name):
    filename = file_name.split("/")[-1]
    return filename.replace(".png.json",".txt")


for item in list_file:
    lobj = doc_json(item)

    new_name_file = process_file_name(item)

    new_name_file = "./newdata/"+new_name_file

    print(new_name_file)
    f = open(new_name_file, "a")
    for obj in lobj:
        f.write(obj)
    f.close()


    

    # lay bbox 
    # 1. doc json  -> x1, y1, x2, y2, label  
    # 2. convert json -> coco format 

    # ghi no ra file 

