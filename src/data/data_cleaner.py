import pandas as pd

def clean_portfolio(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["project_name", "skills", "description", "link"]:
        df[col] = df[col].astype(str).str.strip()

    df["combined_text"] = (
        "Project: " + df["project_name"] +
        "\nSkills: " + df["skills"] +
        "\nDescription: " + df["description"] +
        "\nLink: " + df["link"]
    )

    return df