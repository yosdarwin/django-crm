from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.views import LogoutView
from .models import Lead
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.views.generic import TemplateView, ListView, DetailView
from .forms import CreateLeadModelForm, CreateLeadForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingView(TemplateView):
    template_name = 'landing.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'
    queryset = LogoutView


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('login')


class LeadListView(ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'


# def lead_list(request):
#     context = {
#         'leads': Lead.objects.all()
#     }
#     return render(request, 'lead_list.html', context)


# def home_page(request):
#     context = {
#         'leads': Lead.objects.all()
#     }
#     return render(request, 'homepage.html', context)


class LeadDetailView(DetailView):
    template_name = "lead-details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


# def lead_detail(request, id):
#     context = {
#         'lead':  Lead.objects.get(id=id)
#     }
#     return render(request, 'lead-details.html', context)


# def lead_create(request):
#     if request.method == "POST":
#         form = CreateLeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:list')
#     else:
#         form = CreateLeadModelForm()
#     context = {
#         "form": form
#     }
#     return render(request, "lead-create.html", context)
class LeadUpdateView(UpdateView):
    template_name = 'lead-update.html'
    queryset = Lead.objects.all()
    form_class = CreateLeadModelForm

    def get_success_url(self):
        return reverse('leads:list')


# def lead_update(request, id):
#     lead = Lead.objects.get(id=id)
#     form = CreateLeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = CreateLeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:list')

#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, 'lead-update.html', context)


class LeadDeleteView(DeleteView):
    queryset = queryset = Lead.objects.all()
    template_name = ""

    def get_success_url(self) -> str:
        return reverse("leads:list")


def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect('leads:list')

# def lead_update(request, id):
#     if request.method == "POST":
#         lead = Lead.objects.get(id=id)
#         form = CreateLeadForm(request.POST)
#         if form.is_valid():
#             lead.first_name = form.cleaned_data['first_name']
#             lead.last_name = form.cleaned_data['last_name']
#             lead.age = form.cleaned_data['age']
#             lead.save()
#             return redirect('leads:list')
#     else:
#         form = CreateLeadForm()

#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, 'lead-update.html', context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'lead-create.html'
    form_class = CreateLeadModelForm

    def get_success_url(self):
        return reverse('leads:list')

    def form_valid(self, form):
        send_mail(
            subject="New lead created",
            message="Please go to site to check detail of lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

# def lead_create(request):
#     if request.method == "POST":
#         form = CreateLeadForm(request.POST)
#         if form.is_valid():
#             firstname = form.cleaned_data['first_name']
#             lastname = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=firstname,
#                 last_name=lastname,
#                 age=age,
#                 agent=agent,
#             )
#             return redirect('leads:list')
#     else:
#         form = CreateLeadForm()
#     context = {
#         "form": form
#     }
#     return render(request, "lead-create.html", context)
