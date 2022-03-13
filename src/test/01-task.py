import pandas as pd
from sklearn import datasets
from pathlib import Path

# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -


def make_dataset(product):

    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']

    Path(str(product['data'])).parent.mkdir(exist_ok=True, parents=True)

    df.to_parquet(str(product['data']))


make_dataset(product)
