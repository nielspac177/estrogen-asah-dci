"""One-page workflow diagram: triangulating the role of estrogen in aSAH."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BLUE="#0072B2"; ORANGE="#E69F00"; GREEN="#009E73"; RED="#D55E00"; GREY="#666"; LIGHT="#EAF2F8"; LIGHTG="#E7F5EF"
plt.rcParams.update({"font.size":9.5,"font.family":"DejaVu Sans"})
fig,ax=plt.subplots(figsize=(9.5,7.2)); ax.axis("off"); ax.set_xlim(0,100); ax.set_ylim(0,100)

def box(x,y,w,h,text,fc=LIGHT,ec=BLUE,bold=False,fs=9.5,tc="#111"):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.6,rounding_size=2",
                fc=fc,ec=ec,lw=1.6))
    ax.text(x,y,text,ha="center",va="center",fontsize=fs,color=tc,
            fontweight="bold" if bold else "normal",wrap=True)

def arrow(x1,y1,x2,y2,color=GREY,style="-|>",lw=1.8,ls="-"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=16,
                color=color,lw=lw,linestyle=ls,shrinkA=2,shrinkB=2))

# Title
ax.text(50,97,"Triangulating the role of estrogen in aneurysmal subarachnoid haemorrhage",
        ha="center",fontsize=12.5,fontweight="bold")

# The question
box(50,88,86,9,"THE QUESTION\nDoes estrogen protect the brain's vessels — fewer aneurysm ruptures (aSAH)\nand less delayed cerebral ischaemia (DCI)?  Animal models say yes; untested in humans.",
    fc="#FFF7E6",ec=ORANGE,bold=False,fs=9.5)

# Arm headers
box(26,76,40,7,"ARM 1 — Observational (ICU data)",fc=LIGHT,ec=BLUE,bold=True)
box(74,76,40,7,"ARM 2 — Genetic (Mendelian randomization)",fc=LIGHTG,ec=GREEN,bold=True)
arrow(38,84,30,79.5); arrow(62,84,70,79.5)

# Arm 1 chain
box(26,66,42,8,"MIMIC-IV + eICU  ·  n = 1,771 aSAH patients\nExposure: menopausal state (age <51 vs ≥51)\nOutcome: DCI / vasospasm, in-hospital death",fc=LIGHT,ec=BLUE,fs=8.6)
box(26,54.5,42,7.5,"Bias / weakness\nMenopause = age here → CONFOUNDED by age;\nno biological menopause data (1/354)",fc="#FDECEA",ec=RED,fs=8.4,tc="#7a2012")
box(26,43,42,7.5,"RESULT\nNo protective effect\nadj. OR 0.86 (0.58–1.28); 41/72 specs opposite",fc="#EEF6FF",ec=BLUE,bold=True,fs=8.8)
arrow(26,62,26,58.3); arrow(26,50.8,26,46.8)

# Arm 2 chain
box(74,66,42,8,"Public GWAS  ·  hundreds of thousands of people\nExposure: genes for age at menopause / SHBG\nOutcome: aneurysm GWAS (Bakker 2020)",fc=LIGHTG,ec=GREEN,fs=8.6)
box(74,54.5,42,7.5,"Bias / weakness\nGenes fixed at conception → NO age confounding;\nassumes genes act only via estrogen (pleiotropy check)",fc="#FDECEA",ec=RED,fs=8.4,tc="#7a2012")
box(74,43,42,7.5,"RESULT\nNo protective effect\nIVW OR 1.03 (0.98–1.09); median 1.09 (1.00–1.19)",fc="#EEFBF5",ec=GREEN,bold=True,fs=8.8)
arrow(74,62,74,58.3); arrow(74,50.8,74,46.8)

# Converge
arrow(26,39.2,44,30.5,color=BLUE); arrow(74,39.2,56,30.5,color=GREEN)
box(50,26,66,9,"TRIANGULATION\nTwo designs with DIFFERENT, non-overlapping weaknesses give the SAME answer.\nIf age-confounding were hiding a real effect, the genetic arm (immune to it) would reveal it — it did not.",
    fc="#F3EEFB",ec="#7B4FBE",bold=False,fs=9)
arrow(50,21.5,50,16.5,color="#7B4FBE",lw=2.2)

# Conclusion
box(50,11,94,8.5,"CONCLUSION\nThe animal-model 'estrogen protects' hypothesis is NOT supported in humans for aSAH.\nA rigorous, honest null triangulated across two independent methods.",
    fc="#111",ec="#111",bold=True,fs=9.2,tc="white")

fig.savefig("/Volumes/Niels 2/MIMIC/estrogen-asah-dci/manuscript/figures/triangulation_workflow.png",
            dpi=150,bbox_inches="tight")
print("saved triangulation_workflow.png")
