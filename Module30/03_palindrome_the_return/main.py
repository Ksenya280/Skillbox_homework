from collections import Counter

if __name__ == "__main__":
    def can_be_poly(text: str) -> bool:
        return sum(v % 2 for v in Counter(text).values()) <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
