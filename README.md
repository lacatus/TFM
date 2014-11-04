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

1.	Python 2.7:

```
    sudo apt-get install python python-dev
```

2.	Numpy:

```
	sudo apt-get install python-numpy
```

3. Install OpenCV:

```
	sudo apt-get install python-opencv
```

4.  Install Python's Pip packet manager:

```
	sudo apt-get install python-pip
```

5.  Install Cython:

```
	sudo pip install cython
```

Setup project:
--------------

1.  Download source code:

```
	cd ~/
	git clone https://github.com/lacatus/TFM.git
```

2.	Download datasets:

```
	cd TFM/
	wget https://www.dropbox.com/s/7j7uno3tp30k4s9/data.tar.gz
	tar -xzf data.tar.gz
```

3.  Install Cython script:

```
	python setup.py
```

4.  Run project:

```
	python __main__.py
```