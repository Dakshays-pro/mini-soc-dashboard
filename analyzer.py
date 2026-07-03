print("Mini SOC Dashboard Started...")

# Log file ko open karke read karna
with open('sample.log', 'r') as file:
    logs = file.readlines()

print("\n--- Suspicious Activity Alert ---")

# Har line ko check karna
for line in logs:
    if "FAILED" in line:
        print("ALERT! Suspicious activity detected: " + line.strip())