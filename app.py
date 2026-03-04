import os
import math
import io
from flask import Flask, request, send_file

app = Flask(name)

def digit_sum(n):
return sum(int(d) for d in str(n) if d.isdigit())

def extract_structure(date):
year, month, day = date.split("-")
total = digit_sum(date.replace("-", ""))
cycle = total % 12 + 1
day_val = digit_sum(day)
month_val = digit_sum(month)
return total, cycle, day_val, month_val

def generate_svg(date1, date2):
total1, cycle1, day1, month1 = extract_structure(date1)
total2, cycle2, day2, month2 = extract_structure(date2)

cx, cy = 200, 200
radius = 150
elements = []

elements.append(
    f'<circle cx="{cx}" cy="{cy}" r="{radius}" stroke="black" fill="none"/>'
)

for i in range(cycle1):
    angle = (2 * math.pi / cycle1) * i
    length = 60 + day1 * 2
    x2 = cx + length * math.cos(angle)
    y2 = cy + length * math.sin(angle)
    elements.append(
        f'<line x1="{cx}" y1="{cy}" x2="{x2}" y2="{y2}" stroke="blue"/>'
    )

offset = (month2 / 12) * 2 * math.pi
for i in range(cycle2):
    angle = (2 * math.pi / cycle2) * i + offset
    length = 60 + day2 * 2
    x2 = cx + length * math.cos(angle)
    y2 = cy + length * math.sin(angle)
    elements.append(
        f'<line x1="{cx}" y1="{cy}" x2="{x2}" y2="{y2}" stroke="red"/>'
    )

svg = f"""<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">

{''.join(elements)}
</svg>"""

return svg

@app.route("/")
def home():
return """
<h2>Valentine Harmony Glyph</h2>
<form action="/download">
<input name="date1" placeholder="YYYY-MM-DD" required>
<input name="date2" placeholder="YYYY-MM-DD" required>
<button type="submit">Download SVG</button>
</form>
"""

@app.route("/download")
def download():
date1 = request.args.get("date1")
date2 = request.args.get("date2")

if not date1 or not date2:
    return "Both dates required"

svg = generate_svg(date1, date2)

return send_file(
    io.BytesIO(svg.encode("utf-8")),
    mimetype="image/svg+xml",
    as_attachment=True,
    download_name=f"valentine_{date1}_{date2}.svg"
)

if name == "main":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
