def psi_to_pascal(psi):
    return psi * 1.2

print(f"[conversions.py] __name__ = {__name__}")

if __name__ == '__main__':
    print(f"[conversions.py] Running tests ...")
    # Use Case: Implement Test Cases for the module!!

    psi_to_pascal(1.5)
    
else:
    print(f"[conversions.py] Omitting tests ...")