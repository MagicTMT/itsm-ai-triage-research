import numpy as np

class HumanOversightManager:
    """Manages human-in-the-loop escalation protocols based on decision confidence."""
    def __init__(self, confidence_threshold=0.85, fallback_group="L2_Human_Triage"):
        self.confidence_threshold = confidence_threshold
        self.fallback_group = fallback_group

    def evaluate_routing(self, predicted_group, proba_distribution):
        max_confidence = float(np.max(proba_distribution))
        if max_confidence < self.confidence_threshold:
            return {
                "assigned_group": self.fallback_group,
                "confidence": max_confidence,
                "escalated": True,
                "reason": "Low AI confidence score below threshold"
            }
        return {
            "assigned_group": predicted_group,
            "confidence": max_confidence,
            "escalated": False,
            "reason": "Automated AI routing approved"
        }
