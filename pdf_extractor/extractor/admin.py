from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'pdf_file')
    search_fields = ('email',)

