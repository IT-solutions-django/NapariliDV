from .models import CompanyInfo


def company_info(request):
    try:
        info = CompanyInfo.get_instance()
    except CompanyInfo.DoesNotExist:
        info = None

    context = {
        'company_info': info,
    }

    return context
