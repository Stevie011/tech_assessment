from import_export import resources
from .models import IncomeExpenses

class ExcelSheetResource(resources.ModelResource):
    class Meta:
        model = IncomeExpenses