from pyspi.utils import filter_spis
import pytest

def test_filter_spis_invalid_keywords():
    """Pass in a dataype other than a list for the keywords"""
    with pytest.raises(TypeError) as excinfo:
        filter_spis("pyspi/config.yaml", "linear")
    assert "Keywords must be passed as a list" in str(excinfo.value), "Keywords must be passed as list error not shown."

def test_filter_spis_with_invalid_config():
    """Pass in an invalid/missing config file"""
    with pytest.raises(FileNotFoundError):
        filter_spis("invalid_config.yaml", ["test"])


