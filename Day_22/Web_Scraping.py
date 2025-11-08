import requests, re
from bs4 import BeautifulSoup

def triage(url):
    print("URL:", url)
    r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=20)
    print("HTTP status:", r.status_code)
    if r.status_code != 200:
        print("Stop: non-200 response.")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    print("Title:", soup.title.get_text(strip=True) if soup.title else "N/A")

    # ---- A) STATIC TABLES QUICK TEST (without requiring pandas) ----
    has_table = bool(soup.find("table"))
    print("Has <table> tags?:", has_table)
    if has_table:
        print("=> Path A likely works (pandas.read_html).")
    else:
        print("=> No <table> tags found. Try embedded JSON (Path B).")

    # ---- B) EMBEDDED JSON HUNT ----
    scripts = soup.find_all("script")
    print("Script tags on page:", len(scripts))

    # Heuristic: find largest inline script (often contains JSON)
    inlines = [(i, len(s.get_text() or ""), s) for i, s in enumerate(scripts) if not s.get("src")]
    inlines.sort(key=lambda t: t[1], reverse=True)

    if inlines:
        i, L, s = inlines[0]
        txt = s.get_text() or ""
        markers = ["datasets", "__svelte", "__NEXT_DATA__", "__NUXT__", "INITIAL_STATE", "JSON.parse"]
        hit = any(m.lower() in txt.lower() for m in markers)
        print(f"Largest inline <script>: index={i}, length={L}, looks JSON-ish?: {hit}")
        if hit:
            print("=> Path B likely works (embedded JSON).")
            # Give a small snippet for AI help:
            snippet = txt[:1200].replace("\n"," ")  # first ~1200 chars
            print("\n--- COPY BELOW TO CHATGPT ---")
            print(f"[SCRIPT index {i} SNIPPET]\n", snippet)
            print("--- END SNIPPET ---\n")
            return

    print("=> No obvious embedded JSON. Use DevTools Network → Fetch/XHR (Path C).")
    print("Instructions: F12 → Network → click Fetch/XHR → reload → pick a JSON request → Right click → Copy as cURL → paste here.")


triage('https://archive.ics.uci.edu/datasets')

import requests, json, re
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/datasets"
headers = {"User-Agent": "Mozilla/5.0"}

def extract_balanced(text, open_ch, close_ch):
    start = text.find(open_ch)
    assert start != -1
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return text[start:i+1]
    raise ValueError("no balanced region found")

def find_datasets_in_obj(obj):
    if isinstance(obj, dict):
        if "datasets" in obj:
            return obj["datasets"]
        for v in obj.values():
            res = find_datasets_in_obj(v)
            if res is not None:
                return res
    elif isinstance(obj, list):
        for item in obj:
            res = find_datasets_in_obj(item)
            if res is not None:
                return res
    return None

r = requests.get(url, headers=headers, timeout=20)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")

target_script_text = None
for sc in soup.find_all("script"):
    txt = sc.string or sc.get_text() or ""
    if "datasets" in txt:
        target_script_text = txt
        break

assert target_script_text is not None, "Could not find an inline script containing 'datasets'."

datasets = None

# Try extracting an outer JSON object first
try:
    outer_json_text = extract_balanced(target_script_text, "{", "}")
    outer_obj = json.loads(outer_json_text)
    # try common locations for the JSON payload string
    body_candidate = outer_obj.get("body") if isinstance(outer_obj, dict) else None
    if isinstance(body_candidate, str):
        payload = json.loads(body_candidate)
        datasets = find_datasets_in_obj(payload)
    if datasets is None:
        datasets = find_datasets_in_obj(outer_obj)
except Exception:
    # fallback: try extracting the first JSON array found in the script
    try:
        arr_text = extract_balanced(target_script_text, "[", "]")
        payload = json.loads(arr_text)
        datasets = find_datasets_in_obj(payload)
    except Exception:
        pass

assert datasets is not None, "Failed to locate 'datasets' structure in the script payload."

print(f"Found {len(datasets)} datasets.")
first = datasets[0]
print(first.get("Name", "<no name>"), "-", first.get("NumInstances", "<no num>"))

# Optional: pretty-print a small selection without requiring pandas
for d in datasets[:5]:
    print(f"{d.get('Name')} | {d.get('Area')} | {d.get('Task')} | {d.get('NumInstances')}")
 
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
soup = BeautifulSoup(response.text, 'html.parser')

html = soup.prettify()



payload = {
    "html": html,
    "url": url
}
with open("bu_facts.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print("Saved bu_facts.json")





url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
soup = BeautifulSoup(response.text, 'html.parser')

html = soup.prettify()
payload = {
    "html": html,
    "url": url
}
with open("presidents_facts.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print("Saved presidents_facts.json")