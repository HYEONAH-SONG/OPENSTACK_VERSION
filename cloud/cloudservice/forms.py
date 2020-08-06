from django import forms

class Resource(forms.Form):
    lan=[
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Javascript', 'Javascript'),
        ('Python', 'Python'),
    ]
    img=[
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac os', 'Mac OS'),
    ]
    flav=[
        ('m1.tiny', 'm1.tiny'),
        ('m1.small', 'm1.small'),
        ('m1.medium', 'm1.medium'),
        ('m1.large', 'm1.large'),
        ('m1.xlarge', 'm1.xlarge'),
    ]

    language = forms.ChoiceField(\
        required= True,\
        label='Language ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=lan,
    )
    image = forms.ChoiceField(\
        required= True,\
        label='Image ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=img,
    )
    flavor = forms.ChoiceField(\
        required= True,\
        label='Flavor ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=flav,
    )
    
