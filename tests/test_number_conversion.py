"""Plugin tests."""

from cmem_plugin_number_conversion.transform import NumberConversion


def test_transform_execution_with_optional_input():
    """Test Lifetime with optional input"""
    result = NumberConversion(source_base="bin", target_base="int").transform(inputs=[])
    assert len(result) == 0


def test_transform_execution_int_to_bin():
    """Test decimal to binary conversion"""
    result = NumberConversion(source_base="int", target_base="bin").transform(
        inputs=[["11", "3"]]
    )
    assert result == ["0b1011", "0b11"]


def test_transform_execution_int_to_int():
    """Test decimal to decimal conversion"""
    result = NumberConversion(source_base="int", target_base="int").transform(
        inputs=[["11", "3"]]
    )
    assert result == ["11", "3"]


def test_transform_execution_bin_to_bin():
    """Test binary to binary conversion"""
    result = NumberConversion(source_base="bin", target_base="bin").transform(
        inputs=[["0b11", "1"]]
    )
    assert result == ["0b11", "0b1"]


def test_transform_execution_bin_to_int():
    """Test binary to decimal conversion"""
    result = NumberConversion(source_base="bin", target_base="int").transform(
        inputs=[["0b11", "1"]]
    )
    assert result == ["3", "1"]


def test_transform_execution_hex_to_oct():
    """Test hex to oct conversion"""
    result = NumberConversion(source_base="hex", target_base="oct").transform(
        inputs=[["0xa", "0x1"]]
    )
    assert result == ["0o12", "0o1"]


def test_transform_execution_oct_to_hex():
    """Test oct to hex conversion"""
    result = NumberConversion(source_base="oct", target_base="hex").transform(
        inputs=[["0o12", "0o1"]]
    )
    assert result == ["0xa", "0x1"]
