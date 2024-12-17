from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView)
from .models import (Application, ApplicationComponentItem,
                     ApplicationServiceItem)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from django.http import HttpResponseRedirect, HttpResponse
from catalog.models import Component, Service
from django.conf import settings
from django.template.loader import render_to_string
import weasyprint


@method_decorator(login_required, name='dispatch')
class ApplicationListView(ListView):
    """Список услуг."""

    model = Application
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        for application in context['object_list']:
            application.can_edit = application.master == self.request.user
            application.edit_url = reverse(
                'applications:application_edit',
                args=[application.id]) if application.can_edit else None
            application.delete_url = reverse(
                'applications:application_delete',
                args=[application.id]) if application.can_edit else None
            application.cost = application.get_total_cost()
        return context


@method_decorator(login_required, name='dispatch')
class ApplicationCreateView(CreateView):
    """."""

    model = Application
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['components'] = Component.objects.all()
        context['services'] = Service.objects.all()
        return context

    def form_valid(self, form):
        """Обработка POST-запроса при создании заявки."""
        application = form.save()

        create_resources(self.request, application)

        return HttpResponseRedirect(reverse('applications:applications_list'))


@method_decorator(login_required, name='dispatch')
class ApplicationEditView(UpdateView):
    """."""

    model = Application
    form_class = ApplicationForm

    def dispatch(self, request, *args, **kwargs):
        """Проверка доступа к редактированию."""
        application = self.get_object()
        if application.master != request.user:
            return render(request, '404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Добавляем компоненты и услуги в контекст."""
        context = super().get_context_data(**kwargs)
        context['components'] = Component.objects.all()
        context['services'] = Service.objects.all()
        context['selected_components'] = {
            item.component.id: item.quantity
            for item in self.object.component_items.all()
        }
        context['selected_services'] = {
            item.service.id: item.quantity
            for item in self.object.service_items.all()
        }
        return context

    def form_valid(self, form):
        """Обработка сохранения изменений."""
        application = form.save()

        ApplicationComponentItem.objects.filter(
            application=application).delete()

        ApplicationServiceItem.objects.filter(
            application=application).delete()

        create_resources(self.request, application)

        return HttpResponseRedirect(reverse('applications:applications_list'))


def create_resources(request, application):
    """."""
    components_ids = request.POST.getlist('components')
    for component_id in components_ids:
        quantity = int(request.POST.get(
            f'component_quantity_{component_id}', 0)
        )
        if quantity:
            component = Component.objects.get(id=component_id)
            ApplicationComponentItem.objects.create(
                application=application,
                component=component,
                quantity=quantity
            )

    services_ids = request.POST.getlist('services')
    for service_id in services_ids:
        quantity = int(request.POST.get(
            f'service_quantity_{service_id}', 0)
        )
        service = Service.objects.get(id=service_id)
        ApplicationServiceItem.objects.create(
            application=application,
            service=service,
            quantity=quantity
        )


@method_decorator(login_required, name='dispatch')
class ApplicationDeleteView(DeleteView):
    """."""

    model = Application


@login_required
def create_application_pdf(request, application_id):
    """."""
    application = get_object_or_404(Application, pk=application_id)
    context = {
        'application': application,
        'selected_components': ApplicationComponentItem.objects.filter(
            application=application),
        'selected_services': ApplicationServiceItem.objects.filter(
            application=application),
    }
    html = render_to_string('applications/application_pdf.html',
                            context=context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{application.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    return response