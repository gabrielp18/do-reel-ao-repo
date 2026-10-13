"""Gera o logo do repositório: o botão de play de um reel com a curva DI de verdade passando por ele.

  python assets/logo.py  ->  assets/logo.svg

A linha é a curva do projeto 01: os 19 vencimentos do DI1 de 27/08/2026 com mais de R$ 1 bi negociado,
prazo em dias úteis (calendário ANBIMA). Ela abre em 13,899 % (DI1U26), afunda até 13,635 % (DI1F27) e sobe
até 14,46 % (DI1F35). O trecho vermelho é a inversão: −26,4 bips do U26 ao F27.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from bizdays import Calendar

NAVY, PAPER, BLUE, RED = "#1B2A4A", "#F5F6FA", "#5B8DEF", "#E5484D"
AQUI = Path(__file__).parent
CSV = AQUI.parent / "semana-01" / "01-curva-invertida" / "contratos_di_futuro.csv"

cal = Calendar.load("ANBIMA")
di = pd.read_csv(CSV)
di.columns = ["codigo", "vencimento", "taxa", "variacao", "ultimo_negocio", "volume"]
di["volume"] = di["volume"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float)
di = di[di["volume"] >= 1e9].reset_index(drop=True)
venc = [cal.adjust_next(v) for v in pd.to_datetime(di["vencimento"], dayfirst=True).dt.date]
du = np.array([cal.bizdays(pd.Timestamp("2026-08-27").date(), v) for v in venc])
taxa = di["taxa"].astype(float).to_numpy()
assert len(di) == 19 and di["codigo"].iloc[4] == "DI1F27"
assert round((taxa[4] - taxa[0]) * 100, 1) == -26.4

# prazo em raiz quadrada: abre o começo da curva, onde está a inversão
s = np.sqrt(du / 252)
x = 30 + (s - s[0]) / (s[-1] - s[0]) * 196            # de 30 a 226
y = 200 - (taxa - 13.60) / (14.50 - 13.60) * 118      # 13,60 % embaixo (200), 14,50 % em cima (82)
pts = [f"{a:.1f},{b:.1f}" for a, b in zip(x, y)]
inv = " ".join(pts[:5])                                 # U26 → F27
resto = " ".join(pts[4:])
grade = "".join(f'<path d="M{k} 0V256M0 {k}H256"/>' for k in range(32, 256, 32))

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="Do Reel ao Repo">
  <defs><clipPath id="c"><rect width="256" height="256" rx="56"/></clipPath></defs>
  <rect width="256" height="256" rx="56" fill="{NAVY}"/>
  <g clip-path="url(#c)" stroke="#FFFFFF" stroke-opacity=".07" stroke-width="1.5">{grade}</g>
  <path d="M96 66 L96 190 L198 128 Z" fill="{PAPER}" stroke="{PAPER}" stroke-width="22" stroke-linejoin="round"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="{" ".join(pts)}" stroke="{NAVY}" stroke-width="18"/>
    <polyline points="{resto}" stroke="{BLUE}" stroke-width="7"/>
    <polyline points="{inv}" stroke="{RED}" stroke-width="7"/>
  </g>
  <circle cx="{x[0]:.1f}" cy="{y[0]:.1f}" r="10" fill="{RED}" stroke="{NAVY}" stroke-width="5"/>
</svg>
"""
out = AQUI / "logo.svg"
out.write_text(svg, encoding="utf-8")
print(f"{out} · {len(di)} vértices · U26 em ({x[0]:.0f}, {y[0]:.0f}), F27 em ({x[4]:.0f}, {y[4]:.0f})")
