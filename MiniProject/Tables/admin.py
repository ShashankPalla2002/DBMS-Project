from django.contrib import admin
from .models import Person_Related, Government_Related, Property_Related,IPC_Sections,Judgements, IT_Acts

admin.site.register(Person_Related)
admin.site.register(Government_Related)
admin.site.register(Property_Related)
admin.site.register(IPC_Sections)
admin.site.register(IT_Acts)
admin.site.register(Judgements)