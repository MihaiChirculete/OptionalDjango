from django import forms


class EmailArticleForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class SupportEmail(forms.Form):
    TicketTitle = forms.CharField(max_length=40)
    EmailUser = forms.EmailField()
    complaint = forms.CharField(required=True,
                               widget=forms.Textarea,
                                max_length=150)