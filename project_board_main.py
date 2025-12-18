import pytest
from project_intergration.Common.intergration_path import base_dir, reports_dir

pytest.main([base_dir, "--reruns", "1", "--reruns-delay", "3", "--alluredir={}".format(reports_dir), "--clean-alluredir"])
