<div align="center">

<img src="../../assets/icones/02-divida-e-eleicoes-2026.svg" width="96" alt="Ícone: a dívida bruta até 2031 em três cenários, com a faixa da mistura eleitoral em 2031">

# A eleição explica só 5% do futuro da dívida

**Projeto 02 · Semana 1 · [Do Reel ao Repo](../../README.md)**

*Rodei 20 mil trajetórias da dívida brasileira até 2031. O que mais pesa não está na urna.*

![Comenta DÍVIDA](https://img.shields.io/badge/comenta-D%C3%8DVIDA-E5484D)
![Dados](https://img.shields.io/badge/dados-BCB_%C2%B7_Focus_%C2%B7_IFI-1E56B8)
![Monte Carlo](https://img.shields.io/badge/Monte_Carlo-20.000_trajet%C3%B3rias-1B2A4A)
![Relatório](https://img.shields.io/badge/relat%C3%B3rio-22_p%C3%A1ginas-F2B544)
![Revisão](https://img.shields.io/badge/revis%C3%A3o-26%2F09%2F2026-55617A)
[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabrielp18/do-reel-ao-repo/blob/main/semana-01/02-divida-e-eleicoes-2026/modelo_divida_eleicoes2026_v2.ipynb)

[Em 20 segundos](#-em-20-segundos) · [Rode](#-rode) · [Os cenários](#-os-cenários) · [A conta](#-a-conta) · [O notebook](#-o-notebook-seção-por-seção) · [Caça ao número](#-caça-ao-número) · [Errata](#-errata) · [Limitações](#-o-que-este-modelo-não-vê)

</div>

---

> [!IMPORTANT]
> São cenários **condicionais**: o que acontece com a dívida *se* a trajetória de primário atribuída a cada candidatura
> for executada, inteira ou em parte. Não é previsão, nem pesquisa eleitoral, nem recomendação de voto ou de investimento.

## ⚡ Em 20 segundos

- Quem ganhar em outubro herda uma dívida bruta de **82,5% do PIB** (jul/26) e um primário negativo.
- Para a dívida parar de subir, o primário precisa cobrir a distância entre juro real e crescimento: com $r = 5{,}2\%$ e
  $g = 1{,}5\%$, **3,1% do PIB**. Nenhum dos cenários chega lá.
- Com o plano executado por inteiro e sem choques, a dívida vai a **94,8%** em 2031 no cenário A e a **87,9%** no B1:
  **6,9 pontos** de distância, e **81%** dela é o próprio primário.
- Com a execução sorteada e os choques calibrados nos erros do Focus, em 20 mil trajetórias e eleição meio a meio, a
  mediana vai a **94,5%**, com **74%** de chance de passar de 90%.
- Separando a variância: **89%** da incerteza vem dos choques da economia, **6%** da execução e **5%** da eleição.

## 🏃 Rode

```bash
pip install numpy pandas matplotlib requests jupyterlab
jupyter lab modelo_divida_eleicoes2026_v2.ipynb
```

O notebook não lê arquivo nenhum: os dados de partida estão na seção 1 e a calibração dos choques, na seção 12. Por isso
ele também abre direto no [Colab](https://colab.research.google.com/github/gabrielp18/do-reel-ao-repo/blob/main/semana-01/02-divida-e-eleicoes-2026/modelo_divida_eleicoes2026_v2.ipynb).
As sementes são fixas: rodou de novo, deu o mesmo número.

## 📊 Os cenários

O primário planejado de cada cenário, como o notebook define na seção 1 (em % do PIB):

| Cenário | Como o notebook descreve | Primário em 2031 | Execução sorteada |
|---|---|:-:|:-:|
| **A** | Continuidade (Lula): arcabouço vigente e despesas contratadas, em nível, como as metas | 0,75 | Beta(7; 3), média 0,70 |
| **B1** | Ajuste integral (Flávio): de 0,9 a 2,0 pontos sobre P0, segundo reportagem sobre a equipe (não consta do programa oficial) | 1,98 | Beta(5,5; 4,5), média 0,55 |
| **C** | Ajuste declarado (Renan Santos): de 0,8 a 1,8 ponto sobre P0 | 1,78 | Beta(4; 6), média 0,40 |
| **P0** | Referência sem nova política: o primário esperado pelo Focus | −0,02 | — |

Quer testar outra tradução de um programa? Mude `CENARIOS[...]["pb"]`, `AJ_B1` ou `AJ_C` e reexecute a partir da
seção 5. Quer outra chance para cada lado? Mude `pesos = {"A": 0.5, "B1": 0.5}` na seção 9.

## 🧮 A conta

A dívida de hoje é a de ontem corrigida pelo juro real, diluída pelo crescimento, menos o primário. Igualando $d_t$ a
$d_{t-1}$, sai o primário que a estabiliza:

$$
d_t = d_{t-1}\,\frac{1+r_t}{1+g_t} - pb_t
\qquad\Rightarrow\qquad
pb^* = d\,\frac{r-g}{1+g}
$$

Com $d = 85\%$, cada ponto a mais de juro real pede 0,84 ponto a mais de primário, e cada ponto a mais de crescimento
alivia 0,87.

Em volta disso, um modelo anual em blocos (prêmio de risco, câmbio, PIB, IPCA, Selic e custo da dívida), com o primário
efetivo igual ao de referência mais a fração $u$ do plano que de fato sai do papel:

$$
pb^{pol} = pb^0 + u\,(pb^{plano} - pb^0), \qquad u \sim \text{Beta}(a, b)
$$

E a pergunta do título, pela lei da variância total: quanto da incerteza sobre a dívida de 2031 vem de cada fonte.

$$
\text{Var}(d_{2031}) = \underbrace{\text{Var}\big(\mathbb{E}[d \mid \text{eleição}]\big)}_{\text{eleição}} + \underbrace{\mathbb{E}\big[\text{Var}(d \mid \text{eleição})\big]}_{\text{execução} \,+\, \text{macro}}
$$

## 📖 O notebook, seção por seção

| § | O que acontece | O que sai |
|:-:|---|---|
| 1 | Dados de partida, cenários e parâmetros | a dívida de 82,5% em jul/26 e de 83,4% esperada para dez/26 (Focus) |
| 2 | *(opcional)* Atualização pelo SGS e pelo Focus | com `ATUALIZAR = True`, a dívida inicial vem do Focus mais recente |
| 3 | Aritmética da dívida | o primário estabilizador de **3,10%** e as sensibilidades |
| 4 | O modelo semiestrutural anual | a função `simular`, bloco a bloco |
| 5 | Cenários determinísticos e validação contra o Focus | A **94,8**, B1 **87,9**, C 89,3 e P0 98,9 em 2031; P0 erra o Focus em no máximo 0,79 ponto |
| 6 | De onde vem a diferença A − B1 (Shapley) | 6,85 pontos: **81%** primário, 23% prêmio, −3% crescimento |
| 7 | Monte Carlo com os mesmos choques nos três cenários | leques e probabilidades por cenário e regime de execução |
| 8 | A diferença entre A e B1 sob incerteza | mediana de 3,3 pontos com execução sorteada; ponto de empate em $u_{B1} = 0{,}26$ |
| 9 | Mistura eleitoral e decomposição da variância | mediana **94,5%**, P(> 90%) = **74%**, e 89% / 6% / 5% |
| 10 | Sensibilidade e custos que os programas não quantificam | quanto cada parâmetro mexe na diferença A − B1 |
| 11 | O que um pregão implica | a reação do dólar a uma pesquisa, comparada com o que o modelo explica |
| 12 | Calibração dos choques com os erros do Focus | σ de 2,15 no PIB, 1,94 no juro e 1,15 no primário (2003–2025, sem 2020–21) |

## 🔎 Caça ao número

| No reel | Valor | Onde sai |
|---|---|---|
| a dívida de hoje | 82,5% do PIB (jul/26) | § 1, baseline (SGS 13762) |
| o primário que estabiliza | **3,1% do PIB** | § 3 |
| 2031 no A e no B1, plano inteiro | **94,8%** e **87,9%** | § 5 |
| a distância entre os dois | **6,9 pontos** (6,85) | § 5 e § 6 |
| quanto dela é o primário | **81%** | § 6 |
| a mediana da mistura 50/50 | **94,5%** | § 9 |
| chance de passar de 90% | **74%** | § 9 |
| macro, execução, eleição | **89%**, **6%**, **5%** (σ total de 7,4 pontos) | § 9 |

## 🩹 Errata

A fala do reel foi gravada com a versão anterior do modelo. Os gráficos do vídeo, o relatório e este notebook já trazem a
revisão de 26/09.

| A fala disse | A revisão diz |
|---|---|
| 94,9% e 88,9% em 2031 | **94,8%** e **87,9%** |
| "seis pontos" | **6,9 pontos** |
| mediana de 95,4% | **94,5%** |
| 91% de chance de passar de 90% | **74%** |
| cerca de um décimo para eleição e para execução | **5%** e **6%** |

O que mudou de uma versão para a outra (ponto de partida, choques, repasse cambial, juros nominais e o Monte Carlo com
números aleatórios comuns) está na tabela do topo do notebook.

## 📦 Arquivos

| Arquivo | O que é |
|---|---|
| [`modelo_divida_eleicoes2026_v2.ipynb`](modelo_divida_eleicoes2026_v2.ipynb) | o modelo, executado, com a lista do que mudou na revisão |
| [`Eleicoes2026_Analise_Fiscal_Quantitativa_v2.pdf`](Eleicoes2026_Analise_Fiscal_Quantitativa_v2.pdf) | o relatório, 22 páginas, com o sumário executivo e os gráficos |
| [`apresentacao_eleicoes2026_v2.html`](apresentacao_eleicoes2026_v2.html) | a apresentação: baixe e abra no navegador (precisa de internet para as fontes e os gráficos) |

## 🙈 O que este modelo não vê

- **É anual e calibrado,** não estimado de ponta a ponta.
- **Sem a composição da dívida por indexador:** prefixado, Selic, IPCA e câmbio entram juntos num custo médio.
- **O Congresso entra só pela fração $u$.** Aprovação, desidratação e calendário viram um número entre 0 e 1.
- **O choque de primário inclui desvio de política,** que em B1 e C se soma ao risco de execução.
- **O que os programas não quantificam** (cortes de tributos prometidos, gasto novo não previsto) fica fora da conta
  principal e aparece só na seção 10.

---

<div align="center">

<sub>Conteúdo educacional · cenários condicionais · não é previsão nem recomendação de voto ou de investimento · dados: BCB (Estatísticas Fiscais, SGS, Focus), IFI e os programas</sub>

[⬅️ Projeto 01: a curva inverteu](../01-curva-invertida/README.md) · [Voltar ao repositório](../../README.md) · [Projeto 03: o susto do IPCA+ ➡️](../03-ipca-2050/README.md)

</div>
