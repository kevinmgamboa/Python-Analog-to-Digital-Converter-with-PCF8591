# Python-Analog-to-Digital-Converter-with-PCF8591
This tutorial make used of a Raspberry Pi model B and the AD/DA converter PCF8591T from SUNFOUNDER to gather analog signals, following the book "Raspberry pi Cookbook for python programmers" in its chapter 7.

Let's start

Working with AD/DA converter PCF8591T - SUNFOUNDER MODULE

This tutorial was made with the SUNFOUNDER module AD/DA converter PCF8591T same as the one on the next picture. 

AD/DA converter PCF8591T - SUNFOUNDER MODULE
 
We need to connect this module to the Raspberry Pi as follow:


Image modified from sunfounder (ref: https://www.sunfounder.com/learn/sensor-kit-v2-0-for-raspberry-pi-b-plus/lesson-13-pcf8591-sensor-kit-v2-0-for-b-plus.html)


AD/DA converter PCF8591T - Connection with Raspberry Pi
Then, we can check if the PCF8581T is detected by the raspberry. To achieve this we can use the i2cdetect function at the terminal as follow:
