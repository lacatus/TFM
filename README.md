Tracking by detection real time surveillance system 
===================================================

Author:
-------

- Borja Lacabex Gonzalo
- Email: xebacal@gmail.com
- [Linkedin](http://bit.ly/blacabex)
- [Twitter](https://twitter.com/RoccoLacatus)

Resume:
-------

This project contains the code related to my Master Thesis in Computer Vision. The aim of the project is to make a Real Time people tracking system for Surveillance purposes.

The main software used for this project is the Open Source Computer Vision library, OpenCV, running under Python. Also for optimization purposes, Cython is used.

The surveillance datasets used for this project are:

- [Unsupervised Calibration of Camera Networks and Virtual PTZ Cameras (CVWW'12)](http://lrs.icg.tugraz.at/members/possegger#vptz)
- PETS 2009 - ftp://ftp.cs.rdg.ac.uk/pub/PETS2009/Crowd_PETS09_dataset/a_data/

This code has been made public so the knowledge shared in this project can benefits anothers. The code is distributed under the Apache License 2.0.

Instructions step by step:
--------------------------

The following instructions are provided in order to have the project installed in an Linux Ubuntu system or similar.

Dependecies:
------------

```
    sudo apt-get install python python-dev python-setuptools python-numpy python-opencv python-pip python-scipy python-matplotlib build-essential libatlas-dev libatlas3gf-base
```

- Install Cython and update Scipy:

```
	sudo pip install cython
	sudo pip install --upgrade scipy
```

- Build Scikit-learn:

```
	wget https://pypi.python.org/packages/source/s/scikit-learn/scikit-learn-0.15.2.tar.gz
	tar -xzf scikit-learn-0.15.2.tar.gz 
	cd scikit-learn-0-15-2/
	sudo python setup.py install
	
```

- Build and install OpenCV 3.0.0

```
sudo apt-get -y install libopencv-dev build-essential cmake git libgtk2.0-dev \
    pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev \
    libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev \
    libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \
    libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev \
    libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils 
wget https://github.com/Itseez/opencv/archive/3.0.0.zip
unzip 3.0.0.zip
cd opencv-3.0.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
make -j $(nproc)
sudo make install
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```

Setup project:
--------------

- Download source code:

```
	cd ~/
	git clone https://github.com/lacatus/TFM.git
```

- Download datasets:

```
	cd TFM/
	wget https://www.dropbox.com/s/7j7uno3tp30k4s9/data.tar.gz
	tar -xzf data.tar.gz
```

- Install Cython script:

```
	python setup.py
```

- Run project:

```
	python __main__.py
```