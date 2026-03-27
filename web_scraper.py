import pandas as pd
import time
from serpapi import GoogleSearch

API_KEY = "de287b8640a70a364ad9083e636f72825ea44b668ebaa44447429fe456749dd6"


# ---------- Search Function ----------
def search_person(name):
    params = {
        "engine": "google",
        "q": f'{name} linkedin profile job',
        "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        snippets = []
        titles = []

        for r in results.get("organic_results", []):
            if "snippet" in r:
                snippets.append(r["snippet"])
            if "title" in r:
                titles.append(r["title"])

        return " | ".join(titles), " ".join(snippets)

    except Exception as e:
        print(f"Error searching {name}: {e}")
        return "", ""


# ---------- Simple Domain Classifier ----------
DOMAIN_KEYWORDS = {
    "Data": ["data", "analytics", "machine learning", "ai", "bigquery"],
    "Software": ["software", "developer", "engineer", "backend", "frontend"],
    "Finance": ["bank", "finance", "trading", "risk", "investment"],
    "Healthcare": ["medical", "hospital", "pharma", "clinical"],
    "Education": ["professor", "teacher", "school", "university"],
    "Cloud": ["cloud", "aws", "gcp", "azure"],
}


def classify_domain(text):
    text = text.lower()

    for domain, words in DOMAIN_KEYWORDS.items():
        if any(w in text for w in words):
            return domain

    return "Unknown"


# ---------- Main Pipeline ----------
df = pd.read_csv("alumni.csv")

titles_list = []
snippets_list = []
domains = []

for name in df["name"]:
    print("Searching:", name)

    titles, snippets = search_person(name)

    titles_list.append(titles)
    snippets_list.append(snippets)
    domains.append(classify_domain(titles + " " + snippets))

    time.sleep(1)  # rate limit safety


# ---------- Add Results ----------
df["search_titles"] = titles_list
df["search_snippets"] = snippets_list
df["predicted_domain"] = domains


# ---------- Write Output CSV ----------
df.to_csv("alumni_enriched.csv", index=False)

print("✅ Output written to alumni_enriched_1.csv")
