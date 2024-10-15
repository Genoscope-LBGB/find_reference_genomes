import subprocess

from find_reference_genomes.lineage import Lineage


def find_reference_genomes(name: str):
    lineage = Lineage(*get_lineage(name))
    print(lineage.pairs)


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

    echo_name.stdout.close()
    taxonkit_name2taxid.stdout.close()
    taxonkit_lineage.stdout.close()

    return out.decode("utf-8")

