#!/usr/bin/env python3

import asyncio
import argparse
import textwrap
from pywizlight.bulb import wizlight, PilotBuilder

class Wizcon():
    def __init__(self, ip):
        self.light = wizlight(ip)

    def __del__(self):
        del self.light

    async def turn_bulb_on(self):
        await self.light.turn_on(PilotBuilder())
    
    async def set_scene_id(self, scene_id):
        await self.light.turn_on(PilotBuilder(scene = scene_id))

    async def set_brightness(self, brightness_val):
        await self.light.turn_on(PilotBuilder(brightness = brightness_val))

    async def turn_bulb_off(self):
        await self.light.turn_off()
    
    async def switch_bulb(self):
        await self.light.lightSwitch()
    
    async def run(self, args):
        if args.COMMAND == 'ON':
            if (args.scene_id is not None and args.brightness is not None):
                await self.turn_bulb_on()
            elif (args.scene_id is not None):
                await self.set_scene_id(args.scene_id)
            elif (args.brightness is not None):
                await self.set_brightness(args.brightness)
        elif args.COMMAND == 'OFF':
            await self.turn_bulb_off()
        elif args.COMMAND == 'SWITCH':
            await self.switch_bulb()

def parse_args(args):
    parser = argparse.ArgumentParser(
        prog='wizcon',
        description='Control Philips WiZ Connected smart light bulbs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
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
        '''))
    parser.add_argument('IP', type=str, help='IP address of smart bulb')
    parser.add_argument('COMMAND', type=str.upper, choices=['ON', 'OFF', 'SWITCH'], help='Command sent to the smart bulb')
    parser.add_argument('-si', '--scene_id', type=int, choices=range(1,33), metavar='{1-32}', help='Set scene of smart bulb using scene ID')
    #parser.add_argument('-sn', '--scene_name', type=str, help='Set scene of smart bulb using scene name')
    #parser.add_argument('-c', '--color', type=str, help='Set color of smart bulb')
    parser.add_argument('-b', '--brightness', type=int, choices=range(0, 256), metavar='{0-255}', help='Set brightness of smart bulb')
    #parser.add_argument('-s', '--speed', type=str, help='Set color changing speed of smart bulb')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.2.1')

    return parser.parse_args(args)

async def main():
    args = parse_args(None)
    wizcon = Wizcon(args.IP)
    await wizcon.run(args)

# Entry point for running launch script after installing package, see setup.py
def main_async():
    return asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
