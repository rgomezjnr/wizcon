# wizcon
Control Philips WiZ Connected smart light bulbs

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [pywizlight](https://github.com/sbidy/pywizlight)

## Installation
    pip install wizcon

## Usage
```
usage: wizcon [-h] [-si {1-32}] [-b {0-255}] IP {ON,OFF,SWITCH}

Control Philips WiZ Connected smart light bulbs

positional arguments:
  IP                    IP address of smart bulb
  {ON,OFF,SWITCH}       Command sent to the smart bulb

optional arguments:
  -h, --help            show this help message and exit
  -si {1-32}, --scene_id {1-32}
                        Set scene of smart bulb using scene ID
  -b {0-255}, --brightness {0-255}
                        Set brightness of smart bulb

Scene Table
1: "Ocean"
2: "Romance"
3: "Sunset"
4: "Party"
5: "Fireplace"
6: "Cozy"
7: "Forest"
8: "Pastel Colors"
9: "Wake up"
10: "Bedtime"
11: "Warm White"
12: "Daylight"
13: "Cool white"
14: "Night light"
15: "Focus"
16: "Relax"
17: "True colors"
18: "TV time"
19: "Plantgrowth"
20: "Spring"
21: "Summer"
22: "Fall"
23: "Deepdive"
24: "Jungle"
25: "Mojito"
26: "Club"
27: "Christmas"
28: "Halloween"
29: "Candlelight"
30: "Golden white"
31: "Pulse"
32: "Steampunk"

Examples

Turn smart bulb on:
wizcon 192.168.1.100 ON

Turn smart bulb off:
wizcon 192.168.1.100 OFF

Switch smart bulb between on and off states:
wizcon 192.168.1.100 SWITCH

Set scene to "Deepdive" using scene ID:
wizcon 192.168.1.100 ON --scene_id 23
```

## Source code
https://github.com/rgomezjnr/wizcon

## Author
[Robert Gomez, Jr.](https://github.com/rgomezjnr)

## License
[MIT](https://github.com/rgomezjnr/wizcon/blob/master/LICENSE.txt)
