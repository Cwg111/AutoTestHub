import pytest
from taiga.Common.taiga_path import base_dir, reports_dir

pytest.main(
    [base_dir, "--reruns", "1", "--reruns-delay", "3", "--alluredir={}".format(reports_dir), "--clean-alluredir"])
