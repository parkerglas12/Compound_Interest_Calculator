import matplotlib.pyplot as plt
import seaborn as sns

def calculate_intervals(p: float, r: float, n: float, t: int) -> list[float]:
    intervals: list[float] = []
    for i in range(1, t + 1):
        a: float = p * ((1 + (r / n)) ** (n * i))
        intervals.append(a)
    return intervals

def print_intervals(intervals: list[float]) -> None:
    for i, value in enumerate(intervals, start = 1):
        print(f"After year {i}, your investment or loan is worth ${value:.2f}")

def display_intervals(intervals: list[float]) -> None:
    x_values = range(1, len(intervals) + 1)
    y_values = [round(value, 2) for value in intervals]
    sns.set()
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o")
    plt.xticks(x_values)
    plt.xlabel("Year", fontsize=14, weight="bold", labelpad=15)
    plt.ylabel("Total Amount ($)",  fontsize=14, weight="bold", labelpad=15)
    plt.title("Chart of Compound Interest",  fontsize=14, weight="bold")
    plt.tight_layout(pad=2)
    plt.show()

def get_user_inputs() -> tuple[float, float, int, int]:
    while True:
        try:
            p: float = float(input("What is the initial amount of money you are investing or borrowing: "))     
            r: float = float(input("What is the annual interest rate? (e.g., enter 5 for 5%): ")) / 100
            n: int = int(input("How often is the interest compounded per year: "))
            t: int = int(input("Enter the duration of the investment or loan in years: "))
            if p <= 0 or r <= 0 or n <= 0 or t <= 0:
                raise ValueError("Please enter a positive value for all inputs.")
            elif t > 50:
                raise ValueError("Please enter a time frame between 1 and 50 years.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return p, r, n, t

def main() -> None:
    p,r, n, t = get_user_inputs()
    intervals: list[float] = calculate_intervals(p, r, n, t)
    print_intervals(intervals)
    display_intervals(intervals)

if __name__ == "__main__":
    main()