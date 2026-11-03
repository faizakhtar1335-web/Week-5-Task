"""
Week 5: Comparative review of simplified coding methodologies.

Run:
    python coding_methodology_review.py

Creates:
    methodology_scores.csv
    methodology_comparison_chart.png

The 1–5 values are an illustrative evaluation rubric from the accompanying
report, not experimental measurements or universal rankings.
"""
import csv
import matplotlib.pyplot as plt

CRITERIA = [
    "Clarity",
    "Accessibility",
    "Fast start",
    "Transfer to real code",
    "Debugging insight",
]

SCORES = {
    "Block-based (Scratch)": [5, 5, 5, 3, 3],
    "Guided text-based (Python)": [3, 3, 3, 5, 4],
}

def write_scores_csv(filename="methodology_scores.csv"):
    """Write each approach and its criterion scores to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Approach", *CRITERIA])
        for approach, scores in SCORES.items():
            writer.writerow([approach, *scores])

def print_comparison():
    """Display a readable score summary in the terminal."""
    print("\\nComparative Coding Methodology Review")
    print("-" * 43)
    print(f"{'Criterion':<25}{'Scratch':>9}{'Python':>9}")
    for index, criterion in enumerate(CRITERIA):
        print(
            f"{criterion:<25}"
            f"{SCORES['Block-based (Scratch)'][index]:>9}"
            f"{SCORES['Guided text-based (Python)'][index]:>9}"
        )
    print("\\nScale: 1 = relatively low, 5 = relatively high.")
    print("Scores are qualitative rubric judgements, not measured results.")

def create_chart(filename="methodology_comparison_chart.png"):
    """Create a grouped bar chart comparing the two approaches."""
    positions = list(range(len(CRITERIA)))
    width = 0.36

    plt.figure(figsize=(9, 4.8))
    plt.bar(
        [position - width / 2 for position in positions],
        SCORES["Block-based (Scratch)"],
        width=width,
        label="Block-based (Scratch)",
    )
    plt.bar(
        [position + width / 2 for position in positions],
        SCORES["Guided text-based (Python)"],
        width=width,
        label="Guided text-based (Python)",
    )
    plt.xticks(positions, CRITERIA, rotation=12, ha="right")
    plt.yticks(range(1, 6))
    plt.ylim(0, 5.6)
    plt.ylabel("Rubric score (1 = low, 5 = high)")
    plt.title("Indicative comparison of beginner teaching approaches")
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=180)
    print(f"Chart saved to: {filename}")

def main():
    write_scores_csv()
    print_comparison()
    create_chart()
    print("CSV saved to: methodology_scores.csv")

if __name__ == "__main__":
    main()
