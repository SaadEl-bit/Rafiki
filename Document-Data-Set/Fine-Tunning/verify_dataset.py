import json
from pathlib import Path
from collections import Counter

lines = [json.loads(l) for l in Path("dataset.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
counts = Counter(l["_meta"]["module"] for l in lines)
subjects = Counter(l["_meta"]["subject"] for l in lines)

print(f"Total triplets : {len(lines)}")
print()
print("--- By module ---")
for k, v in sorted(counts.items()):
    print(f"  {k:10}: {v}")
print()
print("--- By exam (subject) ---")
for k, v in sorted(subjects.items(), key=lambda x: -x[1]):
    print(f"  [{v:3}]  {k}")
print()

t = lines[0]
roles = [m["role"] for m in t["messages"]]
print("--- First triplet structure ---")
print("  message roles:", roles)
print("  _meta:", t["_meta"])
print("  system (60c):", t["messages"][0]["content"][:60])
print("  user (80c):", t["messages"][1]["content"][:80])
print("  think present:", "<think>" in t["messages"][2]["content"])
