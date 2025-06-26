def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sorts a package into the correct stack based on its dimensions and mass.

    Parameters:
        width (float): Width of the package in centimeters (must be > 0)
        height (float): Height of the package in centimeters (must be > 0)
        length (float): Length of the package in centimeters (must be > 0)
        mass (float): Mass of the package in kilograms (must be > 0)

    Returns:
        str: One of 'STANDARD', 'SPECIAL', or 'REJECTED'

    Rules:
        - Bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
        - Heavy: mass >= 20 kg
        - REJECTED: both bulky and heavy
        - SPECIAL: either bulky or heavy (but not both)
        - STANDARD: neither bulky nor heavy

    Raises:
        ValueError: If any input is not a positive number.
    """
    # Input validation
    for value, name in zip([width, height, length, mass], ["width", "height", "length", "mass"]):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{name} must be a positive number. Got {value}.")

    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    # Use a ternary operator as required
    return (
        "REJECTED" if bulky and heavy else
        ("SPECIAL" if bulky or heavy else "STANDARD")
    ) 