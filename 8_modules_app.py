from 8_modules_sales import calc_shipping, calc_tax
from 8_modules_sales import * # this is not recommend as this may overwite functions or variables in the current module.

calc_shipping()

import 8_modules_sales

8_modules_sales.calc_shipping()


# python search for modules in the following directories:
import sys
import(sys.path)

# import modules in a subdirectory (packages)


