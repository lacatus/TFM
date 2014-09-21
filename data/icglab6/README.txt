###############################################################################
# README - ICG Lab 6 Dataset
###############################################################################

This dataset contains the video streams and calibrations of 4 static cameras 
observing multiple people within our laboratory. There are 6 scenarios with
the following challenges:

* Changing appearance (chap): 
  This sequence depicts a standard surveillance scenario, where 5 people move 
  unconstrained within the laboratory. Throughout the scene, the people change
  their visual appearance by putting on jackets with significantly different 
  colors than their sweaters.

* Leapfrogs (leaf 1 & 2): 
  These scenarios depict leapfrog games where players leap over each other’s 
  stooped backs. Specific challenges of these sequences are the spatial 
  proximity of players, out-of-plane motion, and difficult poses.

* Musical chairs (much): 
  This sequence shows 4 people playing musical chairs and a non-playing 
  moderator who starts and stops the recorded music. Due to the nature of this
  game, this sequence exhibits fast motion, as well as crowded situations, 
  e.g., when all players race to the available chairs. Furthermore, sitting 
  on the chairs is a rather unusual pose for typical surveillance scenarios 
  and violates the commonly used constraint of standing persons.

* Pose: 
  This sequence shows up to 6 people in various poses, such as standing, 
  walking, kneeling, crouching, crawling, sitting, and stepping on ladders.

* Table: 
  This scenario exhibits significant out-of-plane motion as up to 5 people 
  walk and jump over a table.

For each scenario, we provide the synchronized video streams, the full 
(extrinsic & intrinsic) camera calibration, manually annotated groundtruth for
every 10th frame, as well as a top-view model of the ground-plane.

See below for more details on the provided data/file formats.
For a quick start, run the 'demo_groundtruth.m' MATLAB script.


Please cite the following paper if you use this dataset (bibtex):

  @InProceedings{ possegger13,
    author = {H. Possegger and S. Sternig and T. Mauthner and P.~M. Roth and H. Bischof},
    title = "{Robust Real-Time Tracking of Multiple Objects by Volumetric Mass Densities}",
    booktitle = "Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
    year = "2013"
  }


###############################################################################
# Camera calibration
###############################################################################

* The camera calibration data can be found in the file 'calibration.xml' within 
  the subfolder 'calibration'.

* The calibration data is stored in an OpenCV-compatible XML format, using the
  following tags:
  Note: The matrices are stored in row-major order (i.e., row-by-row).
  o <num_cameras>
    Holds the number of cameras used to record the scene.

  o <IDX>
    For each camera (X in [0, num_cameras-1]), this tag holds the camera 
    identifier to relate the corresponding video file.

  o <PX>
    For each camera, this tag holds the camera's projection matrix, which can 
    also be computed from the remaining parameters, as
      P = K * [R|t] = K * R * [I|-C].

  o <KX>
    For each camera, this tag holds the camera's intrinsic calibration matrix.

  o <RX>
    For each camera, this tag holds the camera's rotation matrix.

  o <CX>
    For each camera, this tag holds the location of its projection center.


###############################################################################
# Videos
###############################################################################

* The recorded video streams can be found in the corresponding subdirectories,
  e.g., chap/cam13X.avi.

* Each video:
  o has been recorded using a static Axis P1347 network camera.
  o is encoded using MPEG-4 (DIVX).
  o has an image resolution of 1024x768.
  o has a frame rate of 20fps.

* Note: Although effort has been made to make sure all camera views are 
  synchronised, there might be slight delays and frame drops in some cases.
  Please let us know if you encounter any inconsistencies.


###############################################################################
# Ground-plane
###############################################################################

* We provide a top view model of the ground-plane, see 
  o 'calibration/config-groundplane.xml'
  o 'calibration/groundplane_lab.png'

* The configuration is stored in an OpenCV-compatible XML format, using the
  following tags:
  o <gp_image_file>
    Filename of the ground-plane/top view image.

  o <gp_offset_x>, <gp_offset_y>
    Offsets (in pixels) of the world coordinate center within the top view image.

  o <m_per_pixel_x>, <m_per_pixel_y>
    Scaling factors to convert between real world ground-plane measurements and 
    pixel at the ground-plane model.

* Using the camera calibration, the homographies between camera views and 
  ground-plane image can easily be computed as:
    H_camview2gpimg = T * S * H_cam2gp,
  where
    T = [1 0 gp_offset_x; 0 1 gp_offset_y; 0 0 1],
    S = [1/m_per_pixel_x 0 0; 0 -1/m_per_pixel_y 0; 0 0 1],
  and H_cam2gp is the inverse of the homography H_gp2cam between the world 
  plane at Z=0 and the camera view, which can be computed as
    H_gp2cam = [p1 p2 p4], 
  where pi is the i-th column of the camera projection matrix P.


###############################################################################
# Groundtruth
###############################################################################

* For each scenario, we provide manually annotated groundtruth files, such as
  'chap/Groundtruth/annotations_person_X.txt', X in [0, num_people-1]. 
  Every 10th frame of the sequence has been annotated.

* These files contain the foot points in real world coordinates for the 
  corresponding person. Each line of such an annotation file follows the
  following format:
    <frame-nr>,<location-x>,<location-y>
  where frame-nr denotes the corresponding frame number (0-based), and 
  location-x and location-y denote the foot point's location on the real world 
  ground-plane.

* Note: The footpoints were manually annotated in each camera view. To obtain
  the provided real world foot points, we projected these onto the ground-plane
  and computed the mean over these projections.


###############################################################################
# Evaluation Protocol
###############################################################################

We provide MATLAB scripts to evaluate your results on these scenarios using
the CLEAR MOT metrics. The code package is available online:
  http://lrs.icg.tugraz.at/download#lab6

A detailed evaluation protocol is provided in the README file of the code 
archive.


