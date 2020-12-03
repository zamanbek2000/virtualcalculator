<h1 align="center"> Virtual-Calculator </h1>

<h3>Introduction</h3>

<strong>If you are curious about how Tony Stark (Iron Man) virtual computer work then this project is a little approach toward it, I hope you will enjoy it.
 </strong>

In this project, I make a virtual calculator. When the code will execute it will use a webcam input and show the video which it captures in addition to that it will also draw a virtual calculator on the output video. User needs to raise his hand and by using the index finger or middle finger or ring finger he/she click virtually on the calculator and can perform any operation he/she wants. the result will display on the display board in the top part of the calculator. It is recommended to use all your fingers for better performance but you can also try it with 3 or 4 fingers.

<a href="https://youtu.be/aqUXr_prnjw"><strong>Youtube video for demonstration</strong></a><br>
<a href="https://youtu.be/aqUXr_prnjw"><img src="data/thumbnail.png"></a>


<h3>Description of all files</h3>

<h4>index.py</h4>

It is a central file that uses other files function, output, etc, and makes the program run.

<h4>addon_function.py</h4>

It will contain all function which is used by index.py. It is use to organize the code.


<h4>Set_HSV_values.py</h4>

When this code will run 3 windows are open, One will show normal video of input, 2nd window will show binary video, and 3rd window will show 7 trackbars, you can play with the first 6 trackbars to get a good binary video of yours in which your hand is properly distinctable. When it has done then close it. <br>
<strong>NOTE:-</strong> If you want to reset all values then click on the reset trackbar.


<h4>calc_size_position.py</h4>

This file is used to adjust calculator position and size by using trackbars. <br>
<strong>NOTE:-</strong> Don't make a value of <strong>X</strong> less than 400.


<h4>Data Folder</h4>

This folder contains all numerical values used by the program. By these values, I try to make my code a little bit dynamic.

<strong>hsv_values.txt -></strong> It will store the HSV value which is used to remove the background from the video which is a capture.

<strong>values.txt -></strong> It will store (x,y) coordinate if the top-left corner of calculator and height and width of a smallest block of the calculator.




<br>

<h3>Required Packages</h3>

```bash
- OpenCV-python
- Numpy
```

Numpy is only use to save and read values of some array
<br>


<h3>1 Getting Started</h3>


<h3>1.1 Installation</h3>

   
1. Clone This Repository
   
```bash
git clone https://github.com/iTs-rd/Virtual-Calculator.git
```
   
2. Install The Required Packages
```bash
cd Virtual-Calculator
pip install -r requirements.txt
```
<strong>If above code doesn't work replace pip by pip3.</strong><br>
It will install everything you need. If you have already installed some of the required packages it will skip that.

<h3>1.2 Run Program</h3>

To run the program simply enter this line

```bash
python index.py
```

When you run index.py it will open 2 windows one is of your normal live video and the other is small in size which shows a video of your right half part and also in binary form. If the smaller window will not removing your background properly or there is so much noise try to change your background by moving to another place or follow #1.3


<h3>1.3 Check Your Present Condition </h3>

First of all, You have to check your hand is properly detected or not. by entering this command

```bash
python Set_HSV_values.py
```

It will open 3 windows, One will show normal video of input, 2nd window will show B&W video, and 3rd window will show 7 trackbars, you can play with the first 6 trackbars to get a good B&W video of yours in which your hand is properly distinctable. When it has done then close it. <br>
<strong>NOTE:-</strong> If you wants to reset all values then click on reset trackbar.

<strong>If all done the program is ready to run</strong>


<h3>1.4 Costimize Calculator Position</h3>

Enter this command

```bash
python calc_size_position.py
```

It will open 2 windows one is your normal live video with calculator drawn on it and another window will contain 5 trackbars to change position, size of calculator. <br>
<strong>NOTE:-</strong> Rest button is used to reset calculator position.


<h3>Summary</h3>

Run these code line by line

```bash
git clone https://github.com/iTs-rd/Virtual-Calculator.git
cd Virtual-Calculator
pip install -r requirements.txt
python index.py
```
<br>
The idea for this project is from a youtube video.

<h3>Contacts</h3>
Email- Rudresh.gupta.che19@iitbhu.ac.in <br>
Linkedin- https://www.linkedin.com/in/rudresh-gupta-b87a84190
