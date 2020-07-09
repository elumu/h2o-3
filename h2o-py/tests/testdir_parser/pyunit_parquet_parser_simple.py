from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils


def parquet_parse_simple():
    """
    Tests Parquet parser by comparing the summary of the original csv frame with the h2o parsed Parquet frame.
    Basic use case of importing files with auto-detection of column types.
    :return: None if passed.  Otherwise, an exception will be thrown.
    """
    parquet = h2o.import_file(path=pyunit_utils.locate("/home/pavel/partitioned_arilines1/"), partitionedBy="Year")
    print(parquet)

if __name__ == "__main__":
    pyunit_utils.standalone_test(parquet_parse_simple)
else:
    parquet_parse_simple()