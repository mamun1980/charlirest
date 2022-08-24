from django.db import models


STATUS = (
    ('active', 'Active'),
    ('archived', 'Archived'),
    ('deleted', 'Deleted')
)

DIMENSION_UNIT = (("cm", "Centemter"), ("m", "Meter"))

WEIGHT_UNIT = (("kg", "Kilogram"), ("g", "Gram"), ("ml", "ML"), ("lb", "LB"), ("l", "L"))

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=20, default="active", choices=STATUS)

    class Meta:
        abstract = True



class Brands(TimeStamp):
    # business_id = models.IntegerField(db_column='id', primary_key=True)
    brand_name = models.CharField(db_column='brand_name', max_length=100, null=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    slug = models.CharField(db_column='slug', max_length=100, null=True, blank=True)
    # images = models.ImageField()

    status = models.CharField(max_length=50, default="active", choices=STATUS)


    class Meta:
        managed = True
        db_table = 'brands'

    def __str__(self):
        return str(self.brand_name)


class Departments(TimeStamp):
    title = models.CharField(db_column='title', max_length=100, null=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    slug = models.CharField(db_column='slug', max_length=100, null=True, blank=True)
    # images = models.ImageField()
    status = models.CharField(db_column='status', max_length=50, default="Active", choices=STATUS)


    class Meta:
        managed = True
        db_table = 'departments'

    def __str__(self):
        return str(self.title)



class Categories(TimeStamp):
    title = models.CharField(db_column='title', max_length=100, null=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    slug = models.CharField(db_column='slug', max_length=100, null=True, blank=True)
    # images = models.ImageField()
    department = models.ForeignKey(Departments, db_column='department_id', null=True, blank=True, on_delete=models.SET_NULL)

    status = models.CharField(db_column='status', max_length=50, default="Active", choices=STATUS)

    class Meta:
        managed = True
        db_table = 'categories'

    def __str__(self):
        return str(self.title)


class SubCategories(TimeStamp):
    title = models.CharField(db_column='title', max_length=100, null=True, blank=True)
    description = models.TextField(db_column='description', null=True, blank=True)
    slug = models.CharField(db_column='slug', max_length=100, null=True, blank=True)
    # images = models.ImageField()
    category = models.ForeignKey(Categories, db_column='category_id', null=True, blank=True, on_delete=models.CASCADE)

    status = models.CharField(db_column='status', max_length=50, default="active", choices=STATUS)

    class Meta:
        managed = True
        db_table = 'sub_categories'

    def __str__(self):
        return str(self.title)


class Products(models.Model):
    # business_id = models.IntegerField(db_column='id', primary_key=True)
    sku = models.CharField(db_column='sku', max_length=50, null=True, blank=True, unique=True)
    barcode = models.CharField(db_column='barcode', max_length=100, null=True, blank=True)
    name = models.CharField(db_column='name', max_length=100, null=True, blank=True)
    title = models.CharField(db_column='title', max_length=50, null=True, blank=True)
    description = models.TextField(db_column='description', max_length=500, null=True, blank=True)


    weight = models.DecimalField(db_column='weight', max_digits=20, decimal_places=5, default=0.0)
    height = models.DecimalField(db_column='height', max_digits=20, decimal_places=5, default=0.0)
    width = models.DecimalField(db_column='width', max_digits=20, decimal_places=5, default=0.0)
    length = models.DecimalField(db_column='length', max_digits=20, decimal_places=5, default=0.0)

    # product_type = models.CharField(db_column='type', max_length=200, null=True, blank=True, choices=PRODUCT_TYPE)
    # pack_type = models.CharField(db_column='pack_type', max_length=20, choices=PACK_TYPE)
    # product_status = models.CharField(db_column='product_status', max_length=20, choices=PRODUCT_STATUS, default="unapproved")

    # slug = models.CharField(db_column='slug', max_length=100, null=True, blank=True)
    # quantity_in_pack = models.PositiveSmallIntegerField(db_column='quantity_in_pack', null=True, blank=True)

    # created_by_user = models.ForeignKey(Users, db_column='created_by_user_id', on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brands, db_column='brand_id', null=True, blank=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, db_column='department_id', null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, db_column='category_id', null=True, blank=True, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategories, db_column='sub_category_id', null=True, blank=True, on_delete=models.CASCADE)

    # images = models.ImageField()
    status = models.CharField(db_column='status', max_length=50, default="Active", choices=STATUS)



    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return str(self.name)
