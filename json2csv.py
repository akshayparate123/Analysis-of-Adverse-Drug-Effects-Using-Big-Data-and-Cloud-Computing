import json
import pandas as pd
f = open("./Data/drug-event.json")
json_file = json.load(f)

new_list = []

# def append_dict(key,value,dict):
#     if key in list(dict.keys()):
#         dict[key].append(value)
#     else:
		
#         dict[key] = [value]
#     return dict


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
    # break
df = pd.DataFrame.from_dict(new_list)
df.to_csv('test.csv')
print()