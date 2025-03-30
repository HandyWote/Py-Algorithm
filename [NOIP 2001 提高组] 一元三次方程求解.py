a, b, c, d = map(float, input().split())

def f(x):
    return a * x**3 + b * x**2 + c * x + d

roots = []
step = 0.5
x = -100.0

while x <= 99.5:
    x1 = x
    x2 = x + step
    f1 = f(x1)
    f2 = f(x2)

    # Check if x1 is a root
    if abs(f1) < 1e-6:
        # Check if already in roots
        found = False
        for root in roots:
            if abs(root - x1) < 1e-6:
                found = True
                break
        if not found:
            roots.append(x1)
    
    # Check if x2 is a root
    if abs(f2) < 1e-6:
        found = False
        for root in roots:
            if abs(root - x2) < 1e-6:
                found = True
                break
        if not found:
            roots.append(x2)
    
    # Check if there's a root in [x1, x2]
    if f1 * f2 < 0:
        left, right = x1, x2
        for _ in range(100):
            mid = (left + right) / 2
            f_mid = f(mid)
            if abs(f_mid) < 1e-6:
                break
            if f_mid * f1 < 0:
                right = mid
            else:
                left = mid
        root = (left + right) / 2
        # Check if root is already in the list
        found = False
        for r in roots:
            if abs(r - root) < 1e-6:
                found = True
                break
        if not found:
            roots.append(root)
    
    x += step

# Sort the roots
roots.sort()

# Format to two decimal places
formatted_roots = [f"{root:.2f}" for root in roots]
print(" ".join(formatted_roots))