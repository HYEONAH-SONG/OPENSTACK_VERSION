from django import forms

class Resource(forms.Form):
    img=[
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac os', 'Mac OS'),
    ]
    lan=[
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Javascript', 'Javascript'),
        ('Python', 'Python'),
    ]
  
    # flav=[
    #     ('m1.tiny', 'm1.tiny'),
    #     ('m1.small', 'm1.small'),
    #     ('m1.medium', 'm1.medium'),
    #     ('m1.large', 'm1.large'),
    #     ('m1.xlarge', 'm1.xlarge'),
    # ]

    # flavor = forms.ChoiceField(\
    #     required= True,\
    #     label='학생 수 Flavor 'ㄴ,\
    #     initial='none',\
    #     error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
    #     disabled=False,
    #     choices=flav,
    # )

    image = forms.ChoiceField(\
        required= True,\
        label='운영체제 ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=img,
    )

    language = forms.ChoiceField(\
        required= True,\
        label='Language ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=lan,
    )
    
    
    
