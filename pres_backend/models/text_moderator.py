# Text moderation using Presidio
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from config import LOG_FILE

class TextModerator:
    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def moderate_text(self, content):
        results = self.analyzer.analyze(
            text=content, 
            entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"],
            language="en"
        )

        if results:
            anonymized_text = self.anonymizer.anonymize(
                text=content,
                analyzer_results=results
            ).text
            self.log_violation(content)
            return anonymized_text

        return content

    def log_violation(self, content):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"Violation detected in text: {content}\n")
