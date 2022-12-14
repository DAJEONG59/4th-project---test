from django import forms
from diary.models import Memory, KeywordPost, ImageFields, FinImg


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        # fields = "__all__"
        fields = ["content_long", "Weather", "Drawing", "Emotion"]


      


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ["content_short", "Weather", "Drawing", "Emotion"]


class ImgForm(forms.ModelForm):
    class Meta:
        model = FinImg
        fields = ['finImg']