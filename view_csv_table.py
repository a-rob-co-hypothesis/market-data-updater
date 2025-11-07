import pandas as pd
import os
import argparse
import webbrowser
import platform
import subprocess

# --- Argument parser ---
parser = argparse.ArgumentParser(description="Visualize prices CSV")
parser.add_argument(
    "--mode",
    choices=["md", "html", "console"],
    nargs="*",
    help="Choose which outputs to open/view: md, html, console"
)
args = parser.parse_args()

# --- Lire le CSV ---
csv_path = "data/prices.csv"
df = pd.read_csv(csv_path)

# --- Nettoyer colonnes si nécessaire ---
if any(isinstance(c, tuple) for c in df.columns):
    tickers = ["AAPL", "TSLA", "NVDA"]  # mettre tous tes tickers ici
    dfs = []
    for ticker in tickers:
        cols = [c for c in df.columns if ticker in str(c)]
        if not cols:
            continue
        tmp = df[cols].copy()
        tmp.columns = ["Date","Ticker","Open","High","Low","Close","Volume"][:len(cols)]
        tmp["Ticker"] = ticker
        dfs.append(tmp)
    df_clean = pd.concat(dfs, ignore_index=True)
else:
    df_clean = df

df_recent = df_clean.tail(10)

# --- Sauvegarder tous les formats ---
md_file = "data/prices_preview.md"
html_file = "data/prices_preview.html"

with open(md_file, "w", encoding="utf-8") as f:
    f.write(df_recent.to_markdown(index=False))
df_recent.to_html(html_file, index=False)

print(f"✅ Markdown saved: {md_file}")
print(f"✅ HTML saved: {html_file}")

# --- Choix interactif si aucun argument ---
modes = args.mode
if not modes:
    print("\nChoose which outputs to open/view:")
    print("1: Markdown (.md)")
    print("2: HTML (.html)")
    print("3: Console")
    choice = input("Enter numbers separated by space (e.g. 1 3): ")
    mapping = {"1": "md", "2": "html", "3": "console"}
    modes = [mapping.get(c) for c in choice.split() if c in mapping]

# --- Fonction cross-platform pour ouvrir un fichier ---
def open_file(path):
    abs_path = os.path.abspath(path)
    system = platform.system()
    if system == "Windows":
        os.startfile(abs_path)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", abs_path])
    else:  # Linux
        subprocess.run(["xdg-open", abs_path])

# --- Ouvrir selon le choix ---
if "md" in modes:
    print(f"Opening {md_file}...")
    open_file(md_file)

if "html" in modes:
    print(f"Opening {html_file} in browser...")
    webbrowser.open_new_tab(os.path.abspath(html_file))

if "console" in modes:
    print("\n--- Console Preview ---\n")
    print(df_recent)
