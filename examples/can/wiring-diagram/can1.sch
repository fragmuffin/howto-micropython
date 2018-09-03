EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:board
LIBS:can1-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCP2562-E/P U?
U 1 1 5B8A4D40
P 2350 1450
F 0 "U?" H 1950 1800 50  0000 L CNN
F 1 "MCP2562-E/P" H 2450 1800 50  0000 L CNN
F 2 "Housings_DIP:DIP-8_W7.62mm" H 2350 950 50  0001 C CIN
F 3 "" H 2350 1450 50  0001 C CNN
	1    2350 1450
	1    0    0    -1  
$EndComp
$Comp
L pyboardv1.1 A?
U 1 1 5B8A4EC1
P 2200 2700
F 0 "A?" H 4650 2950 60  0000 C CNN
F 1 "pyboardv1.1" H 2400 2950 60  0000 C CNN
F 2 "" H 2200 2700 60  0001 C CNN
F 3 "" H 2200 2700 60  0001 C CNN
	1    2200 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 1350 1400 2850
Wire Wire Line
	1400 2850 1700 2850
Wire Wire Line
	1400 1350 1850 1350
Wire Wire Line
	1850 1250 1350 1250
Wire Wire Line
	1350 1250 1350 2950
Wire Wire Line
	1350 2950 1700 2950
$Comp
L GND #PWR?
U 1 1 5B8A5204
P 2350 2150
F 0 "#PWR?" H 2350 1900 50  0001 C CNN
F 1 "GND" H 2350 2000 50  0000 C CNN
F 2 "" H 2350 2150 50  0001 C CNN
F 3 "" H 2350 2150 50  0001 C CNN
	1    2350 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2350 1850 2350 2150
Wire Wire Line
	1850 1650 1750 1650
Wire Wire Line
	1750 1650 1750 1900
Wire Wire Line
	1750 1900 2350 1900
Connection ~ 2350 1900
Wire Wire Line
	3150 2400 3150 2100
Wire Wire Line
	2350 2100 3650 2100
Connection ~ 2350 2100
Wire Wire Line
	3650 2100 3650 2400
Connection ~ 3150 2100
Wire Wire Line
	3850 950  3850 2400
Wire Wire Line
	3850 950  2350 950 
Wire Wire Line
	2350 950  2350 1050
Connection ~ 3850 2000
Wire Wire Line
	1700 2000 3850 2000
Wire Wire Line
	3350 2000 3350 2400
Wire Wire Line
	1700 2000 1700 1550
Wire Wire Line
	1700 1550 1850 1550
Connection ~ 3350 2000
$Comp
L R R?
U 1 1 5B8A5572
P 3200 1650
F 0 "R?" V 3280 1650 50  0000 C CNN
F 1 "120R" V 3200 1650 50  0000 C CNN
F 2 "" V 3130 1650 50  0001 C CNN
F 3 "" H 3200 1650 50  0001 C CNN
	1    3200 1650
	0    1    1    0   
$EndComp
Wire Wire Line
	2850 1350 4200 1350
Wire Wire Line
	3350 1350 3350 1650
Wire Wire Line
	3050 1650 3050 1550
Wire Wire Line
	2850 1550 4200 1550
Connection ~ 3050 1550
Connection ~ 3350 1350
NoConn ~ 4200 1350
NoConn ~ 4200 1550
$EndSCHEMATC
