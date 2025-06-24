import re
from datetime import datetime

LICENSE_PATH = "LICENSE.md"
CURRENT_YEAR = datetime.now().year

with open(LICENSE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"Copyright © (\d{4})(?:-(\d{4}))? \[TruTemplate Contributors\]\(CONTRIBUTORS\.md\)")

match = pattern.search(content)
if match:
    START_YEAR = int(match.group(1))
    year2 = match.group(2)
    if year2:
        # Already a range, update if needed
        if int(year2) != CURRENT_YEAR:
            new_line = f"Copyright © {START_YEAR}-{CURRENT_YEAR} [TruTemplate Contributors](CONTRIBUTORS.md)"
            content = pattern.sub(new_line, content)
    else:
        # Single year, update to range if needed
        if CURRENT_YEAR > START_YEAR:
            new_line = f"Copyright © {START_YEAR}-{CURRENT_YEAR} [TruTemplate Contributors](CONTRIBUTORS.md)"
            content = pattern.sub(new_line, content)

with open(LICENSE_PATH, "w", encoding="utf-8") as f:
    f.write(content)
