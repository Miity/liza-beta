from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail, ResizeToFill,ResizeToFit


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True, default='default', unique=True)

    def __str__(self):
        return self.title


def image_dir(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'post_gallery/{0}/{1}'.format(instance.slug, filename)


class Post(models.Model):
    post_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_at = models.DateTimeField('Дата обновленния', auto_now=True)
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 null=True,
                                 blank=True,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 default=0,
                                 )
    image = models.ImageField("Главное фото", null=True, blank=True, upload_to=image_dir)
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(width=800, height=None)],
                                 format='JPEG',
                                 options={'quality': 80})
    title = models.CharField("Название", max_length=200)
    content = RichTextUploadingField("Контент", null=True, blank=True)
    excert = models.TextField("Краткое описание", max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=150, db_index=True, null=True, blank=True, unique=True)
    status = models.BooleanField("Опубликовать?", default=True)
    comment_status = models.BooleanField("Можно комментировать?", default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug,), )

    class Meta:
        ordering = ["-post_date", "title"]

def gallery_dir(instance, filename):
    return 'post_gallery/{0}/{1}'.format(instance.post.slug, filename)


class Post_Gallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=gallery_dir)
    image_medium = ImageSpecField(source='image',
                                 processors=[Thumbnail(700),],
                                 format='JPEG',
                                 options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(150)],
                                 format='JPEG',
                                 options={'quality': 30})

    def __str__(self):
        return self.post.title
