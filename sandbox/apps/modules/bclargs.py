#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Parse command-line arguments passed to Blender")


action_store_true = (
    ('--render-anim', '-a', 'Render frames from start to end (inclusive)'),
    ('--background', '-b', 'Run in background (often used for UI-less rendering)'),
)


for action in action_store_true:
    parser.add_argument(action[0], action[1], help=action[2], action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    from pprint import pprint

    pprint(args)


