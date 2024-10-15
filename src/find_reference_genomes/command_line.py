import argparse

import find_reference_genomes





def main():
    # parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Short description of what this script does. It will be displayed when running find_reference_genomes -h')
    parser.add_argument(
        '--first',
        type=int,
        required=True,
        help='Short description of the first argument')
    parser.add_argument(
        '--second',
        type=int,
        required=True,
        help='Short description of the second argument')
    args = parser.parse_args()

    # run whatever
    find_reference_genomes.dummy_function()
