#🌈‎Title<br/> DPFD-Net: a dual-path focus diffusion network for infrared small target detection

#🌈‎Description <br/>

    This project provides a complete infrared visual analysis framework, which integrates the processing, training and evaluation functions of two public datasets, HIT-UAV ( High-altitude UAV Infrared Thermal Imaging )   and M3FD-i ( Multi-modal Face Recognition Infrared Subset ). The framework aims to simplify the research process of infrared target detection and provide a reproducible benchmark implementation for academia.

 🌈‎Dataset Information<br/>
   1. HIT-UAV Dataset
   *   Source: Harbin Institute of Technology
   *   Scale: 2,898 infrared images, 105,786 annotated bounding boxes
   *   Classes: Person, Car, Bicycle, OtherVehicle
   *   Resolution: 1024×1024 pixels
   *   Format: .jpg images + .txt format annotations
   *   Features: High-altitude perspective, dense small targets, diverse real-world scenarios
   *   Download URL: https://datasetninja.com/hit-uav
   2. M3FD-i Dataset
   *   Source: Multimodal & Multispectral Face Database (Infrared Subset)
   *   Scale: 4,200 infrared face images, 21,000 annotations
   *   Annotations: Face detection, keypoint labeling, attribute labeling
   *   Scenarios: Indoor/outdoor, various lighting conditions
   *   Format: .jpg images + .txt format annotations
   下载地址：[Biendata Platform](https://github.com/dlut-dimt/TarDAL)
   ├── data<br/>
   │    ├── HIT-UAV/<br/>
   │      │   ├── images/          # Images<br/>
   │      │   ├── labels/          # Text annotation files<br/>
   │      │   ├── split/           # Dataset split for images/labels<br/>
   │    ├── M3FD-i/<br/>
   │      │   ├── images/          # Infrared images<br/>
   │      │   ├── labels/          # Text annotation files<br/>
   │      │   ├── split/           # Dataset split for images/labels<br/>
   
#🌈 Code Information.<br/>
    The version of ultralytics used in this project is 8.0.201, as indicated by the version in ultralytics/init.py.
    python: 3.10.14
    torch: 2.2.2+cu121
    torchvision: 0.17.2+cu121
    timm: 1.0.7
    mmcv: 2.2.0
    mmengine: 0.10.4
    trition: 3.2.0<br/>

#🌈‎Usage Instructions – How to use or load the dataset and code.<br/>
    clone https://github.com/ZGL-ZONG/DPFD-Net.git
    cd DPFD-Net
    pip install -r requirements.txt
    python train.py
    python val.py<br/>

#🌈‎Requirements.txt <br/>
   matplotlib>=3.3.0
   numpy>=1.22.2 # pinned by Snyk to avoid a vulnerability
   opencv-python>=4.6.0
   pillow>=7.1.2
   pyyaml>=5.3.1
   requests>=2.23.0
   scipy>=1.4.1
   torch>=1.8.0
   torchvision>=0.9.0
   tqdm>=4.64.0

#🌈‎Methodology (if applicable) – Steps taken for data processing or modeling.<br/>
#🌈‎Citations (if applicable) – If this dataset was used in research, provide references.<br/>
#🌈‎License & Contribution Guidelines (if applicable).<br/>


