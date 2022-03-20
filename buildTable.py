import numpy as np
import pandas as pd

from pandas import DataFrame
from numpy import ndarray
from typing import List
import os


class texTable:
    def __init__(
        self, source, row= None, col= None, bold_max:bool = True, 
        aggregation: bool =False, aggr_target= None,decimals:int = 4
        ):

        """
        source: numpy ndarray
        if source is padndas data frame row names and column names will be set automatically with source dataframe's \
        else source is numpy array row names and column names should be given as python list.
        row: python list for row names
        column: python list for row names
        aggregation: boolean if true, aggregates source values with aggr_target values by +- sign.
        aggr_target: aggregation is given true, aggregates source and aggr_target value.
        """
        self.source = source
            
        if isinstance(source, ndarray):
            self.source_type = 'numpy'
            
            if row is None or col is None:
                msg = "Error NumPy ndarray source requires row names and column names"
                exit(msg)
            else:
                self.row_names = row 
                self.col_names = col
                self.col_names.insert(0,'')

        else:
            msg = "Error source must be given in numpy nd array"
            exit(msg)

        if aggregation is True:
            if aggr_target is None:
                msg = "if aggregation options is True then aggr_target must be given"
                exit(msg)
            elif type(source) != type(aggr_target):
                msg = "type of source: {} and aggr_target: {} must be same".format(
                    type(source), type(aggr_target)
                )
                exit(msg)

        self.is_aggregate = aggregation
        if self.is_aggregate:
            self.aggr_target = aggr_target
        self.bold_max = bold_max
        self.decimals = decimals

        return
    
    def _build_latex_table(self,path):

        ncolumns = len(self.col_names)
        nrows = len(self.row_names)
        
        if ncolumns == 0 or nrows == 0:
            exit('source is invalid')

        if self.is_aggregate:
            aggr_n_rows = len(self.aggr_target[:,0])
            aggr_n_cols = len(self.aggr_target[0,:])+1

            if aggr_n_cols != ncolumns or aggr_n_rows != nrows:
                exit('source(column:{},row:{}) and aggregation dimension(column:{},row:{}) not matches'.format(ncolumns,nrows,aggr_n_cols,aggr_n_rows))
        
        
        table_structure = 'c'
        for i in range(ncolumns-1):
            table_structure += 'c'

        with open(path,'w') as f:
            f.write("\\begin{document}\\\\ \n")
            f.write("\\begin{table}[!t]\\\\ \n")
            f.write("\\begin{{tabular}}{{{table_structure}}}\\\\ \n".format(table_structure=table_structure))
            f.write("\\hline\n")
            row = "&".join(["\\text{{{}}}".format(str(x)) for x in self.col_names ]) + "\\\\ \n"
            f.write(row)
            for i in range (nrows):
                row_idx = '\\text{{{}}}&'.format(self.row_names[i])
                if self.is_aggregate:
                    row = "&".join([
                        "{}$\\pm${}".format(str(np.round(x,decimals=self.decimals)),
                        str(np.round(y,decimals=self.decimals)))\
                            for x,y in zip(self.source[i,:], self.aggr_target[i,:])
                        ])
                else:
                    row = "&".join(["{}".format(str(x)) for x  in self.source[i,:] ])
                if self.bold_max:
                    max_idx = np.argmax(self.source[i])
                    print(max_idx)
                    row_splitted = row.split('&')
                    row_splitted[max_idx] = '\\textbf{{{}}}'.format(row_splitted[max_idx])
                    row = '&'.join(row_splitted)
                f.write(row_idx + row + '\\\\'+'\n')
            f.write("\\hline\n")
            f.write("\\end{tabular}\\\\ \n")
            f.write("\\end{table}\\\\ \n")
            f.write("\\end{document}\\\\ \n")
            f.close()

        return
    
    def build_tex(self, path):
        self._build_latex_table(path)


