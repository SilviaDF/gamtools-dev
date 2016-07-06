from .segregation import open_segregation

def get_compaction(segregation_data):
    """Get the compaction of each genomic window from a segregation table

    :param segregation_data: Segregation table generated by gamtools
    :returns: :class:`pandas.DataFrame` giving the compaction of each window
    """

    compaction = segregation_data.sum(axis=1)

    return compaction


def compaction_from_args(args):
    """Helper function to call compaction from doit"""

    segregation_data = open_segregation(args.segregation_file)

    compaction = get_compaction(segregation_data)

    compaction.to_csv(args.output_file, sep='\t')
