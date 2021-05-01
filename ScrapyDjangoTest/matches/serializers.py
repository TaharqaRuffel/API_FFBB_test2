from rest_framework import serializers
from matches.models import Match
from django.contrib.auth.models import User


class MatchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedModelSerializer(view_name='match-highlight', format='html')

    class Meta:
        model = Match
        fields = ['id', 'championship', 'day', 'match_date', 'home', 'visitor', 'score_home', 'score_visitor', 'plan',
                  'owner']
