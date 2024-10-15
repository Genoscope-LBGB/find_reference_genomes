import argparse

import find_reference_genomes


def main():
    parser = argparse.ArgumentParser(
        description="Find and download reference genomes from the NCBI")
    parser.add_argument(
        "-n", "--name",
        type=str,
        required=True,
        help="Scientific name of the species of interest")
    args = parser.parse_args()

    find_reference_genomes.find_reference_genomes(args.name)
