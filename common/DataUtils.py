import json
from pathlib import Path

import pandas as pd


class DataUtils:

    @classmethod
    def get_path(cls):
        current_path_parent = Path(__file__).resolve().parent.parent
        current_path_parent=str(current_path_parent)
        return current_path_parent
    @classmethod
    def read_excel(cls,excel_file,sheet_name,n=None):
        df=pd.read_excel(DataUtils.get_path()+f"{excel_file}",sheet_name=sheet_name)
        df['data'] = df['data'].apply(lambda x: json.loads(x))
        test_data=list(df.itertuples(index=False,name=None))
        if n is None:
            return test_data
        else:
            return test_data[n-1:n]


if __name__ == '__main__':
    pass



