import os
def writeSample(template_type,file_type):
    root = os.getcwd()
    path = os.path.join(root,'templates\GeneratedWeb')
    samples = os.listdir(path)
    num = str(len(samples)).zfill(3)
    os.chdir(path)
    os.makedirs(f'sample{num}')
    os.chdir(os.path.join(path,f'sample{num}'))
    
    for tt in template_type:
        print(tt,file_type[tt])
        with open(f"{file_type[tt]}","w",encoding='utf-8') as file:
            file.write('')
    return num

def processing():
    data_type = ['HTML:',"CSS (style.css):","JavaScript (script.js):"]
    template_type = ['html','css','js']
    file_type = dict([['html','index.html'],['css','style.css'],['js','script.js']])
    with open('chatlog.txt',"r",encoding='utf-8') as log:
        text = log.read()
    data = set()
    text = text.split('```')
    for i in range(len(text)):
        for j in range(len(data_type)):
            if data_type[j] in text[i]:
                idx = text[i+1].index('\n')
                data.add((text[i+1][idx+1:],template_type[j]))
    
    num = writeSample(template_type,file_type)
    for i in list(data):
        with open(f"{file_type[i[1]]}","w",encoding='utf-8') as f:
            f.write(i[0])
if __name__=='__main__':
    processing()