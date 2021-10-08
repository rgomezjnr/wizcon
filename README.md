# wizcon
Control Philips WiZ Connected smart light bulbs

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [pywizlight](https://github.com/sbidy/pywizlight)

## Installation
    pip install wizcon

## Usage
```
usage: wizcon [-h] [-si {1-32}] [-b {0-255}] [-v] IP {ON,OFF,SWITCH}

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
  -rgb {0-255} {0-255} {0-255}, --rgb {0-255} {0-255} {0-255}
                        Set RGB color of smart bulb
  -v, --version         show program's version number and exit

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
wizcon --scene_id 23 192.168.1.100 ON

Set brightness to 255 (max brightness):
wizcon --brightness 255 192.168.1.100 ON

Set smart bulb color to blue:
wizcon -rgb 0 0 255 192.168.1.100 ON
```

## Tested bulbs

|                  |              |             |
| ---------------- | ------------ |------------ |
| Model            | A19 (RGB)    |AE27 (White) |
| Firmware Version | 1.22.0       |1.17.1       |
| Model ID         | 23007        |23032        |

## Related
[Smart-Bulb-Control](https://github.com/rgomezjnr/Smart-Bulb-Control) - Rainmeter skin for controlling smart light bulbs

## Support
If you find an issue or have any feedback please submit an issue on [GitHub](https://github.com/rgomezjnr/wizcon/issues).

If you would like to show your support donations are greatly appeciated via:
- [GitHub Sponsors](https://github.com/sponsors/rgomezjnr)
- [PayPal](https://paypal.me/rgomezjnr)
- [Bitcoin:](bitcoin:bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p) bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p
- [Ethereum:](ethereum:0xAB443e578c9eA629088e26A9009e44Ed40f68678) 0xAB443e578c9eA629088e26A9009e44Ed40f68678

## Authors
[Robert Gomez, Jr.](https://github.com/rgomezjnr)

[Ariq Fadlan](https://github.com/ariqfadlan)

## Source code
https://github.com/rgomezjnr/wizcon

## License
[MIT](https://github.com/rgomezjnr/wizcon/blob/master/LICENSE.txt)
