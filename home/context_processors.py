from .models import CompanyInfo
from contacts.forms import FeedbackForm


def company_info(request):
    try:
        info = CompanyInfo.get_instance()
    except CompanyInfo.DoesNotExist:
        info = None

    context = {
        'company_info': info,
    }

    return context


def modal_feedback_form(request):
    modal_feedback_form = FeedbackForm()

    context = {
        'modal_feedback_form': modal_feedback_form,
    }

    return context