import json
import pandas as pd
from tqdm import tqdm

input_file = "data/arxiv-metadata-oai-snapshot.json"
output_file = "data/cs_papers.csv"

papers = []

print("Reading dataset...")

with open(input_file, "r", encoding="utf-8") as file:

    for i, line in enumerate(tqdm(file)):

        paper = json.loads(line)

        if i < 5:
            print("Categories:", paper.get("categories"))

        categories = paper.get("categories", "")

        # Keep any paper whose categories contain "cs."
        if "cs." in categories:

            papers.append({
                "id": paper.get("id"),
                "title": paper.get("title"),
                "abstract": paper.get("abstract"),
                "categories": categories
            })

print("Total CS papers found:", len(papers))

df = pd.DataFrame(papers)
df.to_csv(output_file, index=False)

print("CSV saved successfully!")