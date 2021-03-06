from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    """
    Abstract admin models for populating columns updated_by and created_by
    """
    exclude = ('updated_by', 'created_by',)
    def save_form(self, request, form, change):
        obj = super(ModelAdmin, self).save_form(request, form, change)
    
        if hasattr(obj, 'updated_by'):
            obj.updated_by = unicode(request.user)
       
        if hasattr(obj, 'created_by') and not obj.created_by:
            obj.created_by = unicode(request.user)
            
        return obj