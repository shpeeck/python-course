from django.db import models

class Autors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    @staticmethod
    def create_autor():
        from .views import authors
        for i in authors:
            autor = Autors(first_name=i['first_name'], last_name=i['last_name'], age=i['age'])
            autor.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta():
        verbose_name =  'Autor'
        verbose_name_plural = 'Autors'

class Books(models.Model):
    title = models.CharField(max_length=100)
    released_year = models.PositiveSmallIntegerField()
    description = models.TextField()
    author = models.ForeignKey('Autors', on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def create_books():
        from .views import books
        for i in books:
            book = Books(title=i['title'], released_year=i['released_year'], description=i['description'], author_id=i['author_id'])
            book.save()

    def __str__(self):
        return f"{self.pk} {self.title} {self.released_year} {self.description} {self.author}"

    class Meta():
        verbose_name =  'Book'
        verbose_name_plural = 'Books'

class Comments(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.body)

    class Meta():
        verbose_name =  'Comment'
        verbose_name_plural = 'Comments'