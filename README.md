# Room environmental sensor

This project aims to track environmental sensor readings from a room over time. This includes temperature, relative humidity and CO2 levels. Since this will placed indoors it will use WiFi as primary network, and send data over time to a central location.
If I have time I will also add a sound level tracker.

- [Room environmental sensor](#room-environmental-sensor)
    - [Objectives](#objectives)
    - [Material](#material)
    - [Environment setup](#environment-setup)
    - [Putting everything together](#putting-everything-together)
    - [Platforms and infrastructure](#platforms-and-infrastructure)
    - [The code](#the-code)
    - [The physical network layer](#the-physical-network-layer)
    - [Visualisation and user interface](#visualisation-and-user-interface)
    - [Finalizing the design](#finalizing-the-design)

### Objectives

I work in Educational Technology and wanted to dig into IOT and it's applicancy. The impact the working environment has on everyone, including students, is well known. Having IOT units inside the classrooms would allow to track the impact it has, and how the rooms are actually fitted for the numebr of students across all days. This can then be overlayed with other information, like performance, grades, schedules etc. to get an even bigger impact of the data.

Since this all about learning quickly I gave chosen tools that gets me to the end goal quickly, and perhaps not the best choices for a production grade product.

### Material

| Unit | Description | Price|
|------|-------------|------|
| [LoPy4 Bundle](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/) | A bundle created to the previous course by Electrokit | 949 SEK |



### Environment setup

First up is getting the machine working, and to do so I followed the [Getting Started guide from Pycom](https://docs.pycom.io/gettingstarted/). I am running on a Macbook Pro 2019 running macOS 11.4 (Big Sur). I already had NodeJS installed in my machine which is a pre-requistes and decided to use VSCode as it's my preferred choice of IDE. That did however prove to not be completely straight forward. Following the guide I installed the [Pymakr plugin](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) and seeing as I already had NodeJS installed I thought I would be golden. But after installing the plugin nothing happens, and all commands fails:
#TODO - Insert image here

After some fiddling around it turns out you need one more thing on Mac, xcode. So I installed XCode on my machine and presto, all working as intended.

### Putting everything together

![Screenshot of PDF claiming I2C adress to be 0x61](assets/screenshot_i2c_adr.png)

### Platforms and infrastructure
### The code
### The physical network layer
### Visualisation and user interface
### Finalizing the design
