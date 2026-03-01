# Advanced Scientific Calculator Skill

This skill provides a comprehensive scientific calculator with the latest mathematical functions and features. It supports everything from basic arithmetic to advanced calculus operations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division, exponentiation, modulus
- **Trigonometric Functions**: sin, cos, tan, asin, acos, atan, atan2
- **Hyperbolic Functions**: sinh, cosh, tanh, asinh, acosh, atanh
- **Logarithmic Functions**: Natural log (ln), log base 10, log base 2
- **Exponential Functions**: e^x, arbitrary base exponentiation
- **Root Functions**: Square root, nth root
- **Advanced Mathematics**: Factorial, permutation, combination
- **Equation Solving**: Quadratic equation solver (handles complex roots)
- **Statistical Functions**: Mean, median, mode, standard deviation, variance
- **Calculus Operations**: Numerical derivatives and integrals
- **Complex Numbers**: Support for complex number operations
- **Matrix Operations**: Matrix multiplication and other operations
- **Memory Functions**: Store, recall, clear, add, subtract from memory
- **History Tracking**: Keep track of previous calculations

## Usage Examples

### Basic Calculations
```
calculate 2 + 3 * 4
calculate sin(pi/2)
calculate sqrt(16)
calculate log10(100)
calculate exp(2)  # e^2
```

### Trigonometric Functions
```
calculate cos(pi/3)
calculate tan(pi/4)
calculate asin(0.5)
calculate atan2(1, 1)  # atan(y/x) with proper quadrant
```

### Advanced Functions
```
calculate factorial(5)
calculate sinh(1)
calculate log(10)  # natural log
```

### Quadratic Equations
```
quadratic 1 -5 6  # Solves x² - 5x + 6 = 0
quadratic 1 0 -4  # Solves x² - 4 = 0
```

### Combinatorics
```
permutation 5 3  # P(5,3) = 5!/(5-3)!
combination 5 3  # C(5,3) = 5!/(3!(5-3)!)
```

### Calculus Operations
```
derivative x**2 + 3*x + 1 at 2  # Find derivative at x=2
integral x**2 from 0 to 2       # Definite integral
```

### Statistical Functions
```
calculate mean([1, 2, 3, 4, 5])
calculate median([1, 2, 3, 4, 5])
calculate stdev([1, 2, 3, 4, 5])
```

### Memory Operations
```
memory store 42          # Store value in memory
memory recall            # Retrieve from memory
memory add 8             # Add to memory (42 + 8 = 50)
memory subtract 10       # Subtract from memory (50 - 10 = 40)
memory clear             # Clear memory
```

### History
```
history           # Show calculation history
clear history     # Clear calculation history
```

## Supported Constants
- `pi`: π (3.14159...)
- `e`: Euler's number (2.71828...)
- `tau`: τ (2π)
- `inf`: Infinity
- `nan`: Not a number

## Error Handling
The calculator handles various error conditions:
- Division by zero
- Invalid mathematical operations
- Out of domain function evaluations
- Malformed expressions

## Security
The calculator uses a safe evaluation method that only allows access to approved mathematical functions, preventing code injection.

## Implementation Details
- Uses Python's `math`, `cmath`, and `statistics` libraries
- Implements custom numerical methods for calculus operations
- Supports both real and complex number calculations
- Maintains a history of operations for reference