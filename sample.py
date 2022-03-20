from buildTable import texTable
import pandas as pd
import numpy as np

if __name__ == "__main__":
    pandas_table = pd.DataFrame({'Rows':['rowA','rowB','rowC'],
                    'colA':[2,3,5],
                    'colB':[4,5,6]}).set_index(['Rows'])


    np_table = np.array([[2,3,5],[4,5,6]])
    np_additional = np.random.random((2,3))
    np_row_names = ['rowA','rowB']
    np_col_names = ['colA','colB','colC']

    tableFromNp = texTable(
        source=np_table,
        row=np_row_names,
        col=np_col_names,
        bold_max=True,
        aggregation=True,
        aggr_target=np_additional)
    tableFromNp.build_tex(path = 'np_to_tex_table.tex')
    exit(0)