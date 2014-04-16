import argparse


parser = argparse.ArgumentParser(description="Parse command-line arguments passed to Blender")

parser.add_argument('--background', '-b',
                    action='store_true',
                    help="Run in background (often used for UI-less rendering)")


if __name__ == '__main__':
    args = parser.parse_args()

    if args.background:
        print("Application is running in background mode")

