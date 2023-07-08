import os
from ultralytics import YOLO
path=r"./prediction/images"

# Selected the best model of all iterations
model=YOLO('Model2(Large).pt')
for files in os.listdir(path):
  # print(files)
  model.predict(source=f"{path}/{files}",show=True,save=True)
 