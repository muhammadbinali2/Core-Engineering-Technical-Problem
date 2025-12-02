# O(1) Time Complexity: The function performs a fixed number of arithmetic operations
# and comparisons, independent of the input values' magnitude, making it constant time.

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Dispatches a package to the correct stack (STANDARD, SPECIAL, or REJECTED)
    based on its volume and mass.

    Units: dimensions in cm, mass in kg.

    Args:
        width: Package width (cm).
        height: Package height (cm).
        length: Package length (cm).
        mass: Package mass (kg).

    Returns:
        The name of the stack: 'STANDARD', 'SPECIAL', or 'REJECTED'.
    """
    # 1. Determine Bulky Status
    volume = width * height * length
    is_bulky_by_volume = volume >= 1_000_000 # 1,000,000 cm³
    is_bulky_by_dimension = (width >= 150 or height >= 150 or length >= 150)

    is_bulky = is_bulky_by_volume or is_bulky_by_dimension

    # 2. Determine Heavy Status
    is_heavy = mass >= 20 # 20 kg

    # 3. Dispatch to Stack based on combined criteria
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        # Either bulky OR heavy, but not both (due to the first 'if')
        return "SPECIAL"
    else:
        # Neither bulky nor heavy
        return "STANDARD"

# --- Testing / Examples ---

if __name__ == "__main__":
    print("--- Package Sorting Test Cases ---")

    # Case 1: STANDARD (Not bulky, Not heavy)
    # Volume: 10*10*10 = 1000 (< 1,000,000). Max Dim: 10 (< 150). Mass: 5 (< 20).
    standard_result = sort(10, 10, 10, 5)
    print(f"1. STANDARD (10, 10, 10, 5) -> {standard_result} (Expected: STANDARD)")

    # Case 2: SPECIAL (Bulky ONLY - by Dimension)
    # Volume: 160*10*10 = 16,000 (< 1,000,000). Max Dim: 160 (>= 150). Mass: 5 (< 20).
    special_bulky_dim = sort(160, 10, 10, 5)
    print(f"2. SPECIAL (160, 10, 10, 5) -> {special_bulky_dim} (Expected: SPECIAL)")

    # Case 3: SPECIAL (Bulky ONLY - by Volume)
    # Volume: 100*100*100 = 1,000,000 (>= 1,000,000). Max Dim: 100 (< 150). Mass: 5 (< 20).
    special_bulky_vol = sort(100, 100, 100, 5)
    print(f"3. SPECIAL (100, 100, 100, 5) -> {special_bulky_vol} (Expected: SPECIAL)")

    # Case 4: SPECIAL (Heavy ONLY)
    # Volume: 10*10*10 = 1000. Max Dim: 10. Mass: 25 (>= 20).
    special_heavy = sort(10, 10, 10, 25)
    print(f"4. SPECIAL (10, 10, 10, 25) -> {special_heavy} (Expected: SPECIAL)")

    # Case 5: REJECTED (Bulky AND Heavy)
    # Bulky by Volume. Heavy.
    rejected_both = sort(100, 100, 100, 20)
    print(f"5. REJECTED (100, 100, 100, 20) -> {rejected_both} (Expected: REJECTED)")

    # Case 6: REJECTED (Bulky by Dimension AND Heavy)
    # Bulky by Dimension (150). Heavy.
    rejected_dim = sort(150, 10, 10, 30)
    print(f"6. REJECTED (150, 10, 10, 30) -> {rejected_dim} (Expected: REJECTED)")
