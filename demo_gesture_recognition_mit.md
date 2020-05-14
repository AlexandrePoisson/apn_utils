# Demo Gesture recognition
Try to make this demo on my Jetson nano
https://github.com/mit-han-lab/temporal-shift-module

https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo

## Build opencv
The link to the script to build opencv is dead
Script can be found here (https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.1.1_Jetson.sh)

I edited it because there is a mistake in the cmake statement

## Install TVM
To proceed to step: "sudo python3 setup.py install"
    sudo apt-get install python3-setuptools
  
To install some packages with pip (because apparently the Jetson nano does not come with Python pip)  
    sudo apt install python3-pip

## Install pytorch 1.3.0

  wget https://nvidia.box.com/shared/static/phqe92v26cbhqjohwtvxorrwnmrnfx1o.whl -O torch-1.3.0-cp36-cp36m-linux_aarch64.whl
  pip3 install numpy torch-1.3.0-cp36-cp36m-linux_aarch64.whl

## Install torchvision 0.5.0
  sudo apt-get install libjpeg-dev zlib1g-dev
  git clone --branch v0.5.0 https://github.com/pytorch/vision torchvision   
see below for version of torchvision to download https://github.com/pytorch/vision.git

## Clone tsm package
