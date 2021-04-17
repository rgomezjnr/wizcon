#!/usr/bin/env python3

import sys
import argparse
import unittest
from unittest import IsolatedAsyncioTestCase
import wizcon
from wizcon import wizcon
import pywizlight.scenes


class TestTurnBulbOn(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)

    async def test_turn_bulb_on(self):
        await self.wizcon.turn_bulb_on()
        state = await self.wizcon.light.updateState()
        response = state.get_state()
        self.assertEqual(response, True)

    def tearDown(self):
        del self.wizcon

class TestTurnBulbOff(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)

    async def test_turn_bulb_off(self):
        await self.wizcon.turn_bulb_off()
        state = await self.wizcon.light.updateState()
        response = state.get_state()
        self.assertEqual(response, False)

    def tearDown(self):
        del self.wizcon

class TestSwitchBulb(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)

    async def test_switch_bulb(self):
        state = await self.wizcon.light.updateState()
        initial_bulb_state = state.get_state()

        await self.wizcon.switch_bulb()
        state = await self.wizcon.light.updateState()
        response = state.get_state()

        if initial_bulb_state is True:
            self.assertFalse(response)
        elif initial_bulb_state is False:
            self.assertTrue(response)
        #else:
        #    error

    def tearDown(self):
        del self.wizcon

class TestTurnBulbOnSceneId(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)
        self.scene_id = 23

    async def test_turn_bulb_on_scene_id(self):
        await self.wizcon.turn_bulb_on_scene_id(self.scene_id)
        state = await self.wizcon.light.updateState()
        scene_name = state.get_scene()
        scene_id = self.wizcon.light.get_id_from_scene_name(scene_name)
        self.assertEqual(scene_id, self.scene_id)

    def tearDown(self):
        del self.wizcon
        del self.scene_id

class TestTurnBulbOnSceneIdInvalid(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)
        self.scene_id = 0

    async def test_turn_bulb_on_scene_id_invalid(self):
        with self.assertRaises(IndexError):
            await self.wizcon.turn_bulb_on_scene_id(self.scene_id)

        self.scene_id = 33

        with self.assertRaises(IndexError):
            await self.wizcon.turn_bulb_on_scene_id(self.scene_id)

    def tearDown(self):
        del self.wizcon
        del self.scene_id

class TestTurnBulbOnSceneAll(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizcon = wizcon.Wizcon(args.IP)

    async def test_turn_bulb_on_scene_all(self):
        for scene_id in pywizlight.scenes.SCENES.keys():
            #if s == 1000:      # Skip scene 1000 Rhythm which fails test
            #    continue

            await self.wizcon.turn_bulb_on_scene_id(scene_id)
            state = await self.wizcon.light.updateState()
            scene_name = state.get_scene()
            self.assertEqual(self.wizcon.light.get_id_from_scene_name(scene_name), scene_id)

    def tearDown(self):
        del self.wizcon

class TestWizconScene(IsolatedAsyncioTestCase):
    def setUp(self):
        self.args = wizcon.parse_args([args.IP, 'on', '--scene_id=1'])
        self.wizcon = wizcon.Wizcon(self.args.IP)

    async def test_wizcon_scene(self):
        await self.wizcon.run(self.args)

        state = await self.wizcon.light.updateState()
        scene_name = state.get_scene()
        self.assertEqual(self.wizcon.light.get_id_from_scene_name(scene_name), self.args.scene_id)

    def tearDown(self):
        del self.args
        del self.wizcon

class TestTurnBulbOnBrightness(IsolatedAsyncioTestCase):
    def setUp(self):
        self.args = wizcon.parse_args([args.IP, 'on', '--brightness=28'])
        self.wizcon = wizcon.Wizcon(self.args.IP)

    async def test_wizcon_brightness(self):
        await self.wizcon.run(self.args)

        state = await self.wizcon.light.updateState()
        brightness_value = state.get_brightness()
        self.assertEqual(brightness_value, self.args.brightness)

#class TestTurnBulbOnColor(IsolatedAsyncioTestCase):
#class TestTurnBulbOnBrightnessAndColor(IsolatedAsyncioTestCase):

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test wizcon')
    parser.add_argument('IP', type=str, help='IP address of smart bulb')
    parser.add_argument('unittest_args', nargs=argparse.REMAINDER, help='Additional arguments for unittest.main()')
    args = parser.parse_args()
    unittest_argv = [sys.argv[0]] + args.unittest_args
    unittest.main(argv = unittest_argv)
