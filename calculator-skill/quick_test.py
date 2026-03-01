"""
Quick test of the Scientific Calculator skill
"""
import sys
import os

# Add the skills directory to the path
sys.path.insert(0, os.path.join(os.getcwd(), 'skills'))

from scientific_calculator import scientific_calculator_skill

def quick_test():
    print("Quick Test of Scientific Calculator Skill")
    print("=" * 40)

    # Test basic operations
    tests = [
        ("2 + 3", 5),
        ("4 * 5", 20),
        ("2 ^ 8", 256),
        ("15 / 3", 5),
        ("sqrt(16)", 4),
        ("factorial 5", 120),
        ("log10(100)", 2),
    ]

    print("Testing basic operations...")
    for expr, expected in tests:
        result = scientific_calculator_skill(expr)
        if result["success"]:
            actual = result["result"]
            if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
                match = abs(actual - expected) < 0.0001
            else:
                match = actual == expected

            status = "✓" if match else "✗"
            print(f"{status} {expr} = {actual} (expected {expected})")
        else:
            print(f"✗ {expr} - Error: {result['result']}")

    # Test trigonometric functions
    print("\nTesting trigonometric functions...")
    trig_tests = [
        ("sin(pi/2)", 1.0),
        ("cos(0)", 1.0),
        ("tan(pi/4)", 1.0),
    ]

    for expr, expected in trig_tests:
        result = scientific_calculator_skill(expr)
        if result["success"]:
            actual = result["result"]
            match = abs(actual - expected) < 0.0001
            status = "✓" if match else "✗"
            print(f"{status} {expr} = {actual} (expected ~{expected})")
        else:
            print(f"✗ {expr} - Error: {result['result']}")

    # Test special functions
    print("\nTesting special functions...")
    special_tests = [
        ("factorial 5", 120),
        ("permutation 5 3", 60),
        ("combination 5 3", 10),
    ]

    for expr, expected in special_tests:
        result = scientific_calculator_skill(expr)
        if result["success"]:
            actual = result["result"]
            match = actual == expected
            status = "✓" if match else "✗"
            print(f"{status} {expr} = {actual} (expected {expected})")
        else:
            print(f"✗ {expr} - Error: {result['result']}")

    # Test quadratic solver
    print("\nTesting quadratic solver...")
    quad_result = scientific_calculator_skill("quadratic 1 -5 6")  # x² - 5x + 6 = 0, roots are 2 and 3
    if quad_result["success"]:
        roots = quad_result["result"]
        print(f"✓ quadratic 1 -5 6 = {roots}")
    else:
        print(f"✗ quadratic 1 -5 6 - Error: {quad_result['result']}")

    # Test memory operations
    print("\nTesting memory operations...")
    mem_store = scientific_calculator_skill("memory store 42")
    mem_recall = scientific_calculator_skill("memory recall")
    if mem_store["success"] and mem_recall["success"]:
        print(f"✓ Memory: stored 42, recalled {mem_recall['result']}")
    else:
        print("✗ Memory operations failed")

    print("\nTest completed!")

if __name__ == "__main__":
    quick_test()