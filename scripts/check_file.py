import os
import json

# read a line to judge whether the string can be read
def dict_from_json_file(json_file):
    #with open(json_file.replace(".jsonl", ".txt"), 'w') as f:
    with open("question.txt", 'w') as f:
        with open(json_file, "r", encoding = "utf-8") as reader:
            text = reader.readlines()
            for idx, line in enumerate(text):
                try:
                    json.loads(line)
                except:
                    f.write(str(idx+1) + '\n')

if __name__ == '__main__':
    
    dict_from_json_file('metadata.jsonl')
