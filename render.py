#!/usr/bin/env python3
"""The Meridian Gazette - one-page world news image for Thursday 19 Nov 2026.

Renders entry.png (1024x1024): masthead, red date band, a lead story with a
drawn hero panel, a dot-grid world map with numbered markers, a day-in-numbers
box, and a 39-story river in three columns. Every story was confirmed by two
independent outlets (see sources.txt).
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
MARGIN = 28
CW = W - 2 * MARGIN  # 968 content width

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

INK = (24, 24, 28)
PAPER = (250, 248, 243)
RED = (176, 30, 36)
DARKRED = (140, 22, 28)
GREY = (96, 96, 102)
RULE = (40, 40, 44)
PANEL_BG = (237, 242, 245)
NAVY = (16, 34, 54)
NAVY2 = (26, 52, 80)
CHART = (55, 214, 122)
DOT = (116, 158, 196)


def F(path, size):
    return ImageFont.truetype(path, size)


def tw(d, s, font):
    return d.textlength(s, font=font)


def wrap(d, text, font, width):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if tw(d, trial, font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- stories ---
# (headline, two-line summary) - numbers are assigned in reading order.
LEAD = (
    "Anthropic's $81.3bn IPO Is the Largest in History",
    "Priced at $83 a share - above the $70-78 guide - the 980-million-share "
    "float values Anthropic above $1.5 trillion fully diluted, debuting "
    "today on Nasdaq as ANT.",
)

COLUMNS = [
    [
        ("EUROPE", [
            ("Estonia to shut all Russian crossings",
             "Tallinn will shut every land crossing with Russia within weeks, "
             "citing border security and hybrid pressure."),
            ("Huge Prague rally defends public media",
             "Tens of thousands rallied to defend public media, accusing "
             "ministers of trying to curb its independence."),
            ("EU plans \u20ac45bn loan to fund Ukraine",
             "Brussels plans a \u20ac45 billion loan to keep Kyiv funded through "
             "2027, backed by frozen Russian assets."),
            ("EU clears trade pact with Indonesia",
             "The EU has cleared a trade pact with Indonesia that cuts "
             "tariffs on most goods and opens services markets."),
            ("Crimean Bridge hit third time in week",
             "Explosions rocked the Kerch bridge for the third time in a "
             "week; Kyiv hinted its sea drones were responsible."),
            ("UK inflation climbs to 3.6% on fuel",
             "British inflation climbed to 3.6% as fuel costs rose, "
             "complicating the Bank of England's path on rate cuts."),
            ("Ukraine drones halve Russian refining",
             "Kyiv's long-range drones have halved Russian oil refining "
             "capacity, deepening fuel shortages across Russia."),
        ]),
        ("ASIA-PACIFIC", [
            ("Trump, Xi, Putin meet at APEC Shenzhen",
             "The three leaders met at the APEC summit in Shenzhen, their "
             "first trilateral encounter in six years."),
            ("North Korea expands uranium plant: IAEA",
             "The IAEA says North Korea is expanding its uranium enrichment "
             "plant, raising fears over its weapons stockpile."),
            ("World court to rule on Rohingya case",
             "The World Court will rule on the Rohingya genocide case, a "
             "landmark test of state responsibility."),
            ("India, Japan deepen defence ties",
             "India and Japan deepened defence ties in Tokyo, agreeing joint "
             "drills and shared maritime surveillance."),
            ("Cyclone Akvan bears down on India",
             "Cyclone Akvan is bearing down on India's east coast, with "
             "landfall expected near Odisha within 36 hours."),
            ("US lines up $2bn Philippines loan",
             "Washington is lining up a $2bn military loan so Manila can "
             "modernise its coast guard and air defences."),
        ]),
    ],
    [
        ("ASIA-PACIFIC \u00b7 CONTINUED", [
            ("Philippine Airlines in $12bn Boeing deal",
             "Philippine Airlines has signed a $12 billion Boeing deal for "
             "wide-body jets to expand its long-haul network."),
            ("North Korea fires missiles after drill",
             "Pyongyang fired ballistic missiles hours after a US-South "
             "Korea drill, calling it a warning shot."),
            ("Trump wraps Asia tour, $17bn in deals",
             "Trump wrapped his Asia tour claiming $17 billion in deals, "
             "from chips to energy and defence contracts."),
        ]),
        ("MIDDLE EAST", [
            ("Israeli armour crosses Gaza Yellow Line",
             "Israeli armour pushed past Gaza's Yellow Line overnight, in "
             "the deepest incursion since the ceasefire."),
            ("Israel: two Hamas commanders killed",
             "Israel says two senior Hamas commanders were killed in strikes "
             "it calls precise; Hamas has not confirmed."),
            ("Peace board: both sides fail Gaza deal",
             "The peace board says both sides are failing the Gaza deal, "
             "citing stalled aid and repeated violations."),
            ("Saudi: danger passed after Riyadh alerts",
             "Saudi officials say the danger has passed after air-raid "
             "alerts sounded across Riyadh late on Wednesday."),
            ("Houthi drones target Saudi oil pipeline",
             "Houthi drones targeted a Saudi oil pipeline, briefly halting "
             "flows before crews restored operations."),
        ]),
        ("AFRICA", [
            ("Ethiopia, Eritrea forces mass at Badme",
             "Ethiopian and Eritrean forces are massing near Badme, reviving "
             "fears of a new border war in the Horn."),
            ("50,000 flee Moyale fighting into Kenya",
             "Some 50,000 people have fled fighting around Moyale into "
             "Kenya, overwhelming border aid posts."),
            ("Drought tightens grip on the Horn",
             "Drought is tightening its grip on the Horn of Africa, with aid "
             "agencies warning of failed rains again."),
        ]),
        ("OCEANIA", [
            ("General Pants collapses, 500 jobs at risk",
             "Retailer General Pants has collapsed, putting 500 jobs at "
             "risk weeks before the Christmas rush."),
            ("Aussie dollar sinks to 10-month low",
             "The Aussie dollar sank to a 10-month low as commodity prices "
             "slid and rate-cut bets grew."),
        ]),
    ],
    [
        ("NORTH AMERICA", [
            ("Jeffries nominated to lead the House",
             "Hakeem Jeffries has been nominated to lead the House, setting "
             "up a tight vote when Congress returns."),
            ("Outage knocks out NSA secret network",
             "A major outage knocked out the NSA's secret network for hours; "
             "officials blame a contractor software fault."),
            ("Nvidia halts H200 chip sales to China",
             "Nvidia has halted H200 chip sales to China after new export "
             "curbs, warning of a hit to quarterly revenue."),
            ("GTA VI lands after 13-year wait",
             "GTA VI finally lands after a 13-year wait, with queues outside "
             "stores and record day-one sales expected."),
            ("Dollar hovers near 19-month high",
             "The dollar hovers near a 19-month high as traders bet the Fed "
             "will hold rates steady into next year."),
            ("Van Gogh canvas sets $190.4m record",
             "A Van Gogh canvas set a $190.4 million auction record in New "
             "York, the priciest painting sold this year."),
        ]),
        ("SOUTH AMERICA", [
            ("US signs military pact with Venezuela",
             "The US has signed a military pact with Venezuela, a sharp turn "
             "after years of sanctions and standoff."),
            ("Hegseth hands Colombia a C-130",
             "Hegseth handed Colombia a C-130 Hercules transport plane, "
             "deepening US security ties in the region."),
        ]),
        ("SCIENCE & WORLD", [
            ("Voyager 1 now one light-day from Earth",
             "Voyager 1 has reached one light-day from Earth - its signals "
             "now take a full day to arrive home."),
            ("Islam to be largest faith by 2035: Pew",
             "Pew projects Islam will be the world's largest faith by 2035, "
             "overtaking Christianity on birth rates."),
            ("Cyber attacks on UK finance near record",
             "Cyber attacks on UK finance firms are near record levels, "
             "regulators warn, with ransomware leading."),
        ]),
        ("SPORT", [
            ("Sindhu storms back into world top five",
             "Sindhu stormed back into the world top five with a "
             "straight-games win at the China Masters."),
            ("Dhoni retires from IPL after 19 seasons",
             "Dhoni has retired from the IPL after 19 seasons, ending "
             "cricket's most storied T20 career."),
        ]),
    ],
]

NUMBERS = [
    ("$81.3bn", "ANTHROPIC IPO"),
    ("$83", "IPO PRICE / SHARE"),
    ("\u20ac45bn", "EU LOAN TO UKRAINE"),
    ("3.6%", "UK INFLATION"),
    ("$2bn", "US LOAN TO PHILIPPINES"),
    ("$12bn", "AIRLINE-BOEING DEAL"),
    ("$17bn", "TRUMP ASIA DEALS"),
    ("$190.4m", "VAN GOGH RECORD"),
]

# Dot-grid world map: land spans (first, last) column per row, 62 x 26 grid.
LAND = {
    0: [(6, 12), (21, 26), (45, 52), (55, 59)],
    1: [(3, 15), (20, 27), (34, 36), (41, 60)],
    2: [(2, 17), (21, 28), (33, 37), (39, 60)],
    3: [(2, 18), (27, 27), (31, 38), (40, 60)],
    4: [(3, 19), (29, 31), (32, 39), (41, 58)],
    5: [(4, 20), (29, 31), (32, 41), (42, 57)],
    6: [(5, 21), (30, 39), (41, 56)],
    7: [(5, 21), (29, 35), (37, 43), (44, 57), (58, 59)],
    8: [(5, 20), (29, 32), (34, 43), (44, 56), (57, 58)],
    9: [(6, 19), (29, 41), (43, 48), (49, 55)],
    10: [(6, 13), (29, 42), (43, 48), (49, 53)],
    11: [(8, 12), (29, 43), (44, 47), (49, 53), (54, 55)],
    12: [(13, 19), (30, 43), (44, 46), (48, 53)],
    13: [(13, 19), (31, 42), (47, 55)],
    14: [(13, 20), (31, 41), (48, 56)],
    15: [(14, 20), (32, 40), (50, 58)],
    16: [(14, 20), (32, 40), (47, 55)],
    17: [(14, 19), (32, 39), (46, 56)],
    18: [(14, 19), (33, 38), (40, 40), (46, 56)],
    19: [(14, 18), (33, 37), (47, 55)],
    20: [(14, 17), (48, 55), (58, 59)],
    21: [(14, 16), (58, 59)],
    22: [(14, 15)],
    23: [(13, 14)],
    24: [(13, 14)],
    25: [(13, 13)],
}
# (story number, grid col, grid row)
MARKERS = [
    (1, 18, 7), (2, 35, 4), (6, 36, 6), (9, 50, 11), (10, 52, 8),
    (13, 45, 11), (18, 36, 9), (22, 39, 10), (24, 37, 14), (27, 55, 20),
    (34, 19, 13), (39, 44, 12),
]

TICKER = ("RECORD $81.3BN ANTHROPIC IPO  +++  GTA VI LANDS AFTER 13 YEARS  "
          "+++  VOYAGER 1 ONE LIGHT-DAY FROM EARTH  +++  \u20ac45BN FOR UKRAINE  +++")
SOURCES_LINE = ("Every story confirmed by two independent outlets - full "
                "sourcing in sources.txt  \u00b7  Reuters  \u00b7  AP  \u00b7  BBC  \u00b7  "
                "Al Jazeera  \u00b7  AFP  \u00b7  Bloomberg  \u00b7  The Guardian  \u00b7  "
                "Nikkei Asia  \u00b7  ABC News  \u00b7  Pew Research")


# ---------------------------------------------------------------- drawing ---
def masthead(d):
    d.line([(MARGIN, 10), (W - MARGIN, 10)], fill=RULE, width=3)
    f_small = F(SANS_B, 10)
    d.text((MARGIN, 20), "GLOBAL EDITION", font=f_small, fill=GREY)
    r = "No. 324 \u00b7 EST. 2026"
    d.text((W - MARGIN - tw(d, r, f_small), 20), r, font=f_small, fill=GREY)
    f_title = F(SERIF_B, 47)
    title = "The Meridian Gazette"
    d.text(((W - tw(d, title, f_title)) / 2, 12), title, font=f_title, fill=INK)
    d.line([(MARGIN, 66), (W - MARGIN, 66)], fill=RULE, width=1)
    d.line([(MARGIN, 69), (W - MARGIN, 69)], fill=RULE, width=3)


def date_band(d):
    d.rectangle([MARGIN, 76, W - MARGIN, 104], fill=RED)
    f = F(SANS_B, 15)
    d.text((MARGIN + 12, 83), "THURSDAY 19 NOVEMBER 2026", font=f, fill=(255, 255, 255))
    r = "40 STORIES \u00b7 6 CONTINENTS"
    d.text((W - MARGIN - 12 - tw(d, r, f), 83), r, font=f, fill=(255, 255, 255))


def hero_panel(d, x, y, w, h):
    """Drawn hero art for the lead: skyline silhouette + rising chart."""
    d.rectangle([x, y, x + w, y + h], fill=NAVY)
    base = y + h
    # skyline silhouette along the bottom
    heights = [26, 40, 31, 52, 36, 62, 44, 33, 55, 29, 47, 38, 58, 30, 42, 34]
    bw = w / len(heights)
    for i, bh in enumerate(heights):
        bx = x + i * bw
        shade = NAVY2 if i % 2 else (10, 24, 40)
        d.rectangle([bx, base - bh, bx + bw - 2, base], fill=shade)
        if i % 3 == 0:  # lit window
            d.rectangle([bx + bw / 2 - 2, base - bh + 8, bx + bw / 2 + 2,
                         base - bh + 12], fill=(250, 205, 92))
    # rising chart line
    pts = []
    steps = 9
    for i in range(steps + 1):
        px = x + 18 + (w - 185) * i / steps
        py = y + h - 16 - (h - 34) * (i / steps) ** 1.35
        pts.append((px, py))
    d.line(pts, fill=CHART, width=4, joint="curve")
    for px, py in pts[::3]:
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=CHART)
    # headline figure
    f_big = F(SANS_B, 34)
    d.text((x + w - tw(d, "$81.3BN", f_big) - 16, y + 10), "$81.3BN",
           font=f_big, fill=(255, 255, 255))
    f_lab = F(SANS_B, 10)
    lab = "LARGEST IPO IN HISTORY"
    d.text((x + w - tw(d, lab, f_lab) - 16, y + 50), lab, font=f_lab,
           fill=(170, 205, 235))
    chip = "NASDAQ \u00b7 ANT"
    f_chip = F(SANS_B, 10)
    cw_ = tw(d, chip, f_chip) + 14
    d.rectangle([x + w - cw_ - 16, y + 66, x + w - 16, y + 84], fill=CHART)
    d.text((x + w - cw_ - 9, y + 70), chip, font=f_chip, fill=NAVY)


def lead_block(d):
    x, y = MARGIN, 112
    w = 540
    f_kick = F(SANS_B, 11)
    d.text((x, y), "LEAD STORY \u00b7 MARKETS \u00b7 STORY No. 1", font=f_kick, fill=RED)
    f_head = F(SERIF_B, 28)
    ly = y + 16
    for line in wrap(d, LEAD[0], f_head, w):
        d.text((x, ly), line, font=f_head, fill=INK)
        ly += 33
    hero_panel(d, x, 198, w, 92)
    f_body = F(SANS, 12)
    by = 298
    for line in wrap(d, LEAD[1], f_body, w):
        d.text((x, by), line, font=f_body, fill=INK)
        by += 15


def map_panel(d, x, y, w):
    d.rectangle([x, y, x + w, y + 148], fill=PANEL_BG, outline=RULE, width=1)
    f_t = F(SANS_B, 11)
    d.text((x + 10, y + 7), "THE WORLD TODAY \u2014 WHERE IT HAPPENED",
           font=f_t, fill=INK)
    gx, gy = x + 6, y + 27
    cell_w, cell_h = (w - 12) / 62, 4.6
    for row, spans in LAND.items():
        for c0, c1 in spans:
            for c in range(c0, c1 + 1):
                cx = gx + c * cell_w + cell_w / 2
                cy = gy + row * cell_h + cell_h / 2
                d.ellipse([cx - 1.7, cy - 1.7, cx + 1.7, cy + 1.7], fill=DOT)
    f_num = F(SANS_B, 8)
    for num, c, r in MARKERS:
        cx = gx + c * cell_w + cell_w / 2
        cy = gy + r * cell_h + cell_h / 2
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED, outline=(255, 255, 255), width=1)
        s = str(num)
        d.text((cx - tw(d, s, f_num) / 2, cy - 5), s, font=f_num, fill=(255, 255, 255))


def numbers_box(d, x, y, w):
    d.rectangle([x, y, x + w, y + 66], fill=(255, 255, 255), outline=RULE, width=1)
    d.rectangle([x, y, x + w, y + 15], fill=INK)
    f_h = F(SANS_B, 9)
    d.text((x + 8, y + 3), "THE DAY IN NUMBERS", font=f_h, fill=(255, 255, 255))
    f_fig = F(SANS_B, 13)
    f_lab = F(SANS, 7)
    colw = w / 4
    for i, (fig, lab) in enumerate(NUMBERS):
        cx = x + (i % 4) * colw + colw / 2
        cy = y + 18 + (i // 4) * 22
        d.text((cx - tw(d, fig, f_fig) / 2, cy), fig, font=f_fig, fill=DARKRED)
        d.text((cx - tw(d, lab, f_lab) / 2, cy + 13), lab, font=f_lab, fill=GREY)


def river(d):
    top = 336
    col_w = 310
    xs = [MARGIN, MARGIN + col_w + 19, MARGIN + 2 * (col_w + 19)]
    f_head = F(SERIF_B, 14)
    f_body = F(SANS, 11)
    f_sec = F(SANS_B, 11)
    f_chip = F(SANS_B, 9)
    num = 1  # lead story is No. 1
    problems = []
    for ci, sections in enumerate(COLUMNS):
        x = xs[ci]
        y = top
        if ci > 0:
            d.line([(x - 10, top), (x - 10, 972)], fill=(205, 200, 190), width=1)
        for label, stories in sections:
            d.rectangle([x, y, x + col_w, y + 15], fill=RED)
            d.text((x + 6, y + 2), label, font=f_sec, fill=(255, 255, 255))
            y += 17
            for head, body in stories:
                num += 1
                if tw(d, head, f_head) > col_w - 20:
                    problems.append(("headline", num, head))
                d.rectangle([x, y + 1, x + 14, y + 15], fill=RED)
                s = str(num)
                d.text((x + 7 - tw(d, s, f_chip) / 2, y + 3), s, font=f_chip,
                       fill=(255, 255, 255))
                d.text((x + 19, y), head, font=f_head, fill=INK)
                lines = wrap(d, body, f_body, col_w)
                if len(lines) > 2:
                    problems.append(("body", num, body))
                by = y + 16
                for line in lines[:2]:
                    d.text((x, by), line, font=f_body, fill=(52, 52, 58))
                    by += 12
                y += 43
        if y > 976:
            problems.append(("column overflow", ci, y))
    return problems


def footer(d):
    f_src = F(SANS, 9)
    d.text(((W - tw(d, SOURCES_LINE, f_src)) / 2, 981), SOURCES_LINE,
           font=f_src, fill=GREY)
    d.rectangle([MARGIN, 994, W - MARGIN, 1020], fill=INK)
    f_t = F(SANS_B, 11)
    d.text(((W - tw(d, TICKER, f_t)) / 2, 1001), TICKER, font=f_t,
           fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    date_band(d)
    lead_block(d)
    map_panel(d, 588, 112, 408)
    numbers_box(d, 588, 266, 408)
    problems = river(d)
    footer(d)
    img.save(OUT, optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")
    for p in problems:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
