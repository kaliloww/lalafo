from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    discription = models.TextField(
        max_length=500,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотографии"
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name="дата создания"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"