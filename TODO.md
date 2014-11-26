TODO list

- [x] background.py --> bg subtraction with rgb channels
- [x] background.py --> remove unused def --> _2
- [x] background.py --> more accurate thresholding _1 && _2
- [x] background.py --> changed types of visualization used now
- [x] background.py --> do not update where detected
- [x] background.py --> depurate contours

- [x] data --> add PETS dataset
- [x] datasets --> add PETS dataset
- [x] data/datasets --> remove iglab6 ??

- [x] camera --> add intrinsics rectification to image
- [x] camera --> background images for cameras

- [x] gui --> imshow.py --> paint contours and bounding boxes separately
- [x] gui --> imshow.py --> paint contours projection 
- [x] gui --> trackbar.py --> explore buttons --> UNAVAILABLE FOR PYTHON
- [x] gui --> view FRAME by FRAME --> URGENT !!
- [x] gui --> trackbar --> asign each cam to the config <-- NEXT STEP
- [x] gui --> cvwaitket --> different frame rate in datasets

- [x] detection --> blob.py --> BLOB class with basic functions
- [x] detection --> blob.py --> threshold mean and view results
- [x] detection --> use y and x thresholded result to filter correctly where a person is
- [x] detection --> view docstring of the module
- [x] detection --> contprocess.py 
- [x] detection --> fitEllipse 
- [ ] detection --> subjects
	- create and adapt Subject class (DONE)
	- get lowest position of ellipse (DONE)
	- use retropoyection (read below)
	- differenciate between group or unique subject (use 3d data, width, ellipse angle)
	- delete false positives
	- show data through time in a 2d plane (z = 0) (one per camera)
	- pre-step for data tracking 

- [ ] retroprojection.py 
	- lowest position of ellipse into map
	- y depending on position
		- maybe initialization before video --> http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html
	- relate data to subjects

- [ ] Adapt best config for each dataset

- [ ] More datasets ??

- [ ] doc all .py

- [x] Write README
- [x] Find way to show evolution to teachers
