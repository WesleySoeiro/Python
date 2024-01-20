import os

cwd = os.getcwd()
list_dir = os.listdir(cwd)
list_itens = [i for i in list_dir if os.path.isfile(i) and '.py' not in i]
types = list(set([i.split('.')[-1].lower() for i in list_itens]))
dic = {
    'img' : ['jpeg','png', 'jpg'],
    'site': ['js', 'css', 'html'],
    'text': ['txt'],
    'zip': ['rar']
       }

os.mkdir('Imagens')
os.mkdir('Site')
os.mkdir('Text')
os.mkdir('Zip')

for file_type in types:
    os.mkdir(file_type)
 
    if file_type in dic['img']:
        inp = os.path.join(cwd, file_type)
        outp = os.path.join(cwd, 'Imagens', file_type) 
        os.replace(inp, outp)
        
    elif file_type in dic['site']:
        inp = os.path.join(cwd, file_type)
        outp = os.path.join(cwd, 'Site', file_type) 
        os.replace(inp, outp)
        
    elif file_type in dic['text']:   
        inp = os.path.join(cwd, file_type)
        outp = os.path.join(cwd, 'Text', file_type) 
        os.replace(inp, outp)
        
    elif file_type in dic['zip']:
        inp = os.path.join(cwd, file_type)
        outp = os.path.join(cwd, 'Zip', file_type) 
        os.replace(inp, outp)
        
        
for file in list_itens:
    if file.split('.')[-1] in dic['img']:
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, 'Imagens', file.split('.')[-1], file)
        os.replace(from_path, to_path)

    elif file.split('.')[-1] in dic['site']:
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, 'Site', file.split('.')[-1], file)
        os.replace(from_path, to_path)

    elif file.split('.')[-1] in dic['text']:
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, 'Text', file.split('.')[-1], file)
        os.replace(from_path, to_path)

    elif file.split('.')[-1] in dic['zip']:
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, 'Zip', file.split('.')[-1], file)
        os.replace(from_path, to_path)
        
    


