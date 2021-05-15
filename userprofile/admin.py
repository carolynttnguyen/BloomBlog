from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


# inline admin
class ProfileInline(admin.StackedInline):
    model= Profile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# associate Profile to User
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# re-register the user
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
