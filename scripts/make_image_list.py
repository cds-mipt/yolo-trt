import argparse
import os


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str, required=True)
    parser.add_argument("--image-list", type=str, required=True)
    return parser


def main(args):
    paths = []
    for filename in os.listdir(args.folder):
        paths.append(os.path.join(args.folder, filename))

    with open(args.image_list, "w") as f:
        f.write("\n".join(sorted(paths)))


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    main(args)
