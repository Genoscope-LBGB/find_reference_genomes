import json
import subprocess
import sys

from find_reference_genomes.genome import Genome
from find_reference_genomes.lineage import Lineage


def find_reference_genomes(name: str):
    taxo = Lineage(*get_lineage(name))

    genomes = []
    for i, (node, rank) in enumerate(taxo):
        if rank in ["no_rank", "superkingdom", "kingdom", "phylum"]:
            break

        new_genomes = get_genomes(node, rank)
        for genome in new_genomes:
            if not is_already_in_set(genomes, genome):
                genomes.append(genome)

    print("Organism,Rank,Bioproject,Assembly_level,Cumul_size,scaffold_n50")
    for genome in genomes:
        print(genome)


def get_lineage(name: str) -> str:
    _, _, lineage, ranks = run_taxonkit(name).rstrip("\n").split("\t")
    if len(lineage) == 0:
        raise ValueError(f"Lineage not found for organism: '{name}'. Please check the spelling.")
    return (lineage, ranks)


def run_taxonkit(name: str) -> str:
    echo_name = subprocess.Popen(["echo", name], stdout=subprocess.PIPE)
    taxonkit_name2taxid = subprocess.Popen(
        ["taxonkit", "name2taxid"],
        stdin=echo_name.stdout,
        stdout=subprocess.PIPE,
    )
    taxonkit_lineage = subprocess.Popen(
        ["taxonkit", "lineage", "-i", "2", "-R"],
        stdin=taxonkit_name2taxid.stdout,
        stdout=subprocess.PIPE,
    )
    echo_name.wait()
    taxonkit_name2taxid.wait()
    out = taxonkit_lineage.communicate()[0]

    if taxonkit_lineage.returncode != 0:
        sys.exit(taxonkit_lineage.returncode)

    echo_name.stdout.close()
    taxonkit_name2taxid.stdout.close()
    taxonkit_lineage.stdout.close()

    return out.decode("utf-8")


def get_genomes(node, rank):
    genomes = []

    ncbi_datasets = run_ncbi_dataset(node)
    for report in ncbi_datasets["reports"]:
        name = report["assembly_info"]["biosample"]["description"]["organism"]["organism_name"]
        bioproject = report["assembly_info"]["bioproject_accession"]
        assembly_level = report["assembly_info"]["assembly_level"]
        sequence_length = report["assembly_stats"]["total_sequence_length"]
        scaffold_n50 = report["assembly_stats"]["scaffold_n50"]
        genomes.append(Genome(name, rank, bioproject, assembly_level, sequence_length, scaffold_n50))

    return genomes


def run_ncbi_dataset(node):
    ncbi_datasets = subprocess.Popen(
        ["datasets", "summary", "genome", "taxon", "--assembly-level", "chromosome,complete,scaffold", "--reference", node],
        stdout=subprocess.PIPE,
    )
    out = ncbi_datasets.communicate()[0]
    if ncbi_datasets.returncode != 0:
        sys.exit(1)
    out_json = json.loads(out.decode("utf-8"))
    # dump_json = json.dumps(out_json, indent=2)
    # print(dump_json)
    return out_json


def is_already_in_set(genomes: list[Genome], genome: Genome):
    for g in genomes:
        if g.bioproject == genome.bioproject:
            return True
    return False
