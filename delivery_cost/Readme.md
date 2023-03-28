# Delivery Cost Calculator

This Python script calculates the estimated delivery cost for a given number of packages based on their weight and distance. The script takes as input the base delivery cost, the number of packages, and the package details. For each package, the user is prompted to input the package ID, weight, distance, and offer code (if any). The script then calculates the total cost of delivery based on the weight, distance, and any applicable discounts.

## Requirements
To run this script, you need to have:
- Python version 3
- Pip

## Instruction

To install the python script:

1. Extract the zip file
2. Change directory to `everest-coding`
3. Run the following command:

```terminal
pip install .
```
** You only need to run this once only. After the installation, you can run both script

4. You can the run the program by running following command:

```terminal
delivery_cost
```

## Usage

To run the script, simply execute the `delivery_cost` command in your Python environment. The script will prompt you to enter the following information:

1. Base delivery cost
2. Number of packages

For each package, the script will prompt you to enter the following information:
1. Package ID
2. Package weight
3. Package distance
4. Offer code (if any)

The script will then calculate the total cost of delivery based on the weight, distance, and any applicable discounts. The final delivery cost will be displayed on the screen.

Sample Input/Output
```python
Enter the base delivery cost: 100
Enter the number of packages: 3

Package 1:
Enter the package ID: PKG1
Enter the package weight: 5
Enter the package distance: 5
Enter the offer code (if any): OFR001

Package 2:
Enter the package ID: PKG2
Enter the package weight: 15
Enter the package distance: 5
Enter the offer code (if any): OFR002

Package 3:
Enter the package ID: PKG3
Enter the package weight: 10
Enter the package distance: 100
Enter the offer code (if any): OFR003

+------------+----------+------------+
| Package ID | Discount | Total Cost |
+------------+----------+------------+
|    PKG1    |    0     |    175     |
|    PKG1    |    0     |    275     |
|    PKG1    |   35.0   |   665.0    |
|    PKG1    |    0     |    2485    |
+------------+----------+------------+

```

## License

[MIT](https://choosealicense.com/licenses/mit/)