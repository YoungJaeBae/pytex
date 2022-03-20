# Requirements

numpy
pandas

> ```
> pip install -r requirements.txt
> ```

# How to Use

Build latex table from python file.
Supports numpy ndarray and pandas dataframe.

Numpy nd-array to LaTeX table.

sample

```
from buildTable import texTable
import pandas as pd
import numpy as np


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
tableFromNp.build_tex('np_to_tex_table.tex')
```

result:

```
\begin{document}\\
\begin{table}[!t]\\
\begin{tabular}{cccc}\\
\hline
\text{}&\text{colA}&\text{colB}&\text{colC}\\
\text{rowA}&2$\pm$0.3222&3$\pm$0.5172&\textbf{5$\pm$0.0404}\\
\text{rowB}&4$\pm$0.3044&5$\pm$0.4606&\textbf{6$\pm$0.8175}\\
\hline
\end{tabular}\\
\end{table}\\
\end{document}\\
```

![Alt text](table.png?raw=true "Table")
