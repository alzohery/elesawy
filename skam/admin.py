import datetime
from django.contrib import admin
from skam.models import Skamdata
import csv
from django.http import HttpResponse
# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = 'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [ field for field in opts.get_fields() if not \
        field.many_to_many and not field.one_to_many ] 
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class SkamdataAdmin(admin.ModelAdmin):
    list_display = ['name', 'passwoard', 'country', 'created']
    search_fields = ['name', 'country']
    list_filter = [ 'name', 'country', 'created']
    actions = [export_to_csv]


admin.site.register(Skamdata, SkamdataAdmin)