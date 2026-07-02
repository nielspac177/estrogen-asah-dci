"""One-page workflow diagram: triangulating the role of estrogen in aSAH.

Design goals: swimlanes to group each arm, right-angle merge connectors (no
diagonals), concise text properly centered in every box, restrained palette.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({"font.family": ["Avenir Next", "Arial"], "font.size": 10})

INK = "#1b2733"; MUTE = "#5b6b7a"
BLUE = "#0B6FB8"; BLUE_BG = "#EAF3FB"; BLUE_PANEL = "#F5F9FD"
GREEN = "#0E8F6E"; GREEN_BG = "#E8F6F1"; GREEN_PANEL = "#F4FBF8"
PUR = "#6D4AAF"; PUR_BG = "#F1ECFA"
AMBER = "#B9812A"; AMBER_BG = "#FBF1DC"

fig, ax = plt.subplots(figsize=(10.5, 8.2)); ax.axis("off")
ax.set_xlim(0, 100); ax.set_ylim(0, 100)


def card(x, y, w, h, lines, *, head=None, fc="white", ec=BLUE, tc=INK,
         head_c=None, fs=9.3, lh=3.3, rs=2.2, lw=1.4):
    """A rounded card with vertically-centered, optionally-headed text."""
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle=f"round,pad=0.2,rounding_size={rs}", fc=fc, ec=ec, lw=lw))
    items = ([("__head__", head)] if head else []) + [("body", ln) for ln in lines]
    total = (len(items) - 1) * lh
    top = y + total / 2
    for i, (kind, txt) in enumerate(items):
        yy = top - i * lh
        if kind == "__head__":
            ax.text(x, yy, txt, ha="center", va="center", fontsize=fs + 1.0,
                    color=head_c or ec, fontweight="bold")
        else:
            ax.text(x, yy, txt, ha="center", va="center", fontsize=fs, color=tc)


def varrow(x, y1, y2, color=MUTE, lw=1.7):
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle="-|>",
                 mutation_scale=14, color=color, lw=lw, shrinkA=0, shrinkB=0))


# title
ax.text(50, 97, "Triangulating the role of estrogen in aneurysmal subarachnoid haemorrhage",
        ha="center", fontsize=13, fontweight="bold", color=INK)

# question
card(50, 89, 92, 8, [
    "Does estrogen protect the brain's vessels — fewer aneurysm ruptures (aSAH) and less",
    "delayed cerebral ischaemia?   Protective in animal models · never tested in humans."],
    fc="#FFFBF2", ec=AMBER, fs=9.2, lh=3.1)

# swimlane panels
ax.add_patch(FancyBboxPatch((5, 27.5), 43, 52.5, boxstyle="round,pad=0.2,rounding_size=3",
             fc=BLUE_PANEL, ec=BLUE, lw=1.1, alpha=0.9))
ax.add_patch(FancyBboxPatch((52, 27.5), 43, 52.5, boxstyle="round,pad=0.2,rounding_size=3",
             fc=GREEN_PANEL, ec=GREEN, lw=1.1, alpha=0.9))

# headers
card(26.5, 75.5, 40, 6.4, [], head="ARM 1 · Observational (ICU)", fc=BLUE_BG, ec=BLUE, fs=9.4)
card(73.5, 75.5, 40, 6.4, [], head="ARM 2 · Genetic (MR)", fc=GREEN_BG, ec=GREEN, fs=9.4)

# setup
card(26.5, 64, 38, 11, [
    "MIMIC-IV + eICU", "1,771 aSAH patients", "Menopausal state → DCI / death"],
    ec=BLUE, fs=9.1, lh=3.2)
card(73.5, 64, 38, 11, [
    "Public GWAS (100,000s of people)", "Menopause / SHBG gene variants",
    "→ aneurysm GWAS (Bakker 2020)"], ec=GREEN, fs=9.1, lh=3.2)

# weakness
card(26.5, 50.5, 38, 9, ["confounded by age", "(menopause ≈ age; no hormone data)"],
     head="WEAKNESS", fc=AMBER_BG, ec=AMBER, tc="#6b4a12", fs=8.7, lh=3.0)
card(73.5, 50.5, 38, 9, ["genetic pleiotropy", "(but immune to age confounding)"],
     head="WEAKNESS", fc=AMBER_BG, ec=AMBER, tc="#6b4a12", fs=8.7, lh=3.0)

# result
card(26.5, 37.5, 38, 9, ["No protective effect", "OR 0.86 (0.58–1.28)"],
     head="RESULT", fc="white", ec=BLUE, fs=9.4, lh=3.1)
card(73.5, 37.5, 38, 9, ["No protective effect", "OR 1.03 (0.98–1.09)"],
     head="RESULT", fc="white", ec=GREEN, fs=9.4, lh=3.1)

# intra-lane arrows (between box edges)
for x, c in [(26.5, BLUE), (73.5, GREEN)]:
    varrow(x, 72.3, 69.6, color=c)   # header -> setup
    varrow(x, 58.4, 56.1, color=c)   # setup -> weakness
    varrow(x, 45.9, 42.1, color=c)   # weakness -> result

# merge connectors (right-angle)
rail = 23.5
for x, c in [(26.5, BLUE), (73.5, GREEN)]:
    ax.add_line(Line2D([x, x], [33.0, rail], color=c, lw=1.7))
ax.add_line(Line2D([26.5, 73.5], [rail, rail], color=MUTE, lw=1.7))
varrow(50, rail, 21.1, color=PUR)

# convergence
card(50, 15.5, 86, 9, [
    "Two independent methods with non-overlapping weaknesses reach the SAME answer.",
    "If age-confounding were hiding a real effect, the genetic arm (immune) would show it."],
    head="TRIANGULATION", fc=PUR_BG, ec=PUR, fs=8.9, lh=3.0)
varrow(50, 11.0, 7.6, color=PUR)

# conclusion
card(50, 4.2, 92, 5.6, [
    "Estrogen does not measurably protect against aneurysmal SAH in humans — a rigorous, honest null."],
    fc="#12303a", ec="#12303a", tc="white", fs=10, rs=1.8)

fig.savefig("/Volumes/Niels 2/MIMIC/estrogen-asah-dci/manuscript/figures/triangulation_workflow.png",
            dpi=170, bbox_inches="tight", facecolor="white")
print("saved")
