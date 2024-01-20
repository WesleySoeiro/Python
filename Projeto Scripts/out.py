import os

dic = {
    'img' : ['jpeg','png', 'jpg'],
    'site': ['js', 'css', 'html'],
    'text': ['txt'],
    'zip': ['rar']
       }

cwd = os.getcwd()
#Imagens
folders_img = cwd + "\\" + "Imagens"
list_img = [fold for fold in os.listdir(folders_img)]
for file_type in list_img:
    path_img = cwd + "\\" + "Imagens" + "\\" + file_type
    files_img = os.listdir(path_img)
    for format in files_img:
        path_img = cwd + "\\" + "Imagens" + "\\" + format.split('.')[-1]+ "\\" + format
        from_path_img = path_img
        to_path_img = os.path.join(cwd, format)
        os.replace(from_path_img, to_path_img)
    
#Site
folders_site = cwd + "\\" + "Site"
list_site = [fold for fold in os.listdir(folders_site)]
for file_type in list_site:
    path_site = cwd + "\\" + "Site" + "\\" + file_type
    files_site = os.listdir(path_site)
    for format in files_site:
        path_site = cwd + "\\" + "Site" + "\\" + format.split('.')[-1]+ "\\" + format
        from_path_site = path_site
        to_path_site = os.path.join(cwd, format)
        os.replace(from_path_site, to_path_site)

#Text
folders_text = cwd + "\\" + "Text"
list_text = [fold for fold in os.listdir(folders_text)]
for file_type in list_text:
    path_text = cwd + "\\" + "Text" + "\\" + file_type
    files_text = os.listdir(path_text)
    for format in files_text:
        path_text = cwd + "\\" + "Text" + "\\" + format.split('.')[-1]+ "\\" + format
        from_path_text = path_text
        to_path_text = os.path.join(cwd, format)
        os.replace(from_path_text, to_path_text)
    
#Zip
folders_zip = cwd + "\\" + "Zip"
list_zip = [fold for fold in os.listdir(folders_zip)]
for file_type in list_zip:
    path_zip = cwd + "\\" + "Zip" + "\\" + file_type
    files_zip = os.listdir(path_zip)
    for format in files_zip:
        path_zip = cwd + "\\" + "Zip" + "\\" + format.split('.')[-1]+ "\\" + format
        from_path_zip = path_zip
        to_path_zip = os.path.join(cwd, format)
        os.replace(from_path_zip, to_path_zip)

for exc_img in list_img:
    remov_img = cwd + "\\" + "Imagens"+"\\"+exc_img
    os.rmdir(remov_img)
for exc_text in list_text:
    remov_text = cwd + "\\" + "Text"+"\\"+exc_text
    os.rmdir(remov_text)
for exc_zip in list_zip:
    remov_zip = cwd + "\\" + "Zip"+"\\"+exc_zip
    os.rmdir(remov_zip)
for exc_site in list_site:
    remov_site = cwd + "\\" + "Site"+"\\"+exc_site
    os.rmdir(remov_site)
os.rmdir('Imagens')
os.rmdir('Text')
os.rmdir('Zip')
os.rmdir('Site')
