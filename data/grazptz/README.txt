-------------------------------------------------------------------------------
  Multi-Camera and Virtual PTZ
-------------------------------------------------------------------------------
  General Information
-------------------------------------------------------------------------------

The dataset contains the video streams and calibrations of several static 
cameras and one panoramic video from a spherical camera for two scenarios, both
indoor and outdoor. The panoramic imagery can be used to simulate a PTZ camera
with the proposed virtual PTZ (vPTZ).

Please cite the following paper if you use the dataset in a publication:

  @InProceedings{ possegger12virtualptz,
    author = {H. Possegger and M. R{\"u}ther and S. Sternig and 
        T. Mauthner and M. Klopschitz and P. M. Roth and H. Bischof},
    title = "{Unsupervised Calibration of Camera Networks and Virtual PTZ Cameras}",
    booktitle = "Proceedings of the Computer Vision Winter Workshop (CVWW)",
    year = "2012"
  }


-------------------------------------------------------------------------------
  Set 1 - Outdoor
-------------------------------------------------------------------------------

Contains videos from
  3 static Axis P1347 cameras
  1 spherical Point Grey Ladybug3 camera

The sequence consists of 6000 frames with a framerate of 15 fps, showing a 
crowded campus at Graz University of Technology.


-------------------------------------------------------------------------------
  Set 2 - Indoor
-------------------------------------------------------------------------------

Contains videos from
  4 static Axis P1347 cameras
  1 spherical Point Grey Ladybug3 camera

The sequence consists of 900 frames with a framerate of 15 fps, showing the 
preparations of a handball training game at a sports hall in Graz. 


-------------------------------------------------------------------------------
  Calibration Files
-------------------------------------------------------------------------------
  
For each scenario, we provide the extrinsic parameters of all cameras, as well
as the intrinsic parameters of the static cameras, both stored in the 
corresponding Matlab file 'calibration.mat'.
This file contains a cell array, holding a calibration structure for each
camera in the scenario. The structure contains the following entries:

    camera_label
        Identifier of the camera, i.e. 'cam-13x' for static cameras,
        resp. 'vPTZ' for the spherical camera.

    focal_length
    focal_length_error
    skew
    skew_error
    principal_point
    principal_point_error
    distortion
    distortion_error
        Intrinsic calibration obtained by the toolbox of Jean-Yves 
        Bouguet. See [1] for a detailed description of the intrinsic
        calibration parameters.

    R
        3x3 rotation matrix of the camera.
    t
        3x1 translation vector of the camera, s.t. t = -R * C, 
        where C is the focal point of the camera.


[1] Jean-Yves Bouguet. Camera Calibration Toolbox for Matlab, 2010.
    http://www.vision.caltech.edu/bouguetj/calib_doc/htmls/parameters.html

