
Try to make this demo on my Jetson nano
https://github.com/mit-han-lab/temporal-shift-module

https://github.com/mit-han-lab/temporal-shift-module/tree/master/online_demo

The link to the script to build opencv is dead
  Script can be found here (https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.1.1_Jetson.sh)

I edited it because there is a mistake in the cmake statement

To proceed to step: "sudo python3 setup.py install"
  sudo apt-get install python3-setuptools
  
To install some packages with pip (because apparently the Jetson nano does not come with Python pip)  
  sudo apt install python3-pip
