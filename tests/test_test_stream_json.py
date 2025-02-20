import pyarrow as pa

from datacontract.data_contract import DataContract

datacontract = "fixtures/stream-json/datacontract.yaml"


def test_test_stream_json():
    test_json = {
        "updated_at": "2022-04-20T13:50:34.228811Z",
        "available": 17,
        "location": "18",
        "sku": "9521582929054",
        "null_column": None,
    }
    pydict = {}
    for key in test_json.keys():
        pydict[key] = pa.array([test_json[key]])
    pa_table = pa.Table.from_pydict(pydict)
    data_contract = DataContract(data_contract_file=datacontract, stream_data=pa_table)

    run = data_contract.test()

    print(run)
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)
