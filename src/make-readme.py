import yaml
import sys

tab = "    "

file = sys.argv[1]

with open(file, "r") as yml:
    data = yaml.safe_load(yml)

for route in data:
    for scenario in route["scenarios"]:
        headcode = scenario["headcode"]
        time = scenario["time"]
        dest = scenario["destination"]
        orig = scenario["origin"]

        name = headcode + " " + time + " " + orig + " to " + dest

        with open(headcode + ".tex", "w+") as f:
            f.write("\\documentclass{article}\n")
            f.write("\n")
            f.write("\\title{" + name + "}\n")
            f.write("\\begin{document}\n")
            f.write(tab + "\\maketitle\n")
            f.write("\\end{document}\n")
