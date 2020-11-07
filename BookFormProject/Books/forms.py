from django import forms
from django.forms import ModelForm
from Books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        bookname = cleaned_data.get("book_name")
        price = cleaned_data.get("price")
        page = cleaned_data.get("pages")
        obj = Book.objects.filter(book_name=bookname)
        if obj:
            msg = "Book already exist"
            self.add_error("book_name", msg)
        if price < 100:
            msg = "Enter correct price"
            self.add_error("price", msg)
        if page < 50:
            msg = "Pages should be greater than 50"
            self.add_error("pages", msg)


class Bookupdateform(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
