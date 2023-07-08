from ultralytics import YOLO

# assigned the model 
model=YOLO('yolov8l.yaml')

# trained the model
model.train(data="data.yaml",epochs=300,imgsz=640)

# Run on Colab