import sys
print("Arguments:", sys.argv)
data = sys.stdin.read()
print("Standard input:", data)
print("Standard output", file=sys.stdout)
print("Error output", file=sys.stderr)
