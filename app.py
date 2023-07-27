import argparse

import yaml

from src.processed import PROCESSED

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, required=True, help="path to yaml config")
args = parser.parse_args()

with open(args.config, mode="r") as stream:
    config = yaml.safe_load(stream)


if __name__ == "__main__":

    parser = PROCESSED(config)
    parser.competitions()
