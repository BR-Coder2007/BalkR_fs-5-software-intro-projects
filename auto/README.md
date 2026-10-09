# PID Controller (For 1-Dimensional Car)

## Introduction

This project helps a 1D car reach & maintain a desired velocity, mainly through the help of a PID Controller. This is a developed onboarding project for the UCSC Formula Slug club, worked on by Balkaran Rai.

## How It Works

Given an object of a car with a desired velocity that it needs to reach, the PID controller uses sections P (Proportional), I (Integral), and D (Derivative), to calculate a desired acceleration. This desired acceleration will then be converted to a throttle percentage, which will then update the car and whatever its current velocity is. This, in turn, will lead to a feedback loop where it will keep going until the error (difference between current and desired velocity) reaches 0. Lastly, this project will generate two graphs: velocity over time and error over time, showing that the velocity will converge towards the desired velocity, and that the error will converge towards 0.

## Gain Scheduling

An extension of this system will include gain scheduling. Based on whatever the car's desired velocity is, the controller will select between specific values of different PID gains. There are 5 intervals in which it can be chosen from, 0-20, 21-40, 41-60, 61-80, and 81-100. This helps the overall performance of the system.

## Requirements
1. Python
2. NumPy
3. Matplotlib

## Project files
1. pid_template.py (Used to calcualte the desired acceleration and throttle, as well as containing the car's information)
2. run_template.py (Used to run the simulation and generate the graphs)