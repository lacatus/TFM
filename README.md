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

- Install Cython:

```
	sudo pip install cython
```

- Build Scikit-learn:

```
	wget https://pypi.python.org/packages/source/s/scikit-learn/scikit-learn-0.15.2.tar.gz
	tar -xzf scikit-learn-0.15.2.tar.gz 
	cd scikit-learn-0-15-2/
	sudo python setup.py install
	
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