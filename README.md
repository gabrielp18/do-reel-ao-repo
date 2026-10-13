<!-- Semana nova: copie cada projeto para semana-NN/<nn>-<slug>/ (dados ao lado do notebook, caminhos relativos), ponha a
     capa do carrossel em assets/vitrine/ (540×675, JPG), uma linha na tabela "Os projetos", uma ficha em "As fichas", os
     quadrados do placar e os números dos selos (projetos, testes). -->

<div align="center">

<img src="assets/logo.svg" width="120" alt="Logo: o botão de play de um reel com a curva DI de 27/08/2026 passando por ele">

# Do Reel ao Repo

O código completo por trás dos reels de [@gabrielp.pires](https://instagram.com/gabrielp.pires): cada vídeo de um minuto
vira um projeto que roda, com dado público, conta aberta e nota técnica.

[![Python](https://img.shields.io/badge/Python-3.10%2B-1E56B8?logo=python&logoColor=white)](#-comece-em-30-segundos)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebooks_executados-1B2A4A?logo=jupyter&logoColor=white)](#-os-projetos)
[![Projetos](https://img.shields.io/badge/projetos-4-F2B544)](#-os-projetos)
[![Testes](https://img.shields.io/badge/testes-48-1B2A4A?logo=pytest&logoColor=white)](#projeto-04)
[![Dados](https://img.shields.io/badge/dados-p%C3%BAblicos-1E56B8)](#-de-onde-vêm-os-dados)
[![Instagram](https://img.shields.io/badge/@gabrielp.pires-Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/gabrielp.pires)
[![Site](https://img.shields.io/badge/gabrielppires.com-site-1E56B8)](https://gabrielppires.com)
[![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-55617A)](LICENSE)
![Não é recomendação](https://img.shields.io/badge/n%C3%A3o_%C3%A9-recomenda%C3%A7%C3%A3o-B42318)

</div>

---

## 🎬 Como funciona

<img src="assets/demo-reel.gif" align="right" width="230" alt="Trecho do reel da curva DI: o gráfico em cima e o código sendo digitado embaixo">

Cada reel pega **uma** pergunta que apareceu no noticiário (a curva inverteu, a eleição muda a dívida, o Tesouro IPCA+
despencou) e responde com conta. No vídeo cabe o gráfico, a equação e o código que cabe na tela.

Aqui cabe o resto: a leitura do arquivo bruto, a limpeza, as checagens que ninguém vê, os gráficos, as tabelas e a
parte mais importante de qualquer modelo, **o que ele não vê**.

Em cada pasta de projeto:

- 📓 **o notebook executado**, com as saídas na tela (dá para ler no GitHub sem rodar nada);
- 📊 **o arquivo bruto**, do jeito que sai da fonte;
- 📄 **a nota técnica ou o relatório** em PDF, com as equações numeradas.

<br clear="right">

## 📚 Os projetos

| # | Projeto | A pergunta do reel | O número que fica | Abrir |
|:-:|---|---|---|:-:|
| 01 | [**A curva inverteu**](#projeto-01) | A curva DI inverteu. Vem recessão? | começo da curva em **−26,4 bips**: o mercado precifica pouco mais de **um corte** de 25 bips até janeiro | [📓](semana-01/01-curva-invertida/curva_di_inclinacao_inversao.ipynb) [📄](semana-01/01-curva-invertida/curva_di_inclinacao_inversao_nota_tecnica.pdf) |
| 02 | [**A dívida e a urna**](#projeto-02) | Quanto a eleição muda a dívida até 2031? | a eleição explica **5%** da incerteza; os choques da economia, **89%** | [📓](semana-01/02-divida-e-eleicoes-2026/modelo_divida_eleicoes2026_v2.ipynb) [📄](semana-01/02-divida-e-eleicoes-2026/Eleicoes2026_Analise_Fiscal_Quantitativa_v2.pdf) |
| 03 | [**O susto do IPCA+ 2050**](#projeto-03) | Como o título que protege da inflação cai 12,6%? | **+76 bips** na taxa viram **−12,6%** no preço: 24 anos de prazo são alavanca | [📓](semana-01/03-ipca-2050/ipca_marcacao_a_mercado.ipynb) [📄](semana-01/03-ipca-2050/ipca_longo_duration_convexidade_nota_tecnica.pdf) |
| 04 | [**Alocação macro BR**](#projeto-04) | Uma estratégia gringa funciona aqui? | **24 fatores**, **74 hipóteses** e o CDI com score próprio, porque aqui o caixa compete | [📦](semana-01/04-alocacao-macro-br) [📓](semana-01/04-alocacao-macro-br/notebooks/pipeline_alocacao_macro.ipynb) |

<sub>📓 notebook · 📄 nota técnica ou relatório em PDF · 📦 pacote Python com testes</sub>

## 🗂️ As fichas

## ❓ Perguntas que sempre aparecem

<details>
<summary><b>Preciso saber programar?</b></summary>
<br>
Se você já mexeu numa planilha, consegue acompanhar. Cada notebook explica a conta antes do código, e o código vem em
pedaços pequenos. Comece rodando tudo, depois mude um número (o corte de liquidez, a taxa, a chance de cada cenário) e
veja o que acontece.
</details>

<details>
<summary><b>Os números do notebook batem com os do vídeo?</b></summary>
<br>
Batem. Os notebooks 01 a 03 foram rodados de novo do zero, já dentro deste repositório, e reproduziram todas as saídas.
Onde a fala do vídeo ficou para trás da conta, a <a href="#-erratas-o-vídeo-falou-a-conta-corrigiu">errata</a> diz.
</details>

<details>
<summary><b>Posso trocar a data e rodar com dados de hoje?</b></summary>
<br>
Pode, e é a melhor parte. No 01, baixe os contratos de DI do dia no site da B3, troque <code>DATA_REF</code> e os
vértices citados pelo nome (eles mudam quando um contrato vence). No 03, troque a planilha do Tesouro Transparente: o topo e
o fundo são achados sozinhos, pelo drawdown. No 02, <code>ATUALIZAR = True</code> busca a dívida inicial no Focus mais
recente.
</details>

<details>
<summary><b>Por que um projeto fala de eleição?</b></summary>
<br>
Porque a dívida pública é a variável que mais pesa nos juros longos do Brasil, e outubro de 2026 decide quem vai
administrá-la. O modelo pega o primário que cada programa declarou e pergunta o que acontece com a dívida se ele for
cumprido, e se for cumprido pela metade. A resposta mais interessante não é sobre candidato: 89% da incerteza vem da
economia.
</details>

<details>
<summary><b>Posso usar no meu trabalho, na faculdade, no TCC?</b></summary>
<br>
Pode. O código é MIT: use, mude e redistribua, mantendo o aviso de licença. Se for publicar, cite o repositório e, no
projeto 04, o artigo original da Macrosynergy.
</details>

<details>
<summary><b>Isso é recomendação de investimento?</b></summary>
<br>
Não. É educação. Nenhum notebook diz o que comprar ou em quem votar. Eles mostram como a conta funciona, inclusive quando
ela não funciona.
</details>

## 🤝 Quer ajudar?

- ⭐ **Dê uma estrela.** Não muda a curva de juros, mas muda o meu dia.
- 🐛 **Achou um número estranho?** Abra uma issue com o projeto e a célula.
- 💡 **Tem um tema que deveria virar reel?** Sugira numa issue. Se vier com um artigo para replicar no Brasil, melhor ainda.
- 📲 **Quer o vídeo antes do código?** Siga [@gabrielp.pires](https://instagram.com/gabrielp.pires).
- 📺 **Quer começar do zero mesmo?** A série diária *Finanças Quantitativas do Zero* tem repositório próprio:
  [financas-quant-do-zero](https://github.com/gabrielp18/financas-quant-do-zero).

## ⚠️ Aviso

Conteúdo educacional. Nada aqui é recomendação de investimento, oferta, análise de valor mobiliário ou recomendação de
voto. Os cenários do projeto 02 são condicionais aos programas declarados. Os dados do projeto 04 são sintéticos até você
trocá-los. Resultado passado não garante resultado futuro, e isso vale em dobro para backtest.

## 📄 Licença e créditos

O código está sob a licença [MIT](LICENSE). Os dados ao lado dos notebooks pertencem às respectivas fontes (B3, Tesouro
Nacional, Banco Central, IFI) e seguem os termos de cada uma.

---

<div align="center">

<img src="assets/logo.svg" width="44" alt="">

<sub>Feito com pandas, café e muitos dias úteis por <a href="https://gabrielppires.com">Gabriel Pires</a> ·
<a href="https://instagram.com/gabrielp.pires">@gabrielp.pires</a></sub>

</div>
