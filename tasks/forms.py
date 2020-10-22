from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'What do you want to do today?',
            }
        )
    )
