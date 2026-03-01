# Scientific Calculator Skill

## Overview
The Scientific Calculator Skill is a comprehensive mathematical computation tool that provides advanced scientific calculator functionality. It supports everything from basic arithmetic to complex mathematical operations including trigonometry, calculus, statistics, and more.

## Purpose
This skill enables users to perform complex mathematical calculations directly within the application without needing external calculator tools. It's designed to serve the needs of students, engineers, scientists, and anyone who requires advanced mathematical computations.

## Key Features

### Basic Mathematical Operations
- Addition, subtraction, multiplication, division
- Exponentiation and root extraction
- Modulus operations
- Parentheses for order of operations

### Trigonometric Functions
- Primary functions: sin, cos, tan
- Inverse functions: asin, acos, atan
- Two-argument arctangent: atan2
- Hyperbolic functions: sinh, cosh, tanh

### Logarithmic and Exponential Functions
- Natural logarithm (ln)
- Base-10 logarithm (log10)
- Base-2 logarithm (log2)
- Exponential function (exp)

### Advanced Mathematics
- Factorial calculations
- Permutations and combinations
- Greatest common divisor (GCD)
- Least common multiple (LCM)

### Equation Solving
- Quadratic equation solver with complex root support
- Handles equations of the form ax² + bx + c = 0

### Statistical Functions
- Mean, median, mode
- Standard deviation and variance
- Harmonic and geometric means

### Calculus Operations
- Numerical derivative approximation
- Numerical integration using trapezoidal rule

### Complex Number Support
- Operations with complex numbers
- Phase, polar, and rectangular conversions

### Memory Functions
- Store values in memory
- Recall memory contents
- Add/subtract from memory
- Clear memory

### Calculation History
- Track previous calculations
- Review past results
- Clear history when needed

## Usage Instructions

### Basic Calculations
```
calculate 2 + 3 * 4
calculate sin(pi/2)
calculate sqrt(16)
calculate log10(100)
```

### Trigonometric Functions
```
calculate cos(pi/3)
calculate tan(pi/4)
calculate asin(0.5)
calculate atan2(1, 1)
```

### Equation Solving
```
quadratic 1 -5 6    # Solves x² - 5x + 6 = 0
quadratic 1 0 -4    # Solves x² - 4 = 0
```

### Combinatorics
```
permutation 5 3     # P(5,3) = 5!/(5-3)!
combination 5 3     # C(5,3) = 5!/(3!(5-3)!)
```

### Calculus Operations
```
derivative x**2 + 3*x + 1 at 2    # Find derivative at x=2
integral x**2 from 0 to 2         # Definite integral
```

### Memory Operations
```
memory store 42        # Store value in memory
memory recall          # Retrieve from memory
memory add 8           # Add to memory
memory subtract 10     # Subtract from memory
memory clear           # Clear memory
```

### History Management
```
history               # Show calculation history
clear history         # Clear calculation history
```

## Constants Available
- `pi`: π (3.14159...)
- `e`: Euler's number (2.71828...)
- `tau`: τ (2π)
- `inf`: Infinity
- `nan`: Not a number

## Error Handling
The calculator includes robust error handling for:
- Division by zero
- Invalid mathematical operations
- Out-of-domain function evaluations
- Malformed expressions
- Insufficient parameters for functions

## Security Measures
- Safe evaluation using restricted namespace
- No access to system functions
- Prevents code injection attempts
- Validates all inputs before processing

## Performance Considerations
- Efficient algorithms for common operations
- Numerical methods optimized for accuracy
- Memory-efficient history tracking
- Fast trigonometric and logarithmic calculations

## Integration Points
- Compatible with other mathematical tools
- Returns structured data for further processing
- Supports chaining of operations
- Integrates with statistical analysis tools

## Limitations
- Currently supports single-variable calculus operations
- Matrix operations limited to multiplication
- Complex number support in basic operations only
- No symbolic mathematics (algebraic manipulation)

## Future Enhancements
Potential additions could include:
- Symbolic differentiation and integration
- More advanced matrix operations (determinants, inverses)
- Additional special functions (gamma, beta, etc.)
- Graphing capabilities
- Unit conversion functions

## Troubleshooting
Common issues and solutions:
- If getting "Invalid expression" errors, check parentheses balance
- For trigonometric functions, ensure angles are in radians
- For logarithmic functions, verify the argument is positive
- For inverse trigonometric functions, verify arguments are in domain [-1, 1]

## Examples of Complex Calculations
```
# Calculate compound interest growth
calculate 1000 * exp(0.05 * 10)

# Evaluate a polynomial
calculate 2*(3**2) + 5*3 + 1

# Work with trigonometric identities
calculate sin(pi/6)**2 + cos(pi/6)**2

# Statistical analysis
calculate mean([1, 2, 3, 4, 5])
```

## Support Information
For issues with the calculator skill:
- Verify expression syntax
- Check for proper function names
- Ensure sufficient arguments for functions
- Consult the usage examples above