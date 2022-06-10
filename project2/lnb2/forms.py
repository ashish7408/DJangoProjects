from django import forms
from .models import StudentDetails


# creating a form
class StudentForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = StudentDetails

		# specify fields to be used
		fields = [
			"Name",
			"City",
            "Class",
            "Age",
            "RollNo",
		]
