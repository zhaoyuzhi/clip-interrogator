import os
import json

# read a txt expect EOF
def text_readlines(filename):
    # try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename)
        #file = open(filename, encoding = 'utf-8')
        #file = open(filename, encoding = 'gb18030', errors = 'ignore')
    except IOError:
        error = []
        return error
    content = file.readlines()
    # This for loop deletes the EOF (like \n)
    for i in range(len(content)):
        content[i] = content[i][:len(content[i]) - 1]
    file.close()
    return content

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

# read a jsonl file and judge whether it can be loaded
def jsonl_read(json_file):
    with open(json_file, "r", encoding = "utf-8") as reader:
            text = reader.read()
    return json.loads(text)

# save a list to a txt
def text_save(content, filename, mode = 'a'):
    # try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]) + '\n')
    file.close()

if __name__ == '__main__':
    
    base_filepath = 'metadata.jsonl'
    base = text_readlines(base_filepath)
    
    temp = []
    for k in range(len(base)):
        this_line = base[k]
        for l in range(len(this_line)):
            if this_line[l] == '\"':
                #if this_line[l-4:l] == 'name':
                if not (this_line[l+1:l+5] == 'file' or this_line[l-4:l] == 'name' or this_line[l-3:l] == '\": ' or this_line[l-4:l] == '.png' or this_line[l-3:l] == '\", ' or this_line[l-7:l] == 'feature' or this_line[l+1] == '}'):
                    new_str = this_line[:l] + this_line[(l+1):]
                    this_line = new_str
                    break
        temp.append(this_line)

    text_save(temp, 'metadata_filtered.jsonl', mode = 'a')
