from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def cal_score():
    if method.request == "POST":
        path = request.POST.get('file_csv')
        l = csv.DictReader(open(path))
        def add_scores(email, score, name):
            try:
                obj1 = Teacher.objects.get(teacher_email=email)
                obj3 = Assesment.objects.get(assesment_name=name)
                obj2 = Assesment_Teacher.objects.get_or_create(test_id=obj3.id, teacher_id=obj1.id, test_score=score)
                obj2.save()
            except Assesment_Teacher.DoesNotExist:
                pass
        for i in l:
            for j in i:
                if j == 'Timestamp':
                    date = i[j][:8]
                if j=='Email Address':
                    name = i[j]
                if j == 'Score':
                    s=''
                    for k in range(len(i[j])):
                        if i[j][k]=='/':
                            break
                        else:
                            s+=i[j][k]

                    add_scores(email, int(s[:-1]), name_test)
