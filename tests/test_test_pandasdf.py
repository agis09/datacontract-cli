from datetime import datetime

import pandas as pd

from datacontract.data_contract import DataContract


def test_test_pandasdf():
    df = pd.DataFrame(
        {
            "field_one": ["AB-123-CD", "XY-456-ZZ"],
            "field_two": [15, 20],
            "field_three": [
                datetime.strptime("2024-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
                datetime.strptime("2024-02-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
            ],
        }
    )
    data_contract = DataContract(
        data_contract_file="fixtures/pandasdf/datacontract.yaml",
        pandas_df=df,
    )

    from dask.dataframe import from_pandas
    from dask_sql import Context

    ddf = from_pandas(df, npartitions=1)
    context = Context()

    context.create_table("data", ddf)

    # res = context.sql(
    #     """
    #                 SELECT * FROM data
    #     """
    # )
    # res.compute()

    import pdb

    pdb.set_trace()

    run = data_contract.test()

    print(run.pretty())
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)
