from argparse import ArgumentParser

import core


def main(args):
    img, size = core.load_image(args['in'], args['size'])
    img = core.transform_image(img, args['colors'], args['rstate'])
    core.save_image(img, size, args['out'])

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--in', type=str)
    arg_parser.add_argument('--out', type=str)
    arg_parser.add_argument('--size', default=core.TARGET_SIZE, type=int)
    arg_parser.add_argument('--colors', default=core.PALETTE_COLORS, type=int)
    arg_parser.add_argument('--rstate', default=core.RANDOM_STATE, type=int)
    main(vars(arg_parser.parse_args()))
