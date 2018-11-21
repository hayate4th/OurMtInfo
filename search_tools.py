import pandas as pd


def read_dataset():
    return pd.read_json('data.json')


def get_tuple_by_name(mt_name):
    mt_df = read_dataset()
    try:
        results = mt_df[mt_df.name == mt_name].values[0]
    except:
        try:
            results = mt_df[mt_df.name.str.contains(mt_name)].values
        except:
            return None
    
    return results