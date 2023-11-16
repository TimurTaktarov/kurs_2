from decimal import Decimal


def cm_to_inches(length_cm: float) -> Decimal:
    inches: Decimal = Decimal(length_cm) / Decimal(
        "2.540000000000000000000000000000000000000000000000000000000000"
    )
    rounding = Decimal(str(inches)).quantize(Decimal("0.01"))
    return rounding
