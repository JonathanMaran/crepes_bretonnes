from django import forms


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de Pizza !")

        return message  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # si sujet et message sont valides
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message",  # permet de faire référence au champ message pour le message d'erreur
                               "Vous parlez de pizzas dans le sujet, n'en parlez plus dans le message !!!"
                               # message d'erreur
                               )

        return cleaned_data  # on oublie pas de renvoyer les données si tout est ok


"""
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
"""


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
