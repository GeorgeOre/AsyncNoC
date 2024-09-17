import sys
import re

test_module = sys.argv[1]
log_fname = sys.argv[2]
vcd_fname = sys.argv[3]

# Regular expression to match the log line pattern
log_pattern = re.compile(r"\[(\s*\d+)\]\s+<[^>]+>\s+([^\s]+)\s+:=\s+([^\s]+)")

with open(log_fname, "r") as logfile:
    logs = logfile.readlines()

events = list()
var_db = dict()
initial_values = dict()

# Process each line in the log file
for line in logs:
    line = line.strip()
    if not line:
        continue

    match = log_pattern.search(line)
    if not match:
        print(f"Skipping line due to no match: {line}")
        continue

    timestamp_str, var, val = match.groups()
    try:
        timestamp = int(timestamp_str.strip())
    except ValueError:
        print(f"Skipping line due to invalid timestamp: {line}")
        continue
    
    var = var.replace("[", "_").replace("]", "_")
    
    print(f"Processed event: Time={timestamp}, Var={var}, Value={val}")

    # Set all initial values to 0
    if var not in initial_values:
        initial_values[var] = "0"

    events.append((timestamp, var, val))
    var_db[var] = "%{}".format(var.replace(".", "_"))

print(f"Initial Values: {initial_values}")
print(f"Variable Database: {var_db}")
print(f"Events: {events}")

with open(vcd_fname, "w") as vcdfile:
    vcdfile.write("$comment\n")
    vcdfile.write("Auto-generated from {}.\n".format(log_fname))
    vcdfile.write("$end\n")

    vcdfile.write("$timescale 1ps $end\n")

    vcdfile.write("$scope module _test_{} $end\n".format(test_module))
    for var, var_id in var_db.items():
        vcdfile.write("$var wire 1 {} {} $end\n".format(var_id, var))
    vcdfile.write("$upscope $end\n".format(test_module))
    vcdfile.write("$enddefinitions $end\n".format(test_module))

    vcdfile.write("$dumpvars\n".format(test_module))
    for var, val in initial_values.items():
        vcdfile.write("{}{}\n".format(val, var_db[var]))
    vcdfile.write("$end\n".format(test_module))

    last_event_time = -1
    for timestamp, var, val in events:
        if timestamp > last_event_time:
            vcdfile.write("#{}\n".format(timestamp))
            last_event_time = timestamp
        vcdfile.write("{}{}\n".format(val, var_db[var]))
