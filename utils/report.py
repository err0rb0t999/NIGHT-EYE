import json
from pathlib import Path
from datetime import datetime

EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)


def save_json(data: dict, filename: str = "report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = EXPORT_DIR / f"{filename}_{timestamp}.json"

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return str(file)


def save_html(data: dict, filename: str = "report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = EXPORT_DIR / f"{filename}_{timestamp}.html"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TS-OSINT Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 40px;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
th, td {{
    border: 1px solid #ccc;
    padding: 8px;
}}
th {{
    background: #333;
    color: white;
}}
</style>
</head>
<body>

<h2>TS-OSINT Pro Report</h2>

<table>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
"""

    for k, v in data.items():
        html += f"<tr><td>{k}</td><td>{v}</td></tr>\n"

    html += """
</table>

</body>
</html>
"""

    with open(file, "w", encoding="utf-8") as f:
        f.write(html)

    return str(file)
