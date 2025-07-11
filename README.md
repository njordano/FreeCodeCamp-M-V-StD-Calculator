# Mean-Variance-Standard Deviation Calculator

This is my first ever project using Python and NumPy, completed as part of the [freeCodeCamp Data Analysis with Python course]
(https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator).

## Project Description

This program takes a list of 9 numbers, reshapes it into a 3x3 matrix, and calculates the following statistics:
- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

Each statistic is returned in the form of a dictionary, showing the values:
- For each column (axis 0)
- For each row (axis 1)
- For the entire 3x3 matrix

## Example Intput

```python
calculate([0,1,2,3,4,5,6,7,8])

The output will be:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],  
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

This project is part of the freeCodeCamp curriculum and is for educational purposes.
