#run this part on shell to download zip file
#!pip install kaggle
#!mkdir ~/.kaggle
#!cp /Users/win10/Downloads/kaggle.json /Users/win10/.kaggle/kaggle.json
#!kaggle datasets list -s 'fraud detection'
#!kaggle datasets download -d 'ealaxi/paysim1'
#!mv paysim1.zip C:\Users\win10\Documents\TRAVAIL

import pandas as pd

# read the dataset using the cmpression zip
df = pd.read_csv("paysim1.zip", compression='zip')
print(df)
