import time

def fibo(n):
    """Naive recursive Fibonacci (exponential time)."""
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def fiboBottomUp(n):
    """Bottom-up dynamic programming (iterative, O(n) time)."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n+1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1

def fiboTopDown(n, memo=None):
    """Top-down dynamic programming with memoization (O(n) time)."""
    if memo is None:
        memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    memo[n] = fiboTopDown(n-1, memo) + fiboTopDown(n-2, memo)
    return memo[n]

def time_function(func, n, *args, **kwargs):
    """Return (result, execution_time_in_seconds) for a given function and n."""
    start = time.perf_counter()
    result = func(n, *args, **kwargs)
    end = time.perf_counter()
    return result, end - start

# Test values: start small, increase gradually to see differences
test_values = [5, 10, 15, 20, 25, 30, 35]

print("Fibonacci timing comparison (in seconds):")
print("n\tNaive Rec.  \tBottom-Up\t\tTop-Down")
print("-" * 60)

for n in test_values:
    # Skip naive recursion for larger n to avoid extreme slowness
    if n <= 200:
        res_naive, t_naive = time_function(fibo, n)
    else:
        t_naive = float('inf')  # mark as too slow

    res_bu, t_bu = time_function(fiboBottomUp, n)
    # For top-down, pass a new memo each time to avoid caching across calls
    res_td, t_td = time_function(fiboTopDown, n)

    print(f"{n}\t{t_naive:.6f}\t\t{t_bu:.6f}\t\t{t_td:.6f}")
