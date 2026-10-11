import pandas as pd
from src.data.preprocessor import IncidentPreprocessor
from src.models.classifier import TFIDFLogisticTriage

def train_pipeline():
    print("Loading synthetic training dataset...")
    df = pd.read_csv("data/synthetic/sample_tickets.csv")
    preprocessor = IncidentPreprocessor()
    df = preprocessor.process_dataframe(df)
    
    clf = TFIDFLogisticTriage()
    clf.fit(df["cleaned_text"], df["assigned_group"])
    print("Model training finished successfully.")

if __name__ == "__main__":
    train_pipeline()
