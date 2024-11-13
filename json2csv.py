import json
import pandas as pd
import os

def get_all_files():
    # Get the list of all files and directories
    path = "./Data/JSON"
    dir_list = os.listdir(path)
    # prints all files
    return dir_list

def json2csv(fileList):
    new_list = []
    for file in fileList:
        print(file)
        f = open("./Data/JSON/{}".format(file))
        json_file = json.load(f)
        for result in json_file["results"]:
            new_dict = {}
            # print(result)
            for key in result.keys():
                # print(key)
                if key == "patient":
                    for patient_key in result[key]:
                        if patient_key == "reaction" or patient_key == "drug":
                            for i in result[key][patient_key]:
                                for k in i.keys():
                                    new_dict[k] = i[k]
                                    # new_dict = append_dict(k,i[k],new_dict,idx)
                elif key == 'primarysource' or key == 'sender' or key == 'receiver':
                    try:
                        for k in result[key]:
                            # new_dict = append_dict(k,result[key][k],new_dict,idx)   
                            new_dict[k] = result[key][k]
                    except TypeError as e:
                        new_dict[key] = result[key]
                else:
                    # new_dict = append_dict(key,result[key],new_dict,idx)
                    new_dict[key] = result[key]
            new_list.append(new_dict)
    return new_list
    # break
    

fileList = get_all_files()
# print(fileList)
new_list = json2csv(fileList)
print(len(new_list))
df = pd.DataFrame.from_dict(new_list)
print(df.head())
df.to_csv('test.csv')
# print()