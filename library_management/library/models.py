from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    CATEGORY_OPTIONS=[
        ('Novel','novel'),
        ('Poem','poem'),
        ('Article','article'),
        ('Chatstory','chatstory'),
        ('Manga','manga'),
    ]
    category=models.CharField(max_length=100,choices=CATEGORY_OPTIONS)
    isbn=models.CharField(max_length=12)
    available_copies=models.IntegerField(null=True)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    borrower_name=models.CharField(max_length=100)
    borrower_email=models.EmailField()
    borrow_date=models.DateField(auto_now_add=True)
    is_returned=models.BooleanField()
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.borrower_name
