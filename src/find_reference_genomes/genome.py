class Genome:
    def __init__(self, name: str, rank: str, accession: str, bioproject: str, assembly_level: str, sequence_length: str, scaffold_n50: str):
        self.name = name
        self.rank = rank
        self.accession = accession
        self.bioproject = bioproject
        self.assembly_level = assembly_level
        self.sequence_length = int(sequence_length)
        self.scaffold_n50 = int(scaffold_n50)

    def __str__(self):
        repr = f"{self.name},{self.rank},{self.accession},{self.bioproject},{self.assembly_level},{self.sequence_length},{self.scaffold_n50}"
        return repr
