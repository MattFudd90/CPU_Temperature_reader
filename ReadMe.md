# CPU Temperature Reader for my Raspberry Pi

## Purpose of Project
This project reads the CPU temperature of a Raspberry Pi in real time. 
Displays the reading in a live graph using matplotlib.
Logs timestamped readings to a CSV file.

## Version
21/02/26

## Author
Matt Foord
Computer Science Student

##Technologies Used
- Python
- gpiozero
- matplotlib
- linux (debian)

## Installs required packages

```bash
sudo apt install python3-gpiozero python3-matplotlib

## How to run the program  

```bash
python3 cpu_temp.py

Press 'q' in the plot window to stop the program.

