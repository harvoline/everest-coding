# Delivery Time Calculator

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
delivery_time
```

## Usage

To run the script, simply execute the `delivery_time` command in your Python environment. The script will prompt you to enter the following information:

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
Please enter the number of vehicles available: 2
Please enter the maximum speed for all the vehicles (in km/h): 70
Enter the maximum weight that a delivery vehicle can carry: 200

Package 1:
Enter the package ID: PKG1
Enter the package weight: 50
Enter the package distance: 30
Enter the offer code (if any): OFR001

Package 2:
Enter the package ID: PKG2
Enter the package weight: 75
Enter the package distance: 125
Enter the offer code (if any): OFR008

Package 3:
Enter the package ID: PKG3
Enter the package weight: 175
Enter the package distance: 100
Enter the offer code (if any): OFR003

Package 4:
Enter the package ID: PKG4
Enter the package weight: 110
Enter the package distance: 60
Enter the offer code (if any): OFR002

Package 5:
Enter the package ID: PKG5
Enter the package weight: 155
Enter the package distance: 95
Enter the offer code (if any): NA

+------------+----------+------------+--------+----------+------------------------+-------------------------+
| Package ID | Discount | Total Cost | Weight | Distance | Estimate Delivery Time | Final Est Delivery Time |
+------------+----------+------------+--------+----------+------------------------+-------------------------+
|    PKG2    |   0.0    |   1475.0   |  75.0  |   125    |          1.78          |           1.78          |
|    PKG4    |  105.0   |   1395.0   | 110.0  |    60    |          0.85          |           0.85          |
|    PKG3    |   0.0    |   2350.0   | 175.0  |   100    |          1.42          |           1.42          |
|    PKG5    |   0.0    |   2125.0   | 155.0  |    95    |          1.35          |           4.18          |
|    PKG1    |   0.0    |   750.0    |  50.0  |    30    |          0.42          |           3.98          |
+------------+----------+------------+--------+----------+------------------------+-------------------------+


```

## License

[MIT](https://choosealicense.com/licenses/mit/)