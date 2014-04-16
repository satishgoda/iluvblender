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
    args, help = action[:-1], action[-1]
    parser.add_argument(*args, help=help, action='store_true')


parser.add_argument('--scene', '-S',
                    help='Set the active scene <name> for rendering',
                    type=str,
                    action='store')


def render_frame(arg):
    try:
        int(arg)
    except ValueError as e:
        message = '\n\tvalid options are int, +int, -int'
        raise argparse.ArgumentTypeError(e.message+message)
    return arg

parser.add_argument('--render-frame', '-f',
                    help='Render frame <frame> and save it. \n+<frame> start frame relative, -<frame> end frame relative.',
                    type=render_frame,
                    action='store')

action_store_int = (
    ('--frame-start', '-s', 'Set start to frame <frame> (use before the -a argument)'),
    ('--frame-end', '-e', 'Set end to frame <frame> (use before the -a argument)'),
    ('--frame-jump', '-j', 'Set number of frames to step forward after each rendered frame'),
)

for action in action_store_int:
    args, help = action[:-1], action[-1]
    parser.add_argument(*args, help=help,
                        type=int,
                        action='store')

parser.add_argument('--window-geometry', '-p',
                    nargs=4, type=int,
                    action='store',
                    help='Open with lower left corner at <sx>, <sy> and width and height as <w>, <h>')


if __name__ == '__main__':
    args = parser.parse_args()

    from pprint import pprint

    pprint(vars(args))


