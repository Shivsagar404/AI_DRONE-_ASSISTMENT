import csv

print("=" * 50)
print("🚁 AI DRONE FAULT DIAGNOSIS ASSISTANT")
print("=" * 50)

print("\nSupported Problems:")
print("✓ Drone rotating right/left")
print("✓ GPS not locking")
print("✓ High vibration")
print("✓ Motor overheating")
print("✓ Takeoff flip")
print("✓ Battery problems")

print("\nExample Inputs:")
print("- My drone rotates right after takeoff")
print("- GPS is not locking")
print("- Motor is getting hot")
print("- Drone has high vibration")

problem = input("\nDescribe Drone Problem: ").lower()

# Keyword Detection
if "rotate" in problem or "yaw" in problem:
    keyword = "yaw"

elif "gps" in problem or "hdop" in problem:
    keyword = "gps"

elif "vibration" in problem:
    keyword = "vibration"

elif "motor" in problem or "hot" in problem:
    keyword = "motor"

elif "flip" in problem:
    keyword = "takeoff"

elif "battery" in problem:
    keyword = "battery"

else:
    keyword = problem

# Search Fault Database
with open("fault.csv", "r") as file:

    reader = csv.DictReader(file)

    found = False

    print("\n" + "=" * 50)
    print("🔍 DIAGNOSIS RESULT")
    print("=" * 50)

    for row in reader:

        if keyword in row["symptom"].lower():

            print("\n⚠ Possible Fault:")
            print(row["fault"])

            print("\n✅ Solution:")
            print(row["solution"])

            print("\n" + "-" * 50)

            found = True

    if not found:
        print("\n❌ No matching fault found.")
        print("Try describing the problem differently.")