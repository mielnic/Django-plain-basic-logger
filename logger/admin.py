from django.contrib import admin
from .models import LogEntry
from unfold.admin import ModelAdmin

@admin.register(LogEntry)
class LogEntryAdmin(ModelAdmin):
    list_display = ('timestamp', 'level', 'message')
    search_fields = ('level', 'message')
    readonly_fields = ('timestamp', 'level', 'message')

    def has_add_permission(self, request):
        return False  # Disables the ability to add log entries manually through the admin

    def has_change_permission(self, request, obj=None):
        return False  # Disables the ability to edit log entries through the admin