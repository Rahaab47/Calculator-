"""
Advanced Scientific Calculator Skill

This skill provides a comprehensive scientific calculator with the latest mathematical functions,
including trigonometry, logarithms, exponentials, statistics, and advanced operations.
"""

import math
import cmath
import statistics
from typing import Union, List, Tuple
import re

class ScientificCalculator:
    """
    A comprehensive scientific calculator implementing the latest mathematical features.
    """

    def __init__(self):
        self.history = []
        self.memory = 0

    def calculate(self, expression: str) -> float:
        """
        Safely evaluate a mathematical expression with support for advanced functions.

        Args:
            expression: Mathematical expression as a string

        Returns:
            Result of the calculation
        """
        # Store original expression
        original_expr = expression

        # Replace common math functions with Python equivalents
        expression = self._preprocess_expression(expression)

        try:
            # Use eval safely by restricting available functions
            allowed_names = {
                "__builtins__": {},
                "abs": abs, "round": round, "pow": pow,
                "min": min, "max": max, "sum": sum,
                # Math functions
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "asin": math.asin, "acos": math.acos, "atan": math.atan,
                "atan2": math.atan2, "sinh": math.sinh, "cosh": math.cosh,
                "tanh": math.tanh, "asinh": math.asinh, "acosh": math.acosh,
                "atanh": math.atanh, "exp": math.exp, "log": math.log,
                "log10": math.log10, "log2": math.log2, "sqrt": math.sqrt,
                "ceil": math.ceil, "floor": math.floor, "factorial": math.factorial,
                "degrees": math.degrees, "radians": math.radians,
                "gcd": math.gcd, "lcm": math.lcm if hasattr(math, 'lcm') else self._lcm,
                "pi": math.pi, "e": math.e, "tau": math.tau,
                "inf": math.inf, "nan": math.nan,
                # Complex number support
                "phase": cmath.phase, "polar": cmath.polar,
                "rect": cmath.rect, "exp": cmath.exp, "log": cmath.log,
                "sqrt": cmath.sqrt, "sin": cmath.sin, "cos": cmath.cos,
                "tan": cmath.tan,
                # Statistics functions
                "mean": statistics.mean, "median": statistics.median,
                "mode": statistics.mode, "stdev": statistics.stdev,
                "variance": statistics.variance, "harmonic_mean": statistics.harmonic_mean,
                "geometric_mean": statistics.geometric_mean,
            }

            result = eval(expression, allowed_names)

            # Store in history
            self.history.append((original_expr, result))

            return result
        except Exception as e:
            raise ValueError(f"Invalid expression '{expression}': {str(e)}")

    def _preprocess_expression(self, expr: str) -> str:
        """Convert common math notation to Python equivalents."""
        # Replace common functions with Python equivalents
        replacements = [
            (r'\^', '**'),  # Power operator
            (r'sin\(', 'math.sin('),
            (r'cos\(', 'math.cos('),
            (r'tan\(', 'math.tan('),
            (r'asin\(', 'math.asin('),
            (r'acos\(', 'math.acos('),
            (r'atan\(', 'math.atan('),
            (r'sqrt\(', 'math.sqrt('),
            (r'log\(', 'math.log('),
            (r'ln\(', 'math.log('),
            (r'log10\(', 'math.log10('),
            (r'exp\(', 'math.exp('),
            (r'abs\(', 'abs('),
            (r'round\(', 'round('),
            (r'ceil\(', 'math.ceil('),
            (r'floor\(', 'math.floor('),
            (r'factorial\(', 'math.factorial('),
            (r'degrees\(', 'math.degrees('),
            (r'radians\(', 'math.radians('),
        ]

        processed_expr = expr
        for pattern, replacement in replacements:
            processed_expr = re.sub(pattern, replacement, processed_expr)

        return processed_expr

    def _lcm(self, a: int, b: int) -> int:
        """Calculate least common multiple for older Python versions."""
        return abs(a * b) // math.gcd(a, b)

    def solve_quadratic(self, a: float, b: float, c: float) -> Union[Tuple[complex, complex], Tuple[float, float]]:
        """
        Solve quadratic equation ax² + bx + c = 0

        Args:
            a, b, c: Coefficients of the quadratic equation

        Returns:
            Tuple of roots (real or complex)
        """
        discriminant = b**2 - 4*a*c

        if discriminant >= 0:
            sqrt_discriminant = math.sqrt(discriminant)
            root1 = (-b + sqrt_discriminant) / (2*a)
            root2 = (-b - sqrt_discriminant) / (2*a)
            return (root1, root2)
        else:
            sqrt_discriminant = cmath.sqrt(discriminant)
            root1 = (-b + sqrt_discriminant) / (2*a)
            root2 = (-b - sqrt_discriminant) / (2*a)
            return (root1, root2)

    def factorial(self, n: int) -> int:
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    def permutation(self, n: int, r: int) -> int:
        """Calculate permutation P(n,r) = n!/(n-r)!"""
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid values for permutation calculation")
        return math.factorial(n) // math.factorial(n - r)

    def combination(self, n: int, r: int) -> int:
        """Calculate combination C(n,r) = n!/(r!(n-r)!)"""
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid values for combination calculation")
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

    def matrix_multiply(self, matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
        """Multiply two matrices."""
        rows_a, cols_a = len(matrix_a), len(matrix_a[0])
        rows_b, cols_b = len(matrix_b), len(matrix_b[0])

        if cols_a != rows_b:
            raise ValueError("Cannot multiply matrices: incompatible dimensions")

        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return result

    def derivative_approximation(self, func_str: str, x: float, h: float = 1e-7) -> float:
        """
        Approximate the derivative of a function at point x using finite differences.

        Args:
            func_str: Function as a string (e.g., "x**2 + 3*x + 1")
            x: Point at which to calculate the derivative
            h: Small value for approximation

        Returns:
            Approximated derivative value
        """
        calc = ScientificCalculator()

        # Calculate f(x+h) and f(x-h)
        expr_h_pos = func_str.replace('x', f'({x+h})')
        expr_h_neg = func_str.replace('x', f'({x-h})')

        fx_plus_h = calc.calculate(expr_h_pos)
        fx_minus_h = calc.calculate(expr_h_neg)

        # Central difference formula: f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        return (fx_plus_h - fx_minus_h) / (2 * h)

    def integral_approximation(self, func_str: str, a: float, b: float, n: int = 1000) -> float:
        """
        Approximate the definite integral using the trapezoidal rule.

        Args:
            func_str: Function as a string to integrate
            a, b: Integration bounds
            n: Number of intervals (higher = more accurate)

        Returns:
            Approximated integral value
        """
        calc = ScientificCalculator()
        h = (b - a) / n

        # Calculate f(a) and f(b)
        fa = calc.calculate(func_str.replace('x', f'({a})'))
        fb = calc.calculate(func_str.replace('x', f'({b})'))

        # Sum the intermediate values
        sum_intermediate = 0
        for i in range(1, n):
            xi = a + i * h
            fxi = calc.calculate(func_str.replace('x', f'({xi})'))
            sum_intermediate += fxi

        # Trapezoidal rule: ∫ ≈ h/2 * [f(a) + 2*∑f(xi) + f(b)]
        return h / 2 * (fa + 2 * sum_intermediate + fb)

    def get_history(self) -> List[Tuple[str, float]]:
        """Return calculation history."""
        return self.history.copy()

    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()

    def memory_store(self, value: float):
        """Store value in memory."""
        self.memory = value

    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory

    def memory_clear(self):
        """Clear memory."""
        self.memory = 0

    def memory_add(self, value: float):
        """Add value to memory."""
        self.memory += value

    def memory_subtract(self, value: float):
        """Subtract value from memory."""
        self.memory -= value


def scientific_calculator_skill(input_text: str) -> dict:
    """
    Main skill function for the scientific calculator.

    Args:
        input_text: Input containing the calculation to perform

    Returns:
        Dictionary with result and metadata
    """
    calc = ScientificCalculator()

    try:
        # Parse the input to determine what operation to perform
        input_lower = input_text.lower().strip()

        if input_lower.startswith("calculate ") or input_lower.startswith("eval "):
            expression = input_text.split(" ", 1)[1]
            result = calc.calculate(expression)
            return {
                "result": result,
                "type": "calculation",
                "expression": expression,
                "success": True
            }

        elif input_lower.startswith("quadratic "):
            # Parse coefficients: "quadratic 1 5 6" for x² + 5x + 6 = 0
            parts = input_text.split()
            if len(parts) != 4:
                raise ValueError("Quadratic equation requires 3 coefficients: a, b, c")
            a, b, c = float(parts[1]), float(parts[2]), float(parts[3])
            roots = calc.solve_quadratic(a, b, c)
            return {
                "result": roots,
                "type": "quadratic_solution",
                "equation": f"{a}x² + {b}x + {c} = 0",
                "success": True
            }

        elif input_lower.startswith("factorial "):
            n = int(input_text.split()[1])
            result = calc.factorial(n)
            return {
                "result": result,
                "type": "factorial",
                "input": n,
                "success": True
            }

        elif input_lower.startswith("permutation "):
            parts = input_text.split()
            if len(parts) != 3:
                raise ValueError("Permutation requires 2 values: n r")
            n, r = int(parts[1]), int(parts[2])
            result = calc.permutation(n, r)
            return {
                "result": result,
                "type": "permutation",
                "input": (n, r),
                "success": True
            }

        elif input_lower.startswith("combination "):
            parts = input_text.split()
            if len(parts) != 3:
                raise ValueError("Combination requires 2 values: n r")
            n, r = int(parts[1]), int(parts[2])
            result = calc.combination(n, r)
            return {
                "result": result,
                "type": "combination",
                "input": (n, r),
                "success": True
            }

        elif input_lower.startswith("derivative "):
            # Format: "derivative x**2 + 3*x + 1 at 2"
            parts = input_text.split(" at ")
            if len(parts) != 2:
                raise ValueError("Derivative requires function and point: 'function' at x")

            func_str = parts[0].replace("derivative ", "").strip()
            x = float(parts[1])
            result = calc.derivative_approximation(func_str, x)
            return {
                "result": result,
                "type": "derivative",
                "function": func_str,
                "point": x,
                "success": True
            }

        elif input_lower.startswith("integral "):
            # Format: "integral x**2 from 0 to 2"
            import re
            match = re.search(r'integral (.+?) from ([\d.-]+) to ([\d.-]+)', input_text)
            if not match:
                raise ValueError("Integral format: 'integral function from a to b'")

            func_str = match.group(1)
            a, b = float(match.group(2)), float(match.group(3))
            result = calc.integral_approximation(func_str, a, b)
            return {
                "result": result,
                "type": "integral",
                "function": func_str,
                "bounds": (a, b),
                "success": True
            }

        elif input_lower == "history":
            history = calc.get_history()
            return {
                "result": history,
                "type": "history",
                "success": True
            }

        elif input_lower == "clear history":
            calc.clear_history()
            return {
                "result": "History cleared",
                "type": "clear_history",
                "success": True
            }

        elif input_lower.startswith("memory"):
            if "store" in input_lower:
                value = float(input_text.split()[-1])
                calc.memory_store(value)
                return {
                    "result": f"Stored {value} in memory",
                    "type": "memory_store",
                    "success": True
                }
            elif "recall" in input_lower:
                value = calc.memory_recall()
                return {
                    "result": value,
                    "type": "memory_recall",
                    "success": True
                }
            elif "clear" in input_lower:
                calc.memory_clear()
                return {
                    "result": "Memory cleared",
                    "type": "memory_clear",
                    "success": True
                }
            elif "add" in input_lower:
                value = float(input_text.split()[-1])
                calc.memory_add(value)
                return {
                    "result": f"Added {value} to memory",
                    "type": "memory_add",
                    "success": True
                }
            elif "subtract" in input_lower:
                value = float(input_text.split()[-1])
                calc.memory_subtract(value)
                return {
                    "result": f"Subtracted {value} from memory",
                    "type": "memory_subtract",
                    "success": True
                }
            else:
                return {
                    "result": calc.memory,
                    "type": "memory_status",
                    "success": True
                }

        else:
            # Assume it's a direct calculation
            result = calc.calculate(input_text)
            return {
                "result": result,
                "type": "direct_calculation",
                "expression": input_text,
                "success": True
            }

    except Exception as e:
        return {
            "result": str(e),
            "type": "error",
            "success": False
        }


if __name__ == "__main__":
    # Example usage
    print("Scientific Calculator Skill")
    print("=" * 30)

    # Basic calculations
    print(scientific_calculator_skill("2 + 3 * 4"))
    print(scientific_calculator_skill("sin(pi/2)"))
    print(scientific_calculator_skill("sqrt(16)"))

    # Quadratic equation
    print(scientific_calculator_skill("quadratic 1 -5 6"))  # x² - 5x + 6 = 0

    # Factorial
    print(scientific_calculator_skill("factorial 5"))

    # Permutation and combination
    print(scientific_calculator_skill("permutation 5 3"))
    print(scientific_calculator_skill("combination 5 3"))

    # Derivative
    print(scientific_calculator_skill("derivative x**2 + 3*x + 1 at 2"))

    # Integral
    print(scientific_calculator_skill("integral x**2 from 0 to 2"))

    # Memory operations
    print(scientific_calculator_skill("memory store 42"))
    print(scientific_calculator_skill("memory recall"))