import datetime
import random
import secrets
import os

operatives = [
    "Code: TUA-H", "Code: PER-AK", "Code: TER-AWIS", "Code: KIL-AU",
    "Code: JUN-A", "Code: BAH-AMAN", "Code: JAN-GGUT"
]

timestamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
operative_id = random.choice(operatives)
branch = "red-team/log-update"
commit = "Pending"
action_summary = "Initialized Red Team engagement log"
classification = "[INFO: SYSTEM STABLE]"
signature = secrets.token_hex(4).upper()

row = f"| {timestamp} | {operative_id} | {branch} | {commit} | {action_summary} | {classification} | {signature} |"

filename = "Attendance.md"

if os.path.exists(filename):
    with open(filename, "r+") as f:
        content = f.read()
        if content and not content.endswith('\n'):
            f.write('\n')
        f.write(row + '\n')
else:
    with open(filename, "w") as f:
        f.write("--- [ RED TEAM OPERATIONAL ENGAGEMENT LOG ] ---\n")
        f.write("CONFIDENTIALITY LEVEL: INTERNAL // AUDIT ONLY\n\n")
        f.write("| Timestamp | Operative ID | Branch | Commit | Action Summary | Classification | Signature |\n")
        f.write("| --- | --- | --- | --- | --- | --- | --- |\n")
        f.write(row + '\n')

print("Successfully updated Attendance.md")
