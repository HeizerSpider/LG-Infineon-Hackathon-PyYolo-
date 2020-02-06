# LG-Infineon-Hackathon-PyYolo-

This repo includes the overall project outline (as can be seen in the S.I.M slides as well as poster).

[S.I.M Slide Deck](https://github.com/HeizerSpider/LG-Infineon-Hackathon-PyYolo-/blob/master/Safety%20In%20Motion%20(S.I.M).pdf)  
[S.I.M Poster](https://github.com/HeizerSpider/LG-Infineon-Hackathon-PyYolo-/blob/master/s.i.m%20poster.pdf)  
[Obj. Detection Python code](https://github.com/HeizerSpider/LG-Infineon-Hackathon-PyYolo-/blob/master/Object%20Detect%20by%20Bounding%20Box%20size.py)

It also includes a python file used for the project in the computer vision component. 
Here, PyYolo is used for the purpose of detecting the person(s) as well as objects in the picture as taken by the in-car camera (more details in slide/poster).

In this project, PyYolo was used for 2 main purposes:
1) To classify the objects detected in the image and determine if the objects on the car seat was a human/inanimate object, and determine if the seatbelt warning sign should appear.

![Rear Seat](Rear_seat.png)

2) Through the use of bounding boxes parameters (as seen in the code), to determine if the passenger(if there is one) in the front passenger seat should be allowed to be seated there or not (if child <[recommended height], then he should not be alowed to sit at the front)

![Front Seat](Front_seat.png)
