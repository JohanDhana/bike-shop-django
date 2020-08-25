from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',  'placeholder': 'Phone'}))


class HomeSearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'searchTerm', 'placeholder': 'What are you looking for?'}))


class SearchForm(forms.Form):
    choices_category = [('', 'Kategori'), ('1-BMX', 'BMX'), ('2-MTB', 'MTB')]
    choices_size = [('12', '12'), ('14', '14'),
                    ('16', '16'), ('20', '20'), ('26', '26')]

    query = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form__field form-control w-100 mt-3 mb-0 shadow-none', 'placeholder': 'Search'}))
    category = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', }), choices=choices_category, required=False)
    size = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', }), choices=choices_size)
