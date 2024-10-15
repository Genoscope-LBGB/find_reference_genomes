class Lineage:
    def __init__(self, lineages: str, ranks: str):
        self.pairs = []

        lineages_list = lineages.split(";")
        ranks_list = ranks.split(";")
        for i, (lineage, rank) in enumerate(zip(lineages_list, ranks_list)):
            self.pairs.append((lineage, rank))

    def __iter__(self):
        self.pos = len(self.pairs) - 1
        return self

    def __next__(self):
        if self.pos > 0:
            lineage, rank = self.pairs[self.pos]
            self.pos -= 1
            return (lineage, rank)
        else:
            raise StopIteration


class LineageRankPair():
    def __init__(self, lineage, rank):
        self.lineage = lineage
        self.rank = rank
