from django.core.validators import RegexValidator
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class Place(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    post_code = models.CharField(max_length=5, validators=[
        RegexValidator(regex='^.{5}$', message='Length has to be 5', code='nomatch')])
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Place, self).save(*args, **kwargs)


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name


class Organizer(models.Model):
    title = models.CharField(max_length=100)
    president = models.ForeignKey('Member', related_name="organizer_presidents", on_delete=models.SET_NULL, null=True)
    correspondent = models.ForeignKey('Member', related_name="organizer_correspondents", on_delete=models.SET_NULL,
                                      null=True)

    def __str__(self):
        return self.title


class Championship(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    # pool = models.ForeignKey('Pool', on_delete=models.SET_NULL,null=True)
    organizedBy = models.ForeignKey('Organizer', related_name='championships', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Pool(models.Model):
    code = models.CharField(max_length=25, primary_key=True)
    title = models.CharField(max_length=100)
    championship = models.ForeignKey('Championship', related_name='pools', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Day(models.Model):
    title = models.IntegerField
    pool = models.ForeignKey('Pool', related_name='days', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Match(models.Model):
    day = models.ForeignKey('Day', related_name='matches', on_delete=models.SET_NULL, null=True)
    match_date = models.DateTimeField()
    home = models.ForeignKey('Team', related_name='matches_home', on_delete=models.SET_NULL, null=True)
    visitor = models.ForeignKey('Team', related_name='matches_visitor', on_delete=models.SET_NULL, null=True)
    score_home = models.SmallIntegerField(default=0)
    score_visitor = models.SmallIntegerField(default=0)
    gym = models.ForeignKey('Place', related_name='matches', on_delete=models.SET_NULL, null=True)

    # class Match(models.Model):
    #     created = models.DateTimeField(auto_now_add=True)
    #     updated = models.DateTimeField(auto_now_add=True)
    #     championship = models.CharField(max_length=100)
    #     day = models.IntegerField()
    #     match_date = models.DateTimeField()
    #     home = models.CharField(max_length=100)
    #     visitor = models.CharField(max_length=100)
    #     score_home = models.SmallIntegerField(default=0)
    #     score_visitor = models.SmallIntegerField(default=0)
    #     plan = models.CharField(max_length=100, null=True)
    #     # gym = models.ForeignKey('Gym', on_delete=models.SET_NULL,null=True)
    #     owner = models.ForeignKey('auth.User', related_name='matches', on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ['created']


class Team(models.Model):
    title = models.CharField(max_length=50, null=True)
    club = models.ForeignKey('Club', related_name='teams', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Club(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    couleur = models.CharField(max_length=15)
    address = models.ForeignKey(Place, related_name='clubs_address', on_delete=models.SET_NULL, null=True)
    gym = models.ForeignKey(Place, related_name='clubs_gym', on_delete=models.SET_NULL, null=True)
    ligue = models.ForeignKey(Organizer, related_name='clubs', on_delete=models.SET_NULL, null=True)
    comite = models.ForeignKey(Organizer, related_name='comite', on_delete=models.SET_NULL, null=True)
    president = models.ForeignKey('Member', related_name='clubs_president', on_delete=models.SET_NULL, null=True)
    correspondent = models.ForeignKey('Member', related_name='clubs_correspondent', on_delete=models.SET_NULL,
                                      null=True)

    def __str__(self):
        return self.title
