import hashlib
import pandas as pd


# %%
def save_csv_with_hash(df, file):
    sha1 = hashlib.sha1()
    sha1.update(df.to_csv(index=False, lineterminator="\n").encode("utf-8"))
    hash_val = sha1.hexdigest()
    file = file + "_" + hash_val + ".csv"
    df.to_csv(file, index=False, lineterminator="\n", mode="x")
