"""A few utility functions and variables for preparing homework solutions in notebooks."""

from IPython.display import Latex
import sympy as sp

def formatted_answer(label, symbol):
    """Pretty-print a formatted answer showing label=symbol.
    
    :param label: the (mathematical) variable, written out in LaTeX
    :type label: a string or raw string
    :param symbol: the symbol definition
    :type symbol: a sympy symbol
    """
    
    return Latex("$$" + label + " = " + sp.latex(symbol) + "$$")