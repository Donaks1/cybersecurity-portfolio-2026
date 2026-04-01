"""Password strength checker.

Scores passwords from 0 to 100 based on length and character variety.
"""

from __future__ import annotations

import string


def check_password_strength(password: str) -> tuple[int, str]:
	"""Return a (score, label) tuple for a password.

	Scoring model:
	- Length contributes up to 40 points.
	- Character variety contributes up to 40 points.
	- Bonus points reward stronger combinations.
	- Penalties apply to very common weak patterns.
	"""
	if not password:
		return 0, "Very Weak"

	score = 0

	length = len(password)
	score += min(length * 4, 40)

	has_lower = any(ch.islower() for ch in password)
	has_upper = any(ch.isupper() for ch in password)
	has_digit = any(ch.isdigit() for ch in password)
	has_symbol = any(ch in string.punctuation for ch in password)

	if has_lower:
		score += 10
	if has_upper:
		score += 10
	if has_digit:
		score += 10
	if has_symbol:
		score += 10

	# Bonus for using multiple classes in longer passwords.
	classes_used = sum((has_lower, has_upper, has_digit, has_symbol))
	if length >= 12 and classes_used >= 3:
		score += 10

	if length >= 16 and classes_used == 4:
		score += 10

	lower_password = password.lower()
	common_bad = {
		"password",
		"123456",
		"qwerty",
		"letmein",
		"admin",
	}
	if lower_password in common_bad:
		score -= 40

	if lower_password.isalpha() or lower_password.isdigit():
		score -= 10

	# Keep final score in [0, 100].
	score = max(0, min(score, 100))

	if score < 30:
		label = "Very Weak"
	elif score < 50:
		label = "Weak"
	elif score < 70:
		label = "Moderate"
	elif score < 85:
		label = "Strong"
	else:
		label = "Very Strong"

	return score, label


def main() -> None:
	password = input("Enter a password to check: ")
	score, label = check_password_strength(password)
	print(f"Password strength score: {score}/100")
	print(f"Rating: {label}")


if __name__ == "__main__":
	main()
