#🌈‎Title<br/> DPFD-Net: a dual-path focus diffusion network for infrared small target detection

#🌈‎Description <br/>

    This project provides a complete infrared visual analysis framework, which integrates the processing, training and evaluation functions of two public datasets, HIT-UAV ( High-altitude UAV Infrared Thermal Imaging )   and M3FD-i ( Multi-modal Face Recognition Infrared Subset ). The framework aims to simplify the research process of infrared target detection and provide a reproducible benchmark implementation for academia.

 🌈‎Dataset Information<br/>
   1. HIT-UAV Dataset
    Download URL: https://datasetninja.com/hit-uav
   2. M3FD-i Dataset
    Download URL:[Biendata Platform](https://github.com/dlut-dimt/TarDAL)<br/>
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
    The version of ultralytics used in this project is 8.0.201, as indicated by the version in ultralytics/init.py.<br/>
    python: 3.10.14<br/>
    torch: 2.2.2+cu121<br/>
    torchvision: 0.17.2+cu121<br/>
    timm: 1.0.7<br/>
    mmcv: 2.2.0<br/>
    mmengine: 0.10.4<br/>
    trition: 3.2.0<br/>

#🌈‎Usage Instructions – How to use or load the dataset and code.<br/>
    clone https://github.com/ZGL-ZONG/DPFD-Net.git<br/>
    cd DPFD-Net<br/>
    pip install -r requirements.txt<br/>
    python train.py<br/>
    python val.py<br/>

#🌈‎Requirements.txt <br/>
   matplotlib>=3.3.0<br/>
   numpy>=1.22.2 # pinned by Snyk to avoid a vulnerability<br/>
   opencv-python>=4.6.0<br/>
   pillow>=7.1.2<br/>
   pyyaml>=5.3.1<br/>
   requests>=2.23.0<br/>
   scipy>=1.4.1<br/>
   torch>=1.8.0<br/>
   torchvision>=0.9.0<br/>
   tqdm>=4.64.0<br/>




