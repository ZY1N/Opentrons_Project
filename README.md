# Opentrons_Project
A python program to perform yeast petri dish distribution to PCR trays on the Opentrons-OT-One Robot

## Table of Contents ##
*Objective[includes video]  
*Setup  
*How to Run  
*3d Part Holder
*App Beta

### Objective: ###
  The objective of this code is in order to collect samples from petri dishes and distribute them into PCR Trays. A pipette picks up a tip -> goes to the water trough -> picks up 100ul water -> picks up sample from petri dish -> puts it into PCR slot. See the video below for recorded demonstration. Also check out the beta app, which incorporates machine vision to detect places to take samples.

<img src="https://gfycat.com/oldfashionedshimmeringgrassspider.gif" width="640" height="398"/><p> <a href="https://gfycat.com/oldfashionedshimmeringgrassspider">via Gfycat</a></p>

<div style='position:relative; padding-bottom:calc(55.26% + 44px)'><iframe src='https://gfycat.com/ifr/OldfashionedShimmeringGrassspider' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div><p> <a href="https://gfycat.com/oldfashionedshimmeringgrassspider">via Gfycat</a></p>

## Click on Photo Below to Watch ##
[![20190907_131408 (1)](https://user-images.githubusercontent.com/27908897/64563908-4a846a80-d305-11e9-9f67-f9f902610eaa.jpg)](https://youtu.be/Hqnowgf_G3g)

  
### Setup: ###

First of all you need to setup the machine format as so below. Petri Dishes on B2, C2, and D2. Water containers on B3, C3, and D3. PCR-96 trays on B1, C1, and D1. Pipette tips should be on A3, and a trash container on A1.

### | A3 | B3 | C3 | D3 | E3 |  ###
### | A2 | B2 | C2 | D2 | E2 | ###
### | A1 | B1 | C1 | D1 | E1 | ###


![20190907_131408](https://user-images.githubusercontent.com/27908897/64561522-d09db280-d2ff-11e9-9702-919270efb9c7.jpg)
<img width="177" alt="Screen Shot 2019-09-09 at 12 47 06 PM" src="https://user-images.githubusercontent.com/27908897/64561578-f3c86200-d2ff-11e9-9005-d91bda645826.png">

### How to Run: ###
In order to run this program please attatch it to an Opentrons-Ot-One machine. Enter the command 'python3 protocol.py' in order to run the protocol. Please make sure that the robot is attatched or you will get an error

<img width="226" alt="Screen Shot 2019-09-09 at 12 41 51 PM" src="https://user-images.githubusercontent.com/27908897/64561303-3fc6d700-d2ff-11e9-8b35-e4d969857f82.png">

### 3D Parts: ###

These are the holders that are used to hold the petridish and water troughs in place, as seen in the video. They are modular in design and interchangable. The first picture is of the main petridish holder. Two braces are held apart by a round holder for the petri dish. The second picture and third picture are attachments that you can screw into the 2 main braces in order to convert them into water holders.

[<img width="629" alt="Screen Shot 2019-09-09 at 1 10 25 PM" src="https://user-images.githubusercontent.com/27908897/64563084-47887a80-d303-11e9-801f-5c55d83e86a8.png">](https://cad.onshape.com/documents/4f85f321c5e9bb3822e26e8f/w/5e36e6c439f2159fe2a17e3b/e/40a5098655e5d53734598d2c)

[<img width="516" alt="Screen Shot 2019-09-09 at 1 10 45 PM" src="https://user-images.githubusercontent.com/27908897/64563082-47887a80-d303-11e9-96c6-edce79956d9a.png">](https://cad.onshape.com/documents/25268cf03f4ebe23574cd863/w/20aaa79a2de8add8f43b47bd/e/ee051cdfb7139ba67216771b)

[<img width="264" alt="Screen Shot 2019-09-09 at 1 12 31 PM" src="https://user-images.githubusercontent.com/27908897/64563246-bd8ce180-d303-11e9-9eb9-08c73d0c46ec.png">](https://cad.onshape.com/documents/a18ea2d271567771182e8ddd/w/b9d126b66894c90f384734b7/e/85092496d4540e73111520d5)

### App-Beta ###
The purpose of this app is to provide an wrapper to better help visualize the process. Note: this is optimized for Mac and might not work on Raspberry Pi. To run go the app folder and run [python3 app.py]

<img width="895" alt="Screen Shot 2019-09-09 at 1 32 21 PM" src="https://user-images.githubusercontent.com/27908897/64564411-53297080-d306-11e9-9d63-19715c906184.png">

NOTE THIS IS NOT CALIBRATED AND MAY NOT WORK AS INTENDED

Init does the following:  
  - connects to the robot  
  - homes the robot  
  - takes pictures of the 3 petri dishes  

Start runs the number of plates you pick from the dropdown  

Beta Test MV takes the photos the petridishes and deterentiates them by threshold  

Run Beta Tests works by find the average pixel value of the squares and makes the pipette go to the location to pick up a sample there  



