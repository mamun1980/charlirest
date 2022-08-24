from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    ('active', 'Active'),
    ('archived', 'Archived'),
    ('deleted', 'Deleted')
)

# Create your models here.
class TimeStamp(models.Model):
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStamp):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)

    # profile_image = models.FileField()
    status = models.CharField(max_length=50, default="active", choices=STATUS)

    def __str__(self):
        return self.full_name

class AuthorUpload(models.Model):
    filename = models.FileField(upload_to='public/media')


class Department(TimeStamp):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    # images = models.ImageField()
    status = models.CharField(max_length=50, default="active", choices=STATUS)

    def __str__(self):
        return str(self.title)


class Category(TimeStamp):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)

    # images = models.ImageField()
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=50, default="active", choices=STATUS)

    def __str__(self):
        return str(self.name)



class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField()
    # liked_by = models.ManyToManyField(to=User)

    us_gross = models.IntegerField(default=0)
    worldwide_gross = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


'''


class SubCategory(TimeStamp):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    # images = models.ImageField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    status = models.CharField(max_length=50, default="active", choices=STATUS)

    def __str__(self):
        return str(self.name)



class Post(TimeStamp):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500, null=True, blank=True)
    # tags = models.ManyToManyField(Tags, related_name='post_tags')

    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=50, default="active", choices=STATUS)


    def __str__(self):
        return self.title

'''
