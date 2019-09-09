# Opentrons_Project
A python program to perform yeast petri dish distribution to PCR trays on the Opentrons-OT-One Robot

## Table of Contents ##
*Objective[includes video]  
*Setup  
*How to Run  
*3d Part Holder  

[<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)

### Objective: ###
  The objective of this code is in order to collect samples from petri dishes and distribute them into PCR Trays. A pipette picks up a tip -> goes to the water trough -> picks up 100ul water -> picks up sample from petri dish -> puts it into PCR slot. See the video below for recorded demonstration:
  
### Setup: ###

First of all you need to setup the machine format as so below. Petri Dishes on B2, C2, and D2. Water containers on B3, C3, and D3. PCR-96 trays on B1, C1, and D1. Pipette tips should be on A3, and a trash container on A1.

### | A3 | B3 | C3 | D3 | E3 |  ###
### | A2 | B2 | C2 | D2 | E2 | ###
### | A1 | B1 | C1 | D1 | E1 | ###


![20190907_131408](https://user-images.githubusercontent.com/27908897/64561522-d09db280-d2ff-11e9-9702-919270efb9c7.jpg)
<img width="177" alt="Screen Shot 2019-09-09 at 12 47 06 PM" src="https://user-images.githubusercontent.com/27908897/64561578-f3c86200-d2ff-11e9-9005-d91bda645826.png">

In order to run this program please attatch it to an Opentrons-Ot-One machine. Enter the command 'python3 protocol.py' in order to run the protocol.

<img width="226" alt="Screen Shot 2019-09-09 at 12 41 51 PM" src="https://user-images.githubusercontent.com/27908897/64561303-3fc6d700-d2ff-11e9-8b35-e4d969857f82.png">

### 3D Parts: ###

These are the holders that are used to hold the petridish and water troughs in place, as seen in the video. They are modular in design and interchangable. The first picture is of the main petridish holder. Two braces are held apart by a round holder for the petri dish. The second picture and third picture are attachments that you can screw into the 2 main braces in order to convert them into water holders.

<img width="629" alt="Screen Shot 2019-09-09 at 1 10 25 PM" src="https://user-images.githubusercontent.com/27908897/64563084-47887a80-d303-11e9-801f-5c55d83e86a8.png">

<img width="516" alt="Screen Shot 2019-09-09 at 1 10 45 PM" src="https://user-images.githubusercontent.com/27908897/64563082-47887a80-d303-11e9-96c6-edce79956d9a.png">

<img width="264" alt="Screen Shot 2019-09-09 at 1 12 31 PM" src="https://user-images.githubusercontent.com/27908897/64563246-bd8ce180-d303-11e9-9eb9-08c73d0c46ec.png">

