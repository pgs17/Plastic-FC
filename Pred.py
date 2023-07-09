# importing required dependencies
import os
import pandas as pd
import PIL.Image
from pathlib import Path
from ultralytics import YOLO
path=r"./prediction/images"

df=pd.read_csv(r"C:\Users\saran\Desktop\DATA SCIENCE AND ML\Plastic\Submission.csv")
i=0
# Selected the best model of all iterations
model=YOLO('Model2(Large).pt')

# prediction and geotagging
for files in os.listdir(path):
  # print(files)
  model.predict(source=f"{path}/{files}",show=True,save=True)

  # getting the geolocation 
  img=PIL.Image.open(f"{path}/{files}")
  exif={PIL.ExifTags.TAGS[k]:v
      for k,v in img._getexif().items()
      if k in PIL.ExifTags.TAGS
      
      }
  n=exif['GPSInfo'][2]
  e=exif['GPSInfo'][4]
  ltd=(float)((((n[0]*60)+n[1])*60)+n[2])/60/60
  lng=(float)((((e[0]*60)+e[1])*60)+e[2])/60/60
  df.loc[i,'Geo_Tag_URL']=str(ltd)+"°N"+" "+str(lng)+"°E" 
  i=i+1
  df.to_csv("Submission.csv",index=False)

 