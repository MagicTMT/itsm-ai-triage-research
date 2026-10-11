import numpy as np
from sklearn.metrics import precision_recall_fscore_support

def compute_triage_metrics(y_true, y_pred, latency_ms_list):
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='macro', zero_division=0)
    avg_latency = float(np.mean(latency_ms_list)) if len(latency_ms_list) > 0 else 0.0
    return {
        "precision": round(float(precision), 2),
        "recall": round(float(recall), 2),
        "f1_score": round(float(f1), 2),
        "avg_latency_ms": round(avg_latency, 1)
    }

def calculate_bottleneck_reduction(baseline_latency, new_latency):
    if baseline_latency == 0:
        return 0.0
    return round(((baseline_latency - new_latency) / baseline_latency) * 100, 1)
