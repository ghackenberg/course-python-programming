# Import/export entire submodule
from . import calculations
from . import plotting

# - use the submodules
calculations.calculate()
plotting.plot()

# Import/export specific functions from submodules
from .calculations import calculate
from .plotting import plot

# - use the functions
calculate()
plot()

# Export own function
def test():
    pass

print(f"[analysis/__init__.py] __name__ = {__name__}")

if __name__ == '__main__':
    print(f"[analysis/__init__.py] Running tests ...")
    # Use Case: Implement Test Cases for the module!!

    test()
    
else:
    print(f"[analysis/__init__.py] Omitting tests ...")