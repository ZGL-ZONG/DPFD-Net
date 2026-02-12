import warnings, os


warnings.filterwarnings('ignore')
from ultralytics import RTDETR



if __name__ == '__main__':
    model = RTDETR('D:/old/RT-DETR/RTDETR-20250403/RTDETR-main/ultralytics/cfg/models/rt-detr/rtdetr-DID.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='D:/old/RT-DETR/RTDETR-20250403/RTDETR-main/DOTA/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=2,
                workers=0, 
                # device='0,1',
                # resume='', # last.pt path
                project='runs/train',
                name='exp',
                )
