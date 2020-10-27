#!/usr/bin/env python3

import asyncio
import argparse
from pywizlight.bulb import wizlight, PilotBuilder

class Wizctrl():
    def __init__(self, ip):
        self.light = wizlight(ip)

    def __del__(self):
        del self.light

    async def turn_bulb_on(self):
        await self.light.turn_on(PilotBuilder())
    
    async def turn_bulb_on_scene(self, scene):
        await self.light.turn_on(PilotBuilder(scene = scene))

    async def turn_bulb_off(self):
        await self.light.turn_off()
    
    async def switch_bulb(self):
        await self.light.lightSwitch()
    
    async def run(self, args):
        if args.COMMAND == 'ON':
            if args.scene is not None:
                await self.turn_bulb_on_scene(args.scene)
            else:
                await self.turn_bulb_on()
        elif args.COMMAND == 'OFF':
            await self.turn_bulb_off()
        elif args.COMMAND == 'SWITCH':
            await self.switch_bulb()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Control Philips WiZ smart light bulbs')
    parser.add_argument('IP', type=str, help='IP address of smart bulb')
    parser.add_argument('COMMAND', type=str.upper, choices=['ON', 'OFF', 'SWITCH'], help='Command sent to the smart bulb')
    parser.add_argument('-s', '--scene', type=int, help='Set scene of smart bulb')
    #parser.add_argument('-c', '--color', type=str, help='Set color of smart bulb')
    #parser.add_argument('-b', '--brightness', type=str, help='Set brightness of smart bulb')
    #parser.add_argument('-s', '--speed', type=str, help='Set color changing speed of smart bulb')

    return parser.parse_args(args)

async def main():
    args = parse_args(None)
    wizctrl = Wizctrl(args.IP)
    await wizctrl.run(args)

if __name__ == "__main__":
    asyncio.run(main())
