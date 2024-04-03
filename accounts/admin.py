from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
     
    list_display = ('email', 'username', )