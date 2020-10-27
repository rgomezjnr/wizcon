#!/usr/bin/env python3

import sys
import argparse
import unittest
from unittest import IsolatedAsyncioTestCase
import wizctrl
import pywizlight.scenes

class TestTurnBulbOn(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)

    async def test_turn_bulb_on(self):
        await self.wizctrl.turn_bulb_on()
        state = await self.wizctrl.light.updateState()
        response = state.get_state()
        self.assertEqual(response, True)

    def tearDown(self):
        del self.wizctrl

class TestTurnBulbOff(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)

    async def test_turn_bulb_off(self):
        await self.wizctrl.turn_bulb_off()
        state = await self.wizctrl.light.updateState()
        response = state.get_state()
        self.assertEqual(response, False)

    def tearDown(self):
        del self.wizctrl

class TestSwitchBulb(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)

    async def test_switch_bulb(self):
        state = await self.wizctrl.light.updateState()
        initial_bulb_state = state.get_state()

        await self.wizctrl.switch_bulb()
        state = await self.wizctrl.light.updateState()
        response = state.get_state()

        if initial_bulb_state is True:
            self.assertFalse(response)
        elif initial_bulb_state is False:
            self.assertTrue(response)
        #else:
        #    error

    def tearDown(self):
        del self.wizctrl

class TestTurnBulbOnScene(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)
        self.scene_id = 23

    async def test_turn_bulb_on_scene(self):
        await self.wizctrl.turn_bulb_on_scene(self.scene_id)
        state = await self.wizctrl.light.updateState()
        scene_name = state.get_scene()
        self.assertEqual(self.wizctrl.light.get_id_from_scene_name(scene_name), self.scene_id)

    def tearDown(self):
        del self.wizctrl
        del self.scene_id

class TestTurnBulbOnSceneInvalid(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)
        self.scene_id = 9999

    async def test_turn_bulb_on_scene_invalid(self):
        with self.assertRaises(IndexError):
            await self.wizctrl.turn_bulb_on_scene(self.scene_id)

    def tearDown(self):
        del self.wizctrl
        del self.scene_id

class TestTurnBulbOnSceneAll(IsolatedAsyncioTestCase):
    def setUp(self):
        self.wizctrl = wizctrl.Wizctrl(args.IP)

    async def test_turn_bulb_on_scene_all(self):
        for scene_id in pywizlight.scenes.SCENES.keys():
            #if s == 1000:      # Skip scene 1000 Rhythm which fails test
            #    continue

            await self.wizctrl.turn_bulb_on_scene(scene_id)
            state = await self.wizctrl.light.updateState()
            scene_name = state.get_scene()
            self.assertEqual(self.wizctrl.light.get_id_from_scene_name(scene_name), scene_id)

    def tearDown(self):
        del self.wizctrl

class TestWizctrlScene(IsolatedAsyncioTestCase):
    def setUp(self):
        self.args = wizctrl.parse_args([args.IP, 'on', '--scene=1'])
        self.wizctrl = wizctrl.Wizctrl(self.args.IP)

    async def test_wizctrl_scene(self):
        await self.wizctrl.run(self.args)

        state = await self.wizctrl.light.updateState()
        scene_name = state.get_scene()
        self.assertEqual(self.wizctrl.light.get_id_from_scene_name(scene_name), self.args.scene)

    def tearDown(self):
        del self.args
        del self.wizctrl

#class TestTurnBulbOnBrightness(IsolatedAsyncioTestCase):
#class TestTurnBulbOnColor(IsolatedAsyncioTestCase):
#class TestTurnBulbOnBrightnessAndColor(IsolatedAsyncioTestCase):

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test Wizctrl')
    parser.add_argument('IP', type=str, help='IP address of smart bulb')
    parser.add_argument('unittest_args', nargs=argparse.REMAINDER, help='Additional arguments for unittest.main()')
    args = parser.parse_args()
    unittest_argv = [sys.argv[0]] + args.unittest_args
    unittest.main(argv = unittest_argv)
