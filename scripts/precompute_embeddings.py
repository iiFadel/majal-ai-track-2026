#!/usr/bin/env python3
"""
Generates slides/rag_data.json - REAL neural embeddings for the RAG widget.

Run once:  pip install sentence-transformers
           python scripts/precompute_embeddings.py

The slides load the JSON and do cosine similarity in the browser, so students get
real semantic search (matching MEANING, not words) with no model download on their phones.
"""
import json, pathlib
from sentence_transformers import SentenceTransformer

CHUNKS = [
    "Day 1 lab: a logistic regression classified mushrooms as edible or poisonous. Recall mattered most, because a false negative means eating poison.",
    "Day 1: overfitting means memorizing the training data instead of learning. You detect it from the gap between training and test accuracy.",
    "Day 2 lab: K-Means clustered 200 mall customers by income and spending score into five segments. The elbow method chose K.",
    "Day 2: DBSCAN finds clusters of any shape and labels lonely points as noise, which makes it suit fraud detection.",
    "Day 3 lab: the from-scratch cats vs dogs CNN reached about 67% test accuracy, with a 33-point overfitting gap.",
    "Day 3 lab: with data augmentation the same CNN reached about 69% accuracy with nearly zero gap.",
    "Day 3 lab: transfer learning with a frozen ResNet18 reached roughly 95% on the same cats and dogs data.",
    "Day 3 lab: the digit recognizer showed the augmentation trap. Vertical flips made 6 and 9 collapse into each other.",
    "Day 4: attention lets the model weigh every other word. In 'the trophy did not fit in the suitcase because it was too big', attention links 'it' to 'trophy'.",
    "Day 4 lab: students called an LLM through the API and compared temperature 0 versus 1.3.",
]

# Preset questions. The FIRST one is the money demo: zero words in common with any chunk.
QUERIES = [
    "grouping shoppers by their behaviour",
    "which mistake is worse for dangerous food?",
    "what stopped the model from memorizing?",
    "how well did the borrowed network do?",
    "why did the network mix up two numbers?",
    "how do I make the model less random?",
]

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    out = {
        "chunks": CHUNKS,
        "chunk_vecs": [[round(float(x), 5) for x in v] for v in model.encode(CHUNKS)],
        "queries": QUERIES,
        "query_vecs": [[round(float(x), 5) for x in v] for v in model.encode(QUERIES)],
    }
    path = pathlib.Path(__file__).parent.parent / "assets" / "day5" / "rag_data.json"
    path.write_text(json.dumps(out))
    kb = len(json.dumps(out)) / 1024
    print(f"Wrote {path}  ({kb:.0f} KB, {len(CHUNKS)} chunks, {len(QUERIES)} queries)")

if __name__ == "__main__":
    main()
