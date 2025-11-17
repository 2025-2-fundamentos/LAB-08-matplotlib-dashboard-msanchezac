# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

from pathlib import Path
import os


def pregunta_01():
    """
    Genera un dashboard estático basado en shipping-data.csv.
    Los archivos deben guardarse en la carpeta docs/.
    """

    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    project_root = Path.cwd()

    csv_path = project_root / "files" / "input" / "shipping-data.csv"
    docs_dir = project_root / "docs"

    docs_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    df["Warehouse_block"].value_counts().sort_index().plot(
        kind="bar", color="#4C72B0", ax=ax1
    )
    ax1.set_title("Shipments per Warehouse Block")
    ax1.set_xlabel("Warehouse Block")
    ax1.set_ylabel("Number of Shipments")
    fig1.tight_layout()
    fig1.savefig(docs_dir / "shipping_per_warehouse.png", dpi=150)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    df["Mode_of_Shipment"].value_counts().sort_index().plot(
        kind="bar", color="#55A868", ax=ax2
    )
    ax2.set_title("Mode of Shipment")
    ax2.set_xlabel("Mode")
    ax2.set_ylabel("Number of Shipments")
    fig2.tight_layout()
    fig2.savefig(docs_dir / "mode_of_shipment.png", dpi=150)
    plt.close(fig2)

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    df.groupby("Warehouse_block")["Customer_rating"].mean().sort_index().plot(
        kind="bar", color="#C44E52", ax=ax3
    )
    ax3.set_title("Average Customer Rating by Warehouse")
    ax3.set_xlabel("Warehouse Block")
    ax3.set_ylabel("Average Rating")
    fig3.tight_layout()
    fig3.savefig(docs_dir / "average_customer_rating.png", dpi=150)
    plt.close(fig3)

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    df["Weight_in_gms"].plot(kind="hist", bins=20, color="#8172B2", ax=ax4)
    ax4.set_title("Weight Distribution (gms)")
    ax4.set_xlabel("Weight in gms")
    ax4.set_ylabel("Frequency")
    fig4.tight_layout()
    fig4.savefig(docs_dir / "weight_distribution.png", dpi=150)
    plt.close(fig4)

    html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Shipping Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { border: 1px solid #ddd; padding: 10px; box-shadow: 2px 2px 4px rgba(0,0,0,0.05); }
        img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="grid">
        <div class="card">
            <h3>Shipments per Warehouse</h3>
            <img src="shipping_per_warehouse.png" alt="Shipments per Warehouse">
        </div>
        <div class="card">
            <h3>Mode of Shipment</h3>
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
        </div>
        <div class="card">
            <h3>Average Customer Rating</h3>
            <img src="average_customer_rating.png" alt="Average Customer Rating">
        </div>
        <div class="card">
            <h3>Weight Distribution</h3>
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>
</body>
</html>
"""
    (docs_dir / "index.html").write_text(html, encoding="utf-8")

    return None
