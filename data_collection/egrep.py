import sys, re

# capture regex
regex = sys.argv[1]

for line in sys.stdin:
    # if line matches regex, write out to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
