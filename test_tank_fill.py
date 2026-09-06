"""Automated tests for the tank-fill calculations."""

import pytest

from src.tank_fill import (
    calculate_tank_volume,
    calculate_total_volume,
)


def test_r101_matches_workbook_reference():
    """R-101 should match Tank Fill!G6."""
    result = calculate_tank_volume(
        length_ft=10.0,
        width_ft=6.0,
        depth_in=8.0,
    )

    assert result == pytest.approx(299.2208)


def test_r113_matches_workbook_reference():
    """R-113 should match Tank Fill!G18."""
    result = calculate_tank_volume(
        length_ft=12.0,
        width_ft=5.0,
        depth_in=14.0,
    )

    assert result == pytest.approx(523.6364)


def test_r108_uses_corrected_depth_in_inches():
    """R-108 must use 30 inches when the source says 2.5 feet."""
    result = calculate_tank_volume(
        length_ft=10.0,
        width_ft=6.0,
        depth_in=30.0,
    )

    assert result == pytest.approx(1122.0780)


def test_total_volume_includes_all_workbook_rows():
    """The total must include rows equivalent to G6:G23."""
    workbook_measurements = (
        (10.0, 6.0, 8.0),
        (10.0, 6.0, 10.5),
        (10.0, 6.0, 12.0),
        (10.0, 6.0, 15.0),
        (10.0, 6.0, 18.0),
        (10.0, 6.0, 21.5),
        (10.0, 6.0, 24.0),
        (10.0, 6.0, 2.5),
        (10.0, 6.0, 26.0),
        (10.0, 6.0, 28.5),
        (10.0, 6.0, 30.0),
        (10.0, 6.0, 32.0),
        (12.0, 5.0, 14.0),
        (12.0, 5.0, 16.5),
        (12.0, 5.0, 19.0),
        (12.0, 5.0, 22.0),
        (12.0, 5.0, 25.0),
        (12.0, 5.0, 27.0),
    )

    result = calculate_total_volume(workbook_measurements)

    assert result == pytest.approx(13147.0139)


def test_rejects_zero_length():
    """Zero length is not a valid tank dimension."""
    with pytest.raises(ValueError, match="length_ft"):
        calculate_tank_volume(0.0, 6.0, 8.0)


def test_rejects_negative_depth():
    """Negative depth is not valid."""
    with pytest.raises(ValueError, match="depth_in"):
        calculate_tank_volume(10.0, 6.0, -1.0)


def test_rejects_depth_with_unit_text():
    """The function requires numeric depth in inches."""
    with pytest.raises(ValueError, match="depth_in"):
        calculate_tank_volume(10.0, 6.0, "2.5 ft")
