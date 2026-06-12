from find_reference_genomes.main import parse_assembly_report

# Trimmed real NCBI assembly_report.txt rows (tab-separated).
HUMAN = "\n".join([
    "# Sequence-Name\tSequence-Role\tAssigned-Molecule\tAssigned-Molecule-Location/Type\tGenBank-Accn\tRelationship\tRefSeq-Accn\tAssembly-Unit\tSequence-Length\tUCSC-style-name",
    "1\tassembled-molecule\t1\tChromosome\tCM000663.2\t=\tNC_000001.11\tPrimary Assembly\t248956422\tchr1",
    "X\tassembled-molecule\tX\tChromosome\tCM000685.2\t=\tNC_000023.11\tPrimary Assembly\t156040895\tchrX",
    "HSCHRUN_RANDOM_CTG1\tunplaced-scaffold\tna\tna\tGL000195.1\t=\tNT_113901.1\tPrimary Assembly\t182896\tchrUn_GL000195v1",
])

# Yeast mitochondrion: GenBank-Accn is "na", only RefSeq is usable.
YEAST_MT = "MT\tassembled-molecule\tMT\tMitochondrion\tna\t<>\tNC_001224.1\tnon-nuclear\t85779\tchrM"


def test_maps_both_genbank_and_refseq_to_chromosome():
    m = parse_assembly_report(HUMAN)
    assert m["CM000663.2"] == "1"
    assert m["NC_000001.11"] == "1"
    assert m["CM000685.2"] == "X"


def test_scaffolds_are_skipped():
    m = parse_assembly_report(HUMAN)
    assert "GL000195.1" not in m
    assert "NT_113901.1" not in m


def test_na_accession_is_skipped_but_other_column_kept():
    m = parse_assembly_report(YEAST_MT)
    assert "na" not in m
    assert m["NC_001224.1"] == "MT"
