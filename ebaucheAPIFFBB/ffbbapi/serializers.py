from rest_framework import serializers
from ffbbapi.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Match, Place, Member, Organizer, Pool, Day, Team, Club
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class MatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Match
        #fields = ['url','id', 'championship', 'day', 'match_date', 'home', 'visitor', 'score_home', 'score_visitor', 'plan']
        fields = '__all__'

class PlaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'

class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'

class OrganizerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Organizer
        fields = '__all__'

class PoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pool
        fields = '__all__'

class DaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Day
        fields = '__all__'

class TeamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class ClubSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'
