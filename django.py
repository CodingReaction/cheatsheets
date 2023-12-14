################### CLI ##########################
$python manage.py createcachetable
$python manage.py changepassword *username*

################################ SHortcuts #########################################
render(request, template_name, context=None, content_type=None, status=None)
redirect(to) # Model: get_absolute_url() will be called, Viewname: the reverse will be called. absolute/relative url
get_object_or_404(MyModel, pk=1) # MyModel could be a queryset
get_list_or_404()

################################################# FBV ###############################
HttpResponse("my response", status=200)
HttpResponseNotFound("not found")
raise Http404()
## CBV: https://ccbv.co.uk/

################# SIGNALS ######################################
def my_receiver_function(sender, **kwargs): # declare a receiver
    print("Request finished")

from django.core.signals import request_finished # Connect signal method 1
request_finished.connect(my_receiver_function, sender=None, weak=True, dispatch_uid="unique_identifier_to_avoid_duplication") # django.dispatch.Signal.connect(..)

@receiver(request_finished)                      # Connect signal method 2
def my_decorated_receiver(sender, **kwargs):
    pass


from django.apps imports AppConfig
from django.core.signals import request_finished

class MyAppConfig(AppConfig):
    def ready(self):
        from . import signals # signals decorated with @receiver implicit connected

        request_finished.connect(signals.my_receiver_function) # explicitly connect

@receiver(pre_save, sender=MyModel) # sender is the Model that will trigger the signal on pre_save
def my_handler(sender, **kwargs):
    pass

## Common signals
pre_init # when django model is instantiated. sender=ModelClass / kwargs=dict of model properties
post_init # similar to pre_init but when __init__ is finished, sender= model class, instance = current instance
pre_save # at the beginning of model's save() method, sender = model class, instance = instnace to save
post_save # created=True if new record was created
pre_delete
post_delete
m2m_changed # action = "pre_add"|"post_add"|"pre_remove"|"post_remove"|"pre_clear"|"post_clear"
request_started
request_finished
got_request_exception


################# TEMPLATES ##################################### 
{% extends "base.html" %}
{% load static %}
{% block title %} My title {% endblock %}
{% include "my_component.html" with name="Max" %}

{{ first_name }} # variables and data access
{{ my_dict.key }}
{{ my_obj.attribute }}
{{ my_list.0 }}
{{ task.foo }} # call def foo(self): defined in Task model

{% csrf_token %} #tags
{% cycle 'odd' 'even' %} # as parity
{% if condition1 %} {% elif condition2 %} {% else %} {% endif %}
{% for name in names %} {{ name }} - {{ forloop.counter0 }} {% endfor %}
{% for k, v in my_dict %} ... {% endfor %}
{% debug %}
{% lorem 3 p %}
{% url 'my_app:view-name' v1 v2 %}

## Basic filters
{{ value|default:"default if empty" }}
{{ value|length }} # 7
{{ value|filesizeformat }}
{{ value|safe }}
{{ value|random }}
{{ value|slugify }}
{% autoescape off %} Hello {{ name }} {% endautoescape %}

## Custom Filters
#register.filter(name="replace")
def replace(value, arg):
    return value.replace(arg, "zero")

{{ "0 is a number"|replace:"0" }} # "zero is a number"

@register.filter
@stringfilter #converts to string the value
def lower(value):
    return value.lower()

{{ "HELLO WORLD"|lower }} # "hello world"

## Custom template tags
https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/#writing-custom-template-tags

################# Queues    ####################################
## Basic docker-compose.yml
celery:
    build: ./project
    command: celery --app=core worker --loglevel=info --logfile=logs/celery.log
    volumes:
        - ./project:/usr/src/app # /usr/src/app is the WORKDIR
    environment:
        - DEBUG=1
        - SECRET_KEY=django-secret-key
        - DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
        - CELERY_BROKER=redis://redis:6379/0
        - CELERY_BACKEND=redis://redis:6379/0
    depends_on:
        - django_web
        - redis

## settings on settings.py
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')

#celery.py: in /
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', my_site.settings)
app = Celery('my_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#tasks.py: in /my_app
from celery import shared_task
from django.core.mail import send_mail

from newsletter.models import Issue, Subscription

@shared_task()
def send_issue(issue_id):
    issue = Issue.objects.get(pk=issue_id)
    for subscription in Subscription.objects.filter(newsletter=issue.newsletter):
        send_email.delay('data related')

@shared_task()
def send_email(email, title, content):
    send_mail(title, content, 'newsletter@gmail.com', [email], fail_silently=False)

### a view triggering a task
from tasks.sample_tasks import create_task

@csrf_exempt
def run_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        task = create_task.delay(int(task_type))
        return JsonResponse({"task_id": task.id}, status=202)

from celery.result import AsyncResult

def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)

### for sending the first msg, go to a view or admin action and do something like:
from . import tasks
tasks.send_issue.delay(issue.id)

### autoimport celery when Django starts
from .celery import app as celery_app

__all__ = ("celery_app", )

### CLI
$celery -A my_site worker --loglevel=INFO

### CELERY BEAT for scheduled tasks
# TODO: ver celery beat para tareas de frecuencia diaria: https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html
CELERY_BEAT_SCHEDULE = {
    'scheduled_tasks':{ #name of the task
        'task' : 'my_app.tasks.process_my_pdf' # task function
        'schedule': 10.0, # every 10 seconds
        'schedule': crontab(hour=11, minute=10, day_of_week=3), # or using cron
        'args': (10, 10), # arguments accepted by process_my_pdf
}}


################# Flashing: Messages framework ##################
from django.contrib import messages
MESSAGE_LEVEL: DEBUG | INFO | SUCCESS | WARNING | ERROR
messages.add_message(request, messages.INFO, "Hello world")
messages.success(request, "Profile details updated")
storage = get_messages(request)
for message in storage:
    pass

{% if messages %}
    {% for message in messages %}
      <p {% if message.tags %} class="{{ message.tags }}" {% endif  %}> {{ message }} </div>
      {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %} <b> an error is present! </b> {% endif %}

######################### CACHE #################################
#Different types of caches: 
MEMCACHED: memory-based, runs daemon that alloted RAM: pymemcache binding
REDIS: in-memory db, runs a server: redis-py binding
DATABASE: stores in db, fast if well-indexed db (needs to set LOCATION = my_cache_table
FILESYSTEM: each cache value = separate file. LOCATION = subdirectory path
LOCAL MEMORY CACHING: default one, benefits of mem cached but per-process/thread-safe
#Arguments of CACHES setting:
TIMEOUT: None(never expires) | 5 (5 seconds) | 0 (inmediate expire)
OPTIONS: MAX_ENTRIES | CULL_FREQUENCY | no_delay | max_pool_size (depends on caching strategy)
# Per-site cache: caches the entire site, needs extra MIDDLEWARE:
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware"
]
CACHE_MIDDLEWARE_SECONDS = 300

# Per-view cache: using a decorator
@cache_control(private=True) # 2 kinds of caches: public (server), private( browser), bank account
@cache_control(max_age=3600)
@vary_on_headers("User-Agent", "Cookie") # @vary_on_cookie
@cache_page(60 * 15, cache='special_cache')
def my_view(request):
    pass

# Low level cache api:
cache.add("add_key", "Initial value") # add if doesn't exists
cache.set('my_key', "hello world", 30)
cache.get('my_key', default=None) #returns None if expired or doesnt exists
cache.get_many(['a', 'b', 'c'])
cache.set_many({'a': 1, 'b': 2, 'c': 3})
cache.delete('my_key')
cache.delete_many([...])
cache.clear()
cache.touch('my_key', 10) # set new expiration time

######################################### FORMS ##################################
from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label="Your name", max_length=100)
    description = forms.CharField(widget=forms.text

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
        fields = "__all__"
        exclude = ["secret"]
        widgets = {
            "content": Textarea(attrs={"cols": 80, "rows": 20}),}
        labels = {
            "content": _("My content"),}
        help_texts = {
            "content": _("Some help text"),}
        error_mesages = {
            "name": {
                "max_lengh": _("Too long"),}}
        
        # ForeignKey = django.forms.ModelChoiceField
        # ManyToManyField = django.forms.ModelMutlipleChoiceField


def get_name_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return redirect('thanks')
    else:
        form = NameForm()
    return render(request, 'name_template.html', {"form": form})

def article_view(request):
    form = ArticleForm(request.POST, instance=None|Article)
    form.save() #optional commit=False


<form> {{ form }} </form>

{{ form.non_field_errors }}
{% for field in form %}
  <div>
     {{ field.errors }}
      {{ field.label_tag }}
        {{ field }}

class CalendarWidget(forms.TextInput):
    class Media: # can also be used in forms
        css = {
            "all": ["custom.css"]
        }
        js = ["anims.js", "other_script.js"]

# render form using template:
rendered_form = MyForm().render('form_snippet.html')
return render(request, "index.html", {"form": rendered_form})

# Forms with FileField or ImageField
{% if form.is_multipart %}
    <form enctype="multipart/form-data"></form>
{% else %}
    <form></form>
{% endif %}
#bound form with image field:
from django.core.files.uploadedfile import SimpleUploadedFile
data = {"subjet": "hello", "message": "Hi there"}
file_data = {"mugshot": SimpleUploadedFile("face.jpg", b"file data")}
form = ContactFormWithMugshot(data, file_data) # in the example
form = ContactFormWithMugshot(request.POST, request.FILES) # in practice
form = ContactForm(initial={"subject": "Hi there!"}) #autofill unbound form at runtime, ex. with username session

form.is_valid()
form.is_multipart() # True
form.is_bound() # true or false if have or not data, emtpy dict = bound with empty data
form.has_changed() # if changed from initial data
form.changed_data  #list of names of fields with values different from initial
form.cleaned_data
form.fields
form.hidden_fields
form.errors #{'username': ['Must include digits', 'too short'], 'email': ['Already used']}
form.non_field_errors()
form.errors.as_json() #{"email":[{"message": "invalid email", "code": "invalid"}]}
form.add_error(TODO)
form.has_error(field_name, code=None)

form["email"].data         # "max@max.com" or None
form["email"].value()      # "max@max.com" or Initial, rendered the same way widget would do
form.fields["email"]       # <input type=... />
form.fields["email"].label # <label for=... >

form["email"].errors # ['This field is required']
form["email"].help_text
form["email"].widget_type

############################## Auth && permissions        ##############################
u = User.objects.get(username="max") #change password
u.set_password("bacalao")
u.save()

from django.contrib.auth import authenticate, login
user = authenticate(username='max', password='secret')
if user is not None:
    login(request, user) #logout(request)
    # redirect to success page
else:
    pass # user is not registered anywhere

if request.user.is_authenticated:
    pass # user is registered
else:
    pass # this is an AnonymousUser instance


from django.contrib.auth.decorators import login_required

@login_required # if not logged redirect user to settings.LOGIN_URL
def my_view(request):
    pass

#if the view is a CBV use the LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"

#limit access based on another conditions like custom one or permission
from django.contrib.auth.decorators import user_passes_test, permission_required

def email_check(user):
    return user.email.endswith("@example.com")

@permission_required("polls.add_choice")
@user_passes_test(email_check)
def my_view(request):
    pass


my_user.groups.set([group_list])
my_user.groups.add(group, group2,...)
my_user.groups.remove(group, group2, ..)
my_user.groups.clear()
my_user.user_permissions.set(...)

## Authentication views: https://docs.djangoproject.com/en/4.2/topics/auth/default/#all-authentication-views
LoginView | LogoutView | PasswordChangeView | PasswordChangeDoneView | PasswordResetView | PasswordResetDoneView
AdminPasswordChangeForm
AuthenticationForm
path("accounts/", include("django.contrib.auth.urls"))
path("change-password/", auth_views.PasswordChangeView.as_view(template_name="change-password.html")) # for more control


############################## Admin                      ###############################
from django.contrib import admin

@admin.register(Author) #avoids doing the admin.site.register() thing
class AuthorAdmin(admin.ModelAdmin): # for custom admin interface
    fields = ["name", "title"]
    exclude = ["password"]

admin.site.register(Author, AuthorAdmin) # same as admin.site.register(Author)

## more admin docs: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
## admin actions: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/



############################## Logging: builtin python module ###########################
#configure the logger in settings.py

LOGGING={
    "handlers": {
        "console":{
            "class": "logging.StreamHandler",
            }, ...}}

################################# Session storage ####################################
request.session # a dictionary that comes with every request serialized as JSON
#ex. user can only post a comment once:
def post_comment(request, new_comment):
    if request.session.get("has_commented", False):
        return HttpResponse("You've already commented")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session["has_commented"] = True
    return HttpResponse("Thanks for your comment!")

## session outside of a view:
from django.contrib.sessions.backends.db import SessionStore
s = SessionStore()
s["last_login"] = 1376587090
s.create()
s.session_key # '2b1189afsadfsadf'
s = SessionStore(session_key='2bfsdafsdafsssa')


################################# PAGINATION #########################################
from django.core.paginator import Paginator
paginator = Paginator(Product.objects.all(), 100) # 100 items per page
page_obj = paginator.get_page(request.GET.get('page'))

# Decorators: django.contrib.auth.decorators

## USER_PASSES_TEST decorator
def email_check(user):
    return user.email.endswith("@example.com")

@user_passes_test(email_check) #optional login_url=settings.LOGIN_URL
def my_view(request):
    pass

## PERMISSION_REQUIRED decorator
@permission_required("polls.add_choice") # checks if user have the permission
def my_view(request):
    pass

## LOGIN_REQUIRED decorator
@login_required
def my_view(request):
    pass

################# MODEL: django.db.models ###################################

# 3 types of Inheritance: Abstract Base Model, Multi-table and Proxy Model

### BASICS
CharField(max_length=100)
BooleanField(help_text="if age is greatter than 18")
IntegerField()
FloatField()
TextField()
DateField() #auto_now | auto_now_add
DateTimeField()
SlugField(unique=True)
URLFIeld()


### ADVANCED
CharField(max_length=1, choices=[("S", "Small"), ("M", "Medium")]) # enumeration / enum field. 
# if shirt_size = CharField(choices) then item.shirt_size ["S"], item.get_shirt_size_display() ["Small"]
EmailField()
FileField(upload_to="uploads/") # uploaded to MEDIA_ROOT/uploads, MEDIA_URL is the url to access the file
ImageField(upload_to="...")
JSONField()
UUIDFIeld(primary_key=True, default=uuid.uuid4, editable=False)

#Attribs
default, max_length, choices, help_text, primary_key, unique, unique_together, index, index_together

### RELATIONSHIPS
ForeignKey(Question,                          # 'production.Question' another app
        on_delete=models.CASCADE,             # on_delete: SET_NULL, SET_DEFAULT, SET()
        limit_choices_to={"answered": False}, #only answered questions
        related_name="answers")               # reverse name, "+" to avoid reverse of question. 
ManyToManyField(Group,          # "self" for Tag<->Tag relationship
        db_table="groups", #autogenerated using the names of both tables
        though="Membership",   #use an intermediate table Membership to add extra attribs
        though_fields=("group", "person",)) # FK in the intermediate table
OneToOneField(Profile, related_name="profile")

class Person(...)
class Group(...) members = models.ManyToManyField(Person, through="Membership")
class Membership(...): person = models.Foreign.. ; group = models.Foreign..., invite_reason = models.CharField(...)



### OTHERS
BinaryField()
DecimalField(max_digits=None, decimal_places=None)
DurationField()
GenericIPAddressField()
TimeField() # represented as python: datetime.time

### class Meta
abstract = True
proxy = True # uses the same table, needs to inherit from another Model
ordering = ["field_name"]
db_table = "table_name"
verbose_name = "Study"
verbose_name_plural = "Studies"
class Meta(CommonInfo.Meta, Unmanaged.Meta) # inherit multiple Meta classes

### Methods
def save(self, *args, **kwargs):
    if self.name == "Max":
        return # don't save!
    else:
        super().save(*args, **kwargs)

######## Models and QuerySet
class BookingQuerySet(models.QuerySet):
    # Custom, chainable methods added here, which will
    # do lower level 'filter', 'order_by' etc.
    def in_basket(self):
        return self.filter(shelved=False, confirmed=False)

    def for_year(self, year):
        return self.filter(start_date__year=year)

    # etc.


class Booking(models.Model):
    # fields etc

    objects = BookingQuerySet.as_manager()

joe = Author.objects.create(name="Joe") # objects is the default Manager of the Model
entry.authors.add(joe) # m2m field
filter(...) / exclude(...)
order_by("-date")
.get(pk=1) # also objects.all().get() works
name__exact="Max"
name__contains
name__startswith
phone__isnull
number_comments__gt=F("number_of_pingbacks") # field on the same model, F() expressions

## Aggregation
Book.objects.filter().count()

from django.db.models import Avg, Max, Min, Count, Sum
Book.objects.aggregate(Avg("price")) # {'price__avg': 34.35}
Book.objects.aggregate(Max("price")) # {'price__max': Decimal('81.20')}

## Constraints
class Customer(models.Model):
    age = models.IntegerField()
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name="age_gte_18"),
        ]


TODO::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Testing
## Mailing
## i18n
## advanced with Subquery: https://docs.djangoproject.com/en/4.2/ref/models/expressions/


############### MANAGERS: https://docs.djangoproject.com/en/4.2/topics/db/managers/ ####################################


############### Async in Django ################################################


########################## STRIPE
# Prices, PaymentIntents (linked to Stripe Customer)
# https://github.com/stripe/stripe-python
# 1 - Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY
# 2 - Product model: contains name and stripe_product_id
# 3 - Price model: contains product, stripe_price_id and price Integer (in cents)
# 4 - Add views for StripeCheckout, Success and Cancel
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)
# 5 - Install the CLI to test webhooks:  stripe listen --forward-to localhost:8000/webhooks/stripe/ and add SPRITE_WEHOOK_SECRET
# 6 - Add webhook handler view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        line_items = stripe.checkout.Session.list_line_items(session["id"])

        stripe_price_id = line_items["data"][0]["price"]["id"]
        price = Price.objects.get(stripe_price_id=stripe_price_id)
        product = price.product

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. The URL is: {product.url}",
                recipient_list=[customer_email],
                from_email="your@email.com"
            )


    return HttpResponse(status=200)

# 7 - Custom payment flow https://stripe.com/docs/payments/quickstart
class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            price = Price.objects.get(id=self.kwargs["pk"])
            intent = stripe.PaymentIntent.create(
                amount=price.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "price_id": price.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
# TODO: review tutorial https://justdjango.com/blog/django-stripe-payments-tutorial

########################## PAYPAL


########################## PAYONEER
