# World News in One Image — Saturday 21 November 2026.
# Drawn from scratch with Pillow: masthead, a hero story, seven region
# sections and a two-column story grid. No copied layout code.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 28
COL_GAP = 16
CONTENT_W = W - 2 * MARGIN
COL_W = (CONTENT_W - COL_GAP) // 2

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)

F_TITLE = font("DejaVuSans-Bold.ttf", 40)
F_DATE = font("DejaVuSans-Bold.ttf", 20)
F_META = font("DejaVuSans.ttf", 13)
F_HERO_H = font("DejaVuSans-Bold.ttf", 25)
F_HERO_D = font("DejaVuSans.ttf", 14)
F_SEC = font("DejaVuSans-Bold.ttf", 12)
F_HEAD = font("DejaVuSans-Bold.ttf", 13)
F_DET = font("DejaVuSans.ttf", 11)
F_CHIP = font("DejaVuSans-Bold.ttf", 9)
F_FOOT = font("DejaVuSans.ttf", 11)

PAPER = (248, 244, 233)
INK = (27, 27, 27)
MUTED = (107, 100, 85)
NAVY = (22, 38, 63)
GOLD = (232, 184, 75)
HERO_BG = (253, 235, 200)
HERO_RED = (179, 39, 30)
LINE = (216, 208, 188)
WHITE = (255, 255, 255)

REGIONS = [
    ("NORTH AMERICA", "NA", (31, 111, 178)),
    ("SOUTH AMERICA", "SA", (46, 139, 87)),
    ("EUROPE", "EU", (106, 76, 147)),
    ("AFRICA", "AF", (201, 123, 26)),
    ("MIDDLE EAST", "ME", (179, 39, 30)),
    ("ASIA", "AS", (14, 124, 123)),
    ("OCEANIA", "OC", (217, 79, 112)),
]

# (headline, detail, source) — every story first reported on 21 Nov 2026.
# Details are kept short so headline + detail + source fit on two lines.
STORIES = {
    "NORTH AMERICA": [
        ("Wall Street tech rout deepens",
         "Nasdaq dives 5.3%; S&P 500 falls 3.7% into correction.", "BBC"),
        ("SEC probes Nvidia accounts",
         "Regulators examine accounting issues; shares fell 13.8%.", "CNBC"),
        ("US bars Chinese telecom firms",
         "FCC votes to stop China Mobile and peers getting US numbers.", "FCC"),
        ("Trump threatens AI-centre tax",
         "US firms building data centres abroad face a 'tremendous tax'.", "AP"),
        ("New York to shut Rikers by 2032",
         "Mamdani sets a date to close the island jail complex.", "BBC"),
        ("Judge blocks homeless-aid revamp",
         "Judge rejects Trump's bid to remake a $4bn aid programme.", "Reuters"),
    ],
    "SOUTH AMERICA": [
        ("Colombia stops work in protest",
         "Unions call a nationwide stoppage amid protests and chaos.", "AP"),
        ("Hegseth's surprise Caracas stop",
         "War secretary visits as the two restore military ties.", "Reuters"),
        ("Venezuela signs US military deal",
         "Caracas signs a defence deal under a year after Maduro's fall.", "AP"),
        ("Brazil post strike looms",
         "Correios unions vote a strike from 26 Nov.", "Fentect"),
        ("Tesla opens first Argentina store",
         "Tesla enters Argentina as the auto market opens up.", "Reuters"),
        ("Colombia to cull Escobar hippos",
         "Ten hippos descended from the drug lord's pets are culled.", "AP"),
    ],
    "EUROPE": [
        ("Russian missile lands in Poland",
         "A Kh-101 missile crashes in Poland; NATO scrambles jets.", "Reuters"),
        ("UK and EU strike landmark deal",
         "Farm checks go from March 2028; youth mobility for 100,000.", "GOV.UK"),
        ("Gen Z rallies sweep Europe",
         "Thousands march in 25 countries over costs and climate.", "Al Jazeera"),
        ("Denmark expels Russian diplomat",
         "Copenhagen alleges a plot to kill a Ukrainian rapper.", "Al Jazeera"),
        ("French police jailed over beating",
         "Officers sentenced for the 2020 beating of Michel Zecler.", "BBC"),
        ("Depardieu faces sex inquiry",
         "Depardieu and a French author probed over sexual claims.", "BBC"),
        ("Vatican raises Christmas tree",
         "A giant holiday tree goes up beside St Peter's Basilica.", "AP"),
    ],
    "AFRICA": [
        ("600 women killed in South Africa",
         "Nearly 600 women killed in three months, figures show.", "BBC"),
        ("ANC fights to hold big cities",
         "Ruling party battles to keep key cities after poll losses.", "BBC"),
        ("Ebola hits 100 Congo schools",
         "About 100 schools are affected by Ebola in eastern DR Congo.", "AP"),
        ("Nigeria boat capsizes, 4 dead",
         "A boat carrying mourners to a funeral kills at least four.", "Al Jazeera"),
        ("Africa gets credit rating agency",
         "A new agency aims to make sovereign ratings fairer.", "Al Jazeera"),
    ],
    "MIDDLE EAST": [
        ("Saudi intercepts Houthi missiles",
         "Riyadh says it downed three Houthi missiles.", "Saudi govt"),
        ("Houthis hit Saudi power plant",
         "Strikes on a power plant cut power in several cities.", "AP"),
        ("Saudi strikes hit four Yemen cities",
         "Raids on four Yemen cities are reported to kill 41.", "Al Jazeera"),
        ("Iran claims US drone downed",
         "IRGC says it shot down a US MQ-9 drone over Hormuz.", "Al Jazeera"),
        ("Israeli drones kill 7 in Gaza",
         "Seven killed in drone strikes in central Gaza.", "Al Jazeera"),
        ("Gaza children mark Children's Day",
         "Displaced children in Gaza mark World Children's Day.", "Al Jazeera"),
        ("Iraq retakes militia stronghold",
         "Forces seize Jurf al-Sakhar after 12 years of militia rule.", "AP"),
        ("Israel weighs strike on Iran",
         "Ex-navy chief predicts a joint strike on Iran in two weeks.", "Reuters"),
    ],
    "ASIA": [
        ("Three-way peace declaration",
         "Trump, Xi and Putin issue a joint peace declaration.", "AP"),
        ("China warns Japan over Taiwan",
         "Beijing tells Tokyo to correct its 'false statements'.", "Reuters"),
        ("Seoul tops e-gov ranking",
         "South Korea leads the UN e-government index for the first time.", "UN"),
        ("Indian jailed 19 years in US plot",
         "Man sentenced in the US over a plot to kill a Sikh separatist.", "BBC"),
        ("Malaysia U-turn on Rohingya post",
         "Malaysia posts then deletes a Rohingya resettlement plan.", "Reuters"),
        ("Dhaka blames Delhi for violence",
         "Dhaka blames India and the Awami League for the unrest.", "AP"),
        ("Pakistan minister visits India",
         "A Pakistani minister visits India for the first time since 2025.", "AP"),
        ("Anthropic shares slide on debut",
         "The first pure-AI listing falls hard in the tech sell-off.", "BBC"),
    ],
    "OCEANIA": [
        ("Pacific trio urges Russia ceasefire",
         "Australia, Canada and NZ jointly call for an end to the war.", "Canada"),
        ("Australia win rugby world cup",
         "Australia crush NZ 34–10 for a fourth straight title.", "Al Jazeera"),
        ("Xi hails Australia turnaround",
         "Xi says ties with Australia have fully turned around.", "Reuters"),
        ("Australia, China agree AI talks",
         "Canberra and Beijing agree annual talks on AI.", "ABC"),
    ],
}

HERO = ("COURT: MYANMAR COMMITTED GENOCIDE",
        "The Hague — The International Court of Justice rules 9–6 that Myanmar committed "
        "genocide against the Rohingya in 2017 and orders an investigation and compensation. — ICJ",
        "ICJ")

TOTAL = 1 + sum(len(v) for v in STORIES.values())


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def fit_one(draw, s, f, max_w, label):
    """One line only; fail loudly instead of silently cutting a source."""
    if text_w(draw, s, f) <= max_w:
        return s
    raise SystemExit(f"OVERFLOW [{label}]: {s!r} is "
                     f"{text_w(draw, s, f):.0f}px wide, max {max_w}px")


def wrap(draw, s, f, max_w, max_lines):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise SystemExit(f"OVERFLOW hero detail: {lines}")
    return lines


def globe(draw, cx, cy, r, color):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=color, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=color, width=2)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 0, 360, fill=color, width=2)


def scales(draw, x, y, s, color):
    # Simple scales of justice: post, beam, two pans.
    draw.line([x, y - s, x, y + s], fill=color, width=3)
    draw.line([x - s, y - s * 0.7, x + s, y - s * 0.7], fill=color, width=3)
    for sx in (x - s, x + s):
        draw.line([sx, y - s * 0.7, sx - s * 0.4, y], fill=color, width=2)
        draw.line([sx, y - s * 0.7, sx + s * 0.4, y], fill=color, width=2)
        draw.arc([sx - s * 0.4, y - s * 0.15, sx + s * 0.4, y + s * 0.45],
                 0, 180, fill=color, width=2)
    draw.ellipse([x - 3, y - s - 4, x + 3, y - s + 2], fill=color)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead (90px) ----
    d.rectangle([0, 0, W, 90], fill=NAVY)
    d.rectangle([0, 90, W, 94], fill=GOLD)
    globe(d, 62, 45, 26, GOLD)
    d.text((100, 10), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=WHITE)
    d.text((100, 58), "SATURDAY 21 NOVEMBER 2026", font=F_DATE, fill=GOLD)
    meta = f"{TOTAL} STORIES · 7 REGIONS"
    d.text((W - MARGIN - text_w(d, meta, F_META), 60), meta, font=F_META, fill=WHITE)

    y = 94 + 10
    # ---- hero (78px) ----
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 78], radius=8, fill=HERO_BG)
    d.rectangle([MARGIN, y, MARGIN + 6, y + 78], fill=HERO_RED)
    scales(d, MARGIN + 34, y + 39, 16, HERO_RED)
    hx = MARGIN + 64
    d.text((hx, y + 6), HERO[0], font=F_HERO_H, fill=HERO_RED)
    hero_lines = wrap(d, HERO[1], F_HERO_D, W - MARGIN - hx - 8, 2)
    for i, ln in enumerate(hero_lines):
        d.text((hx, y + 34 + i * 18), ln, font=F_HERO_D, fill=INK)

    y += 78 + 10
    # ---- region sections, two columns ----
    row_h = 26
    sec_h = 18
    for name, code, color in REGIONS:
        stories = STORIES[name]
        d.rectangle([MARGIN, y, W - MARGIN, y + sec_h], fill=color)
        d.text((MARGIN + 8, y + 3), name, font=F_SEC, fill=WHITE)
        d.text((W - MARGIN - text_w(d, f"{len(stories)} stories", F_SEC) - 8, y + 3),
               f"{len(stories)} stories", font=F_SEC, fill=WHITE)
        y += sec_h + 3
        # two-column rows
        for i in range(0, len(stories), 2):
            for j in (0, 1):
                if i + j >= len(stories):
                    break
                head, det, src = stories[i + j]
                x = MARGIN + j * (COL_W + COL_GAP)
                # region chip
                d.rounded_rectangle([x, y + 2, x + 30, y + 17], radius=3, fill=color)
                tw = text_w(d, code, F_CHIP)
                d.text((x + (30 - tw) / 2, y + 4), code, font=F_CHIP, fill=WHITE)
                tx = x + 36
                tw_max = COL_W - 36
                head = fit_one(d, head, F_HEAD, tw_max, head)
                det = fit_one(d, f"{det} — {src}", F_DET, tw_max, head)
                d.text((tx, y), head, font=F_HEAD, fill=INK)
                d.text((tx, y + 13), det, font=F_DET, fill=MUTED)
            y += row_h
            d.line([MARGIN, y - 1, W - MARGIN, y - 1], fill=LINE, width=1)
        y += 4

    # ---- footer ----
    d.line([MARGIN, H - 26, W - MARGIN, H - 26], fill=LINE, width=1)
    foot = ("Sources: ICJ · BBC · Reuters · AP · Al Jazeera · CNBC · GOV.UK · UN · FCC · ABC — "
            "every story first reported on Saturday 21 November 2026.")
    d.text((MARGIN, H - 20), foot, font=F_FOOT, fill=MUTED)

    print(f"stories: {TOTAL}, final y: {y}, canvas: {H}")
    if y > H - 30:
        raise SystemExit(f"OVERFLOW layout: final y {y} leaves no room for the footer")
    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
