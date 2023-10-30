from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


class StudentRegisterView(CreateView):
    template_name = 'students/student/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        user = authenticate(
            username=cleaned_data['username'],
            password=cleaned_data['password']
        )
        login(self.request, user)
        return result
