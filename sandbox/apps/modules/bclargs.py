#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Parse command-line arguments passed to Blender")


action_store_true = (
    ('--render-anim', '-a', 'Render frames from start to end (inclusive)'),
    ('--background', '-b', 'Run in background (often used for UI-less rendering)'),
    ('--window-border', '-w', 'Force opening with borders (default)'),
    ('--window-borderless', '-W', 'Force opening without borders'),
    ('--start-console', '-con', 'Start with the console window open (ignored if -b is set), (Windows only)'),
    ('--no-native-pixels', "Do not use native pixel size, for high resolution displays (MacBook 'Retina')"),
)


for action in action_store_true:
    help = action[-1]
    args = action[:-1]
    parser.add_argument(*args, help=help, action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    from pprint import pprint

    pprint(args)

