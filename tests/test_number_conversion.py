"""Plugin tests."""
import io

import pytest
from cmem.cmempy.workspace.projects.datasets.dataset import make_new_dataset
from cmem.cmempy.workspace.projects.project import delete_project, make_new_project
from cmem.cmempy.workspace.projects.resources.resource import (
    create_resource,
)

from cmem_plugin_number_conversion.transform import NumberConversion

PROJECT_NAME = "number-conversion_test_project"
DATASET_NAME = "sample_dataset"
RESOURCE_NAME = "sample_dataset.txt"
DATASET_TYPE = "text"


@pytest.fixture
def setup(request):
    """Provides the DI build project incl. assets."""
    make_new_project(PROJECT_NAME)
    make_new_dataset(
        project_name=PROJECT_NAME,
        dataset_name=DATASET_NAME,
        dataset_type=DATASET_TYPE,
        parameters={"file": RESOURCE_NAME},
        autoconfigure=False,
    )
    with io.StringIO("number-conversion plugin sample file.") as response_file:
        create_resource(
            project_name=PROJECT_NAME,
            resource_name=RESOURCE_NAME,
            file_resource=response_file,
            replace=True,
        )

    request.addfinalizer(lambda: delete_project(PROJECT_NAME))


def test_transform_execution_with_optional_input():
    """Test Lifetime with optional input"""
    result = NumberConversion(source_base="bin", target_base="int").transform(inputs=[])
    assert len(result) == 0


def test_transform_execution_int_to_bin():
    """Test Lifetime with sequence of inputs."""
    result = NumberConversion(source_base="int", target_base="bin").transform(
        inputs=[["11", "3"]]
    )
    assert result == ["0b1011", "0b11"]


def test_transform_execution_int_to_int():
    """Test Lifetime with sequence of inputs."""
    result = NumberConversion(source_base="int", target_base="int").transform(
        inputs=[["11", "3"]]
    )
    assert result == ["11", "3"]


def test_transform_execution_bin_to_bin():
    """Test Lifetime with sequence of inputs."""
    result = NumberConversion(source_base="bin", target_base="bin").transform(
        inputs=[["0b11", "1"]]
    )
    assert result == ["0b11", "0b1"]
