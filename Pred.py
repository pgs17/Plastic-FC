import os
from ultralytics import YOLO
path=r"./prediction/images"
model=YOLO('Model1.pt')
for files in os.listdir(path):
  print(files)
  model.predict(source=f"{path}/{files}",show=True,save=True)
 