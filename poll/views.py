from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Phonebase, Article, Comments, Unique_set
from .forms import ChatForm
import nltk
from nltk.stem.lancaster import LancasterStemmer

# Для загрузки файла
from .forms import UploadFileForm


stemmer = LancasterStemmer()
import numpy
import tflearn
import random
import json
import pickle


def calculator(request):
    return render(request, 'poll/calculator.html')


def support(request):
    contact_list = Phonebase.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'poll/support.html', {'contacts': contacts})


def Tank(request):
    contact_list = Tank.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'poll/support.html', {'contacts': contacts})


def order(request):
    return render(request, 'poll/order.html')


def unique(request):
    return render(request, 'poll/unique.html')


def all(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        name_host = request.META.get('SERVER_PORT')
        method = request.META.get('REQUEST_METHOD')

        # Unique_set.objects.create(UserAgent=user_agent, IP_user=ip)
        asq = Unique_set.objects.get_or_create(UserAgent=user_agent, IP_user=ip)
        if asq[1] == False:
            data = {"ip": ip, "user_agent": user_agent, "name_host": name_host, "method": method}
            return render(request, 'poll/all.html', context=data)

        return render(request, 'poll/unique.html')


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))


"""CHAT"""


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


MODEL = None

def get_model():
    global MODEL
    if MODEL is None:
        words, labels, training, output = get_hdata()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        MODEL = tflearn.DNN(net)
        MODEL.load("model.tflearn")
    return MODEL

DATAA = None
def get_data():
    global DATAA

    if DATAA is None:
        with open("intents.json") as file:
            DATAA = json.load(file)
    return DATAA


HDATA = None
def get_hdata():
    global HDATA

    if HDATA is None:
        with open("data.pickle", "rb") as f:
            HDATA = pickle.load(f)
    return HDATA


def chat(request):
    out = "her"
    if "your_name" in request.POST:
        words, labels, training, output = get_hdata()
        results = get_model().predict([bag_of_words(request.POST["your_name"], words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in get_data()["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        out=random.choice(responses)

    return render(request, 'poll/chat.html',context={'name':out})

"""CHAT  END"""


def basic_one(request):
    view = "basic_one"
    html = "<html><body> this is %s view </body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    return render(request, 'poll/myview.html', {'name': view})


def art1icles(request):
    view = "template_two"
    return render(request, 'poll/myview.html', {'name': view})


def articles(request):
    return render(request, 'poll/articles.html', {'articles': Article.objects.all()})


def article(request, article_id=2):
    return render(request, 'poll/article.html', {'article': Article.objects.get(id=article_id),
                                                 "comments": Comments.objects.filter(comments_article_id=article_id)})





def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
    else:
        form = UploadFileForm()
    return render(request, ('poll/articles.html', {'form': form}))




