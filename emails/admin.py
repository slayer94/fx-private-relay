from django.contrib import admin

from .models import DeletedAddress, DomainAddress, Profile, RelayAddress


class DeletedAddressAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


class RelayAddressAdmin(admin.ModelAdmin):
    pass


class DomainAddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(DeletedAddress, DeletedAddressAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(RelayAddress, RelayAddressAdmin)
admin.site.register(DomainAddress, DomainAddressAdmin)
