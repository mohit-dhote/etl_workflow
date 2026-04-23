import datetime

# Get today's date in YYYYMMDD format
date = datetime.date.today().strftime("%Y%m%d")

# Create a new problem file
filename = f"problem_{date}.py"
with open(filename, "w") as f:
    f.write(f"""# Daily Python Problem for {date}
# Problem: Write a function that reverses a string.
# Example: reverse_string("hello") -> "olleh"

def reverse_string(s):
    return s[::-1]

# Test
print(reverse_string("hello"))
""")

print(f"Created {filename}")