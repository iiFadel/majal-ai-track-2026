# Majal Initiative — AI Track

Five-day AI curriculum: supervised learning → unsupervised → computer vision → NLP/LLMs → agents.

**📊 Slides:** https://<your-username>.github.io/majal-ai/

## Material

| Day | Topic | Slides | Labs |
|:---:|-------|:------:|------|
| 1 | AI Foundations & Supervised Learning | soon | `labs/day1/` |
| 2 | Unsupervised Learning | soon | `labs/day2/` |
| 3 | Computer Vision & Deep Learning | soon | `labs/day3/` |
| 4 | NLP → Transformers → LLMs | soon | `labs/day4/` |
| 5 | Agentic AI | [slides](https://<your-username>.github.io/majal-ai/slides/day5.html) | `labs/day5/` |

## Building locally

Install [Quarto](https://quarto.org/docs/get-started/), then:

```bash
python scripts/precompute_embeddings.py  # ONCE: builds the RAG widget data
quarto preview slides/day5.qmd           # live preview, auto-reloads on save
quarto render                     # build the whole site into _site/
```

## Publishing

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the site and
deploys it to GitHub Pages. One-time setup: repo **Settings → Pages → Source: GitHub Actions**.

## Structure

```
├── index.qmd              # landing page (the table above)
├── _quarto.yml            # project config
├── slides/
│   ├── day5.qmd           # Day 5 deck
│   └── custom.scss        # shared theme for all decks
└── labs/                  # Jupyter notebooks
```

> **Note:** `slides/rag_data.json` is generated but **should be committed** — the
> GitHub Pages build does not run the precompute script (it would need to download PyTorch).
