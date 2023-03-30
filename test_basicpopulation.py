import pytest
import os
from population import population_change



@pytest.fixture
def population_file(tmpdir):
    file_content = "Ukraine,2021,44000000" \
                   "\nUkraine,2010,46000000" \
                   "\nUSA,2021,308000000" \
                   "\nUSA,2010,330000000" \
                   "\nChina,2021,1400000000"
    f = tmpdir.join("population.txt")
    f.write(file_content)
    return f


@pytest.fixture
def expected_result():
    return {"Ukraine": 2000000, "USA": 22000000}


def test_population_change(population_file, expected_result):
    assert population_change(population_file) == expected_result


def test_population_change_missing_file():
    with pytest.raises(FileNotFoundError):
        population_change("missing_file.txt")
