import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class RuleBasedTriage:
    """Rule-based baseline ticket triage classifier."""
    def predict(self, texts):
        results = []
        for text in texts:
            t = text.lower()
            if "database" in t or "postgresql" in t or "sql" in t:
                results.append("DBA_Team")
            elif "password" in t or "login" in t or "access" in t:
                results.append("Service_Desk_L1")
            elif "vpn" in t or "network" in t or "dns" in t:
                results.append("Network_Ops")
            elif "kubernetes" in t or "pod" in t or "docker" in t:
                results.append("DevOps_L2")
            else:
                results.append("Service_Desk_L1")
        return np.array(results)

class TFIDFLogisticTriage:
    """TF-IDF + Logistic Regression triage classifier."""
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)
        self.clf = LogisticRegression(max_iter=1000)

    def fit(self, X, y):
        X_vec = self.vectorizer.fit_transform(X)
        self.clf.fit(X_vec, y)

    def predict(self, X):
        X_vec = self.vectorizer.transform(X)
        return self.clf.predict(X_vec)

    def predict_proba(self, X):
        X_vec = self.vectorizer.transform(X)
        return self.clf.predict_proba(X_vec)
