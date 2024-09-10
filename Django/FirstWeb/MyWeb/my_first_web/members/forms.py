from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"  #["firstname", "lastname"]  # "__all__"