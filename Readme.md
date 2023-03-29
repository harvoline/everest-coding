# Everest Coding - Muhammad Norafif

---

## Instruction

---

To install the python script:

1. Extract the zip file
2. Change directory to `everest-coding`
3. Run the following command:

```terminal
    pip install .
```
** You only need to run this once only. After the installation, you can run both script

** Please check each of the documentation on how to run each of the script. Sample provided to demonstrate how to use it.

## Documentation

---

1. [Delivery Cost](./delivery_cost/Readme.md)
2. [Delivery Time](./delivery_time/Readme.md)

## Test Cases

---

### All Test Cases
To run all the test cases for both module, you can follow the below steps:

1. Change your directory to `everest-coding`
2. Run below command
```commandline
    python -m unittest discover -p "test_*.py"
```

### Individual Test Cases

To run test cases for `delivery_cost` only, please run the following command:
```commandline
    python -m unittest .\delivery_cost\test_delivery_cost.py
    python -m unittest .\delivery_cost\test_delivery_cost_input.py  
```

---

To run test cases for `delivery_time` only, please run the following command:
```commandline
    python -m unittest .\delivery_time\test_delivery_time.py
```

** You can run this from `everest-coding` folder