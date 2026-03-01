"""
Test suite for the Scientific Calculator skill
"""

from scientific_calculator import scientific_calculator_skill

def test_basic_operations():
    """Test basic arithmetic operations."""
    print("Testing basic operations...")

    # Addition
    result = scientific_calculator_skill("2 + 3")
    assert result["result"] == 5, f"Expected 5, got {result['result']}"
    print("✓ Addition works")

    # Multiplication
    result = scientific_calculator_skill("4 * 5")
    assert result["result"] == 20, f"Expected 20, got {result['result']}"
    print("✓ Multiplication works")

    # Exponentiation
    result = scientific_calculator_skill("2 ^ 8")
    assert result["result"] == 256, f"Expected 256, got {result['result']}"
    print("✓ Exponentiation works")

    # Division
    result = scientific_calculator_skill("15 / 3")
    assert result["result"] == 5, f"Expected 5, got {result['result']}"
    print("✓ Division works")


def test_trigonometric_functions():
    """Test trigonometric functions."""
    print("\nTesting trigonometric functions...")

    # sin(pi/2) should be approximately 1
    result = scientific_calculator_skill("sin(pi/2)")
    assert abs(result["result"] - 1.0) < 0.0001, f"Expected ~1.0, got {result['result']}"
    print("✓ Sine function works")

    # cos(0) should be 1
    result = scientific_calculator_skill("cos(0)")
    assert abs(result["result"] - 1.0) < 0.0001, f"Expected ~1.0, got {result['result']}"
    print("✓ Cosine function works")

    # tan(pi/4) should be approximately 1
    result = scientific_calculator_skill("tan(pi/4)")
    assert abs(result["result"] - 1.0) < 0.0001, f"Expected ~1.0, got {result['result']}"
    print("✓ Tangent function works")


def test_logarithmic_functions():
    """Test logarithmic functions."""
    print("\nTesting logarithmic functions...")

    # log(100) base 10 should be 2
    result = scientific_calculator_skill("log10(100)")
    assert result["result"] == 2.0, f"Expected 2.0, got {result['result']}"
    print("✓ Log base 10 works")

    # Natural log of e should be 1
    result = scientific_calculator_skill("log(e)")
    assert abs(result["result"] - 1.0) < 0.0001, f"Expected ~1.0, got {result['result']}"
    print("✓ Natural logarithm works")


def test_square_root():
    """Test square root function."""
    print("\nTesting square root function...")

    result = scientific_calculator_skill("sqrt(16)")
    assert result["result"] == 4.0, f"Expected 4.0, got {result['result']}"
    print("✓ Square root works")


def test_factorial():
    """Test factorial function."""
    print("\nTesting factorial function...")

    result = scientific_calculator_skill("factorial 5")
    assert result["result"] == 120, f"Expected 120, got {result['result']}"
    print("✓ Factorial works")


def test_quadratic_solver():
    """Test quadratic equation solver."""
    print("\nTesting quadratic equation solver...")

    # x² - 5x + 6 = 0, roots are 2 and 3
    result = scientific_calculator_skill("quadratic 1 -5 6")
    roots = result["result"]
    # Check if roots are approximately 2 and 3
    root_values = [float(root) for root in roots]
    assert 2.0 in root_values or abs(root_values[0] - 2.0) < 0.0001 or abs(root_values[1] - 2.0) < 0.0001
    assert 3.0 in root_values or abs(root_values[0] - 3.0) < 0.0001 or abs(root_values[1] - 3.0) < 0.0001
    print("✓ Quadratic solver works")


def test_permutation_combination():
    """Test permutation and combination functions."""
    print("\nTesting permutation and combination...")

    # P(5,3) = 5!/(5-3)! = 5!/2! = 60
    result = scientific_calculator_skill("permutation 5 3")
    assert result["result"] == 60, f"Expected 60, got {result['result']}"
    print("✓ Permutation works")

    # C(5,3) = 5!/(3!*2!) = 10
    result = scientific_calculator_skill("combination 5 3")
    assert result["result"] == 10, f"Expected 10, got {result['result']}"
    print("✓ Combination works")


def test_memory_operations():
    """Test memory functions."""
    print("\nTesting memory operations...")

    # Store value in memory
    result = scientific_calculator_skill("memory store 42")
    assert result["success"] == True
    print("✓ Memory store works")

    # Recall value from memory
    result = scientific_calculator_skill("memory recall")
    assert result["result"] == 42, f"Expected 42, got {result['result']}"
    print("✓ Memory recall works")

    # Add to memory
    result = scientific_calculator_skill("memory add 8")
    result = scientific_calculator_skill("memory recall")
    assert result["result"] == 50, f"Expected 50, got {result['result']}"
    print("✓ Memory add works")


def run_all_tests():
    """Run all tests."""
    print("Running Scientific Calculator Skill Tests...\n")

    try:
        test_basic_operations()
        test_trigonometric_functions()
        test_logarithmic_functions()
        test_square_root()
        test_factorial()
        test_quadratic_solver()
        test_permutation_combination()
        test_memory_operations()

        print("\n🎉 All tests passed! The Scientific Calculator skill is working correctly.")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n💥 An error occurred during testing: {e}")


if __name__ == "__main__":
    run_all_tests()