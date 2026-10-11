import re
import pandas as pd

class IncidentPreprocessor:
    """Preprocesses raw ITSM incident tickets."""
    
    def __init__(self, remove_pii=True):
        self.remove_pii = remove_pii

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower()
        if self.remove_pii:
            text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
            text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP_ADDRESS]', text)
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def process_dataframe(self, df: pd.DataFrame, text_col="description") -> pd.DataFrame:
        df = df.copy()
        df["cleaned_text"] = df[text_col].apply(self.clean_text)
        return df
