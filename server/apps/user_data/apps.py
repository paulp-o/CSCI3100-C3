from django.apps import AppConfig


class UserDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_data'  # Updated to reflect the nested structure

    def ready(self):
        import apps.user_data.signals  # Ensure this import reflects the new structure
