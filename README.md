# shopping-cart

(description based on rock-paper-scissors-exercise from Corbin Beckerman)

This is a python based code for a cashier check out. Follow the instructions for instillation and use.

## Set-up

First, you need to create and activate a specific Anaconda environment. Do so through the following method in the command line:

```sh
conda create -n shopping-env python=3.8 # (first time only)
conda activate shopping-env
```

Once the environment is set up, you will then need to install certain packages. Do so by executing the following code, also in the command line:

```sh
pip install -r requirements.txt
```

Once these packages are installed, create a new file titled .env in the root directory of the repository, and write the following code, substituting 0.0875 with whatever rate you desire. Please note that this is the method you need to use. For example, if you wanted a tax rate of 12.5%, you would have to set TAX_RATE to 0.125.

    TAX_RATE=0.0875

## Usage

Start the program by putting the following command into the command line:

```py
python shopping_cart.py
```

Once that command is entered, follow the instructions accordingly- there is an initial instruction that has more details.