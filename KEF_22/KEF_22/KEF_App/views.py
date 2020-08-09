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

#New changes
def take_assesment(request):
    obj = Assesment.objects.all()
    # obj1 = Assesment_Teacher.objects.all()
    context = {
        'object' : obj
    }
    return render(request, 'assesment.html', context)
    
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
    return render(request, 'assesment.html') #new changes

def visuals_teacher(request):
    l1 = Assesment_Teacher.objects.values_list('teacher_id','scores')
    scores = []
    current_user = request.user
    id = current_user.id
    for i in range(len(l1)):
        if l1[i][0] == id:
            scores.append(l1[i][1])

    plt.plot(scores,'g',label='line one',linewidth=2)
    plt.title("Overall progress of teacher")
    plt.xlabel("No. of Tests")
    plt.ylabel("Scores")
    plt.legend()
    plt.show()
    plt.savefig('static/plot1.png')
    return render(request,'visuals_teacher.html')

def visuals_school(request):
    l1 = Assesment_Teacher.objects.values_list('teacher_id','scores')
    l2 = School_Teacher.objects.values_list('teacher_id','school_id')
    current_school = request.user
    id = current_school.id
    d = {}
    for i in range(len(l2)):
        if l2[i][1] == id:
            d[l2[i][0]]=[]

    for i in range(len(l1)):
        if l1[i][0] in d:
            d[l1[i][0]].append(l1[i][1])

    c=0
    for f in d:
        x = [i for i in range(1,len(d)+1)]
        plt.plot(x,d[f])
        plt.title("Overall progress of teacher in quiz",f)
        plt.xlabel("No. of Teachers")
        plt.ylabel("Scores")
        plt.legend()
        plt.show()
        plt.savefig('plot_school',c,'.png')
        c+=1

    cumm_sum = []
    for i in d:
        cumm_sum.append(sum(d[i])//len(d[i]))
    x = [i for i in range(1,len(d)+1)]
    plt.plot(x,cumm_sum)
    plt.plot(x,d[f])
    plt.title("Overall cummulative progress of teacher in school")
    plt.xlabel("No. of Teachers")
    plt.ylabel("Scores")
    plt.legend()
    plt.show()
    plt.savefig('plot_school.png')
    return render(request,'visuals_school.html')
