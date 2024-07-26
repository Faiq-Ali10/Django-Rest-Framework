from django.db import models

class Document(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    nouns = models.JSONField(null=True, blank=True)  # Use JSONField for lists in MongoDB
    verbs = models.JSONField(null=True, blank=True)  # Use JSONField for lists in MongoDB

    def __str__(self):
        return self.email





