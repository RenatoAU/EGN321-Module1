"""Pure functions for calculating rectangular tank volume.
Inputs use feet for length and width and inches for depth.
The returned result is measured in U.S. gallons.
"""

from math import isfinite
from numbers import Real
from typing import Iterable, Sequence


# Conversion factors used by the inherited workbook.
INCHES_PER_FOOT = 12.0
US_GALLONS_PER_CUBIC_FOOT = 7.48052


def _validate_positive_number(value: Real, name: str) -> float:
    """Validate one measurement and return it as a float."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a real number.")

    numeric_value = float(value)

    if not isfinite(numeric_value) or numeric_value <= 0:
        raise ValueError(
            f"{name} must be a finite number greater than zero."
        )

    return numeric_value


def calculate_tank_volume(
    length_ft: Real,
    width_ft: Real,
    depth_in: Real,
) -> float:
    """Calculate rectangular tank volume in U.S. gallons."""
    length_value = _validate_positive_number(length_ft, "length_ft")
    width_value = _validate_positive_number(width_ft, "width_ft")
    depth_value = _validate_positive_number(depth_in, "depth_in")

    # Convert the depth from inches to feet before calculating volume.
    depth_ft = depth_value / INCHES_PER_FOOT

    volume_cubic_ft = length_value * width_value * depth_ft

    return volume_cubic_ft * US_GALLONS_PER_CUBIC_FOOT


def calculate_total_volume(
    measurements: Iterable[Sequence[Real]],
) -> float:
    """Calculate the total volume for multiple tank-fill rows."""
    total_gallons = 0.0
    row_count = 0

    for row_number, measurement in enumerate(measurements, start=1):
        row_count += 1

        try:
            length_ft, width_ft, depth_in = measurement
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Measurement row {row_number} must contain "
                "length_ft, width_ft, and depth_in."
            ) from error

        total_gallons += calculate_tank_volume(
            length_ft,
            width_ft,
            depth_in,
        )

    if row_count == 0:
        raise ValueError("measurements must contain at least one row.")

    return total_gallons
