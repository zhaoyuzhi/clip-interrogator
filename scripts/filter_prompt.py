import os

# save a list to a txt
def text_save(content, filename, mode = 'a'):
    # try to save a list variable in txt file.
    file = open(filename, mode, encoding = 'utf-8')
    for i in range(len(content)):
        file.write(str(content[i]) + '\n')
    file.close()

# read a txt expect EOF
def text_readlines(filename):
    # try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename, encoding = 'utf-8')
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

# post-process a text
def postp_text(text, unuseful_prompt, whether_add_share_str = False):
    prompt_list = text.split(', ')
    out_list = []
    for i in range(len(prompt_list)):
        save_tag = True
        for unuseful_item in unuseful_prompt:
            if unuseful_item in prompt_list[i]:
                save_tag = False
        if save_tag:
            out_list.append(prompt_list[i])
    if whether_add_share_str:
        out_string = ''
        for j in range(len(out_list)):
            out_string += out_list[j]
            if j != len(out_list) - 1:
                out_string += ', '
        out_string += ', gta v style'
    return out_string

if __name__ == '__main__':
    #-----------------------------------------------------------
    # read the original file and the unuseful prompt list
    base_txt = 'original.txt'
    unuseful_prompt_txt = 'unuseful_prompt.txt'
    whether_add_share_str = False

    base = text_readlines(base_txt)
    unuseful_prompt = text_readlines(unuseful_prompt_txt)

    #-----------------------------------------------------------
    
    save_file = 'metadata.jsonl'

    savelist = []
    for i in range(len(base) // 2):
        imgname = base[i*2]
        text = base[i*2+1]
        text = postp_text(text, unuseful_prompt, whether_add_share_str)
        cur_str = '{\"file_name\": \"' + imgname + '\", \"additional_feature\": \"' + text + '\"}'
        savelist.append(cur_str)
        print(i, len(base) // 2, cur_str)
        
    text_save(savelist, save_file, mode = 'a')
