import re
import copy
import os

def load_file_raw(path):
    with open(path, "r") as f:
        return f.read()

def replace_with(text, regexes:dict):
    text_temp = copy.copy(text)
    for key, value in regexes.items():
        text_temp = re.sub(key, value, text_temp)
    return text_temp

if __name__ == '__main__':
    dataset_name_path = {"Yoochoose": "docs/exp_data/yoochoose", "Diginetica": "docs/exp_data/diginetica", "Coveo": "docs/exp_data/coveo", "Retailrocket": "docs/exp_data/retailrocket"}
    
    template_text = load_file_raw("docs/exp_data/rees46/rees46_main.rst")
    template_dataset_name = "Rees46"
    for dataset_name, result_path in dataset_name_path.items():
        regexes = {template_dataset_name: dataset_name, template_dataset_name.lower(): dataset_name.lower()}
        res_text = replace_with(template_text, regexes)
        with open(os.path.join(result_path, f"{dataset_name.lower()}_main.rst"), "w") as f:
            f.write(res_text)