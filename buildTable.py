import numpy as np
from pandas import DataFrame
from numpy import ndarray
from typing import List
from pylatex import (
    Document,
    Section,
    Subsection,
    Tabular,
    Math,
    TikZ,
    Axis,
    Plot,
    Figure,
    Matrix,
    Alignat,
)
from pylatex.utils import bold
import os


class texTable:
    def __init__(
        self, source, row: None, col: None, aggregation: bool, additional: None
    ):
        """
        source: numpy ndarray or pandas dataframe
        if source is padndas data frame row names and column names will be set automatically with source dataframe's \
        else source is numpy array row names and column names should be given as python list.
        row: python list for row names
        column: python list for row names
        aggregation: boolean if true, aggregates source values with additional values by +- sign.
        additional: aggregation is given true, aggregates source and additional value.
        """
        if type(source) == DataFrame:
            if row is not None and col is not None:
                msg = "Error pandas DataFrame source does not require row names and column names"
                exit(msg)
        elif type(source) == ndarray:
            if row is None and col is None:
                msg = "Error NumPy ndarray source does not require row names and column names"
                exit(msg)
        else:
            msg = "Error source must be given"
            exit(msg)

        self.source = source
        self.row_names = row
        self.column_names = col

        if aggregation is True:
            if additional is None:
                msg = "if aggregation options is True then additional must be given"
                exit(msg)
            elif type(source) != type(additional):
                msg = "type of source: {} and additional: {} must be same".format(
                    type(source), type(additional)
                )
                exit(msg)

        self.is_aggregate = aggregation
        if self.is_aggregate:
            self.aggr_target = additional

        geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
        self.doc = Document(geometry_options=geometry_options)

        pass
