from django import forms
from .models import Exam, Result

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["section", "title", "date", "max_marks"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "section": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "max_marks": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["exam", "student", "marks_obtained"]
        widgets = {
            "exam": forms.Select(attrs={"class": "form-select"}),
            "student": forms.Select(attrs={"class": "form-select"}),
            "marks_obtained": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_marks_obtained(self):
        marks = self.cleaned_data.get("marks_obtained")
        exam = self.cleaned_data.get("exam")
        if exam and marks is not None and marks > exam.max_marks:
            raise forms.ValidationError(f"Marks cannot exceed the maximum of {exam.max_marks}")
        return marks
