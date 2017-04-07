This original project is online in this link:
https://www.youtube.com/watch?v=fJcl6Gw1D8k

## Install Libraries

**1. openCV for python3.6**
  * Download **opencv_python-3.2.0.6-cp36-cp36m-win32.whl (python3.6 32bit )** in this https://pypi.python.org/pypi/opencv-python
  * Go to folder that keep this file and Use this command to install
```
 pip install opencv_python-3.2.0.6-cp36-cp36m-win32.whl
```
**2. numpy in python**
```
pip install numpy
```
## How to Use

You can choose to run this project in two way 

**1. Run with no argument by run this command** 
```
python Main(NoArc).py  
```
  * The **"LicPlateImages/use01.jpg"** is a default input file.
  * The **"Output/imgDrawRec.jpg"** and **"Output/imgPlate.jpg"** are default output file 
**2. Run with no argument by run this command** 
```
python Main(Arc).py  [nameInput] [nameOutputRec] [nameOutputPlate]
```
  * **nameInput** is input file name.
  * **nameOutputRec** is output file name that contain rectangle that cover the license plate.
  * **nameOutputPlate** is output file name that crop the license plate only.

**Example**
```
python Main(Arc).py LicPlateImages/use01.jpg  Output/imgDrawRec.jpg  Output/imgPlate.jpg```
```
LicPlateImages/use01.jpg: 
![alt text][LicPlateImages/use01.jpg]

Output/imgDrawRec.jpg: 
![alt text][Output/imgDrawRec.jpg]

Output/imgPlate.jpg: 
![alt text][Output/imgPlate.jpg]

[LicPlateImages/use01.jpg]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "LicPlateImages/use01.jpg"
[Output/imgDrawRec.jpg]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "LicPlateImages/use01.jpg"
[Output/imgDrawPlate.jpg]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "LicPlateImages/use01.jpg"
