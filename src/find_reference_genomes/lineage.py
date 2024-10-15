class Lineage:
    def __init__(self, lineages: str, ranks: str):
        self.pairs = []

        lineages_list = lineages.split(";")
        ranks_list = ranks.split(";")
        for i, (lineage, rank) in enumerate(zip(lineages_list, ranks_list)):
            self.pairs.append((lineage, rank))


class LineageRankPair():
    def __init__(self, lineage, rank):
        self.lineage = lineage
        self.rank = rank
