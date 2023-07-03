from ultralytics import YOLO

model=YOLO('yolov8n.yaml')

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# model.train(data="data.yaml",epochs=130,imgsz=640,plots=True)
# metrics=model.val()

if __name__ == '__main__':
    model.train(data="data.yaml",epochs=130,imgsz=640,plots=True)