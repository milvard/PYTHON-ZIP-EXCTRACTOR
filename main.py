import os  
from datetime import datetime  
from zipfile import ZipFile  

# Διεύθυνση αποθήκευσης φακέλου 
parentir = '.\\'
# Δημιουργία ονόματος φακέλου  
folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
newpath = os.path.join( parentir , folder_name)  
# Δημιουργία του φακέλου  
os.makedirs(newpath)  
# Εξαγωγή του zip στον νέο φάκελο  
with ZipFile("C:\\Users\\mvardakis\\Desktop\\ZIP EXCTRACT TO TIMESTAMP FOLDER (PYTHON)\\upload_inspee.gdb.zip", 'r') as zObject:  
    zObject.extractall(path=newpath)
