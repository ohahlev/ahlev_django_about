from django.db import models

class About(models.Model):
    whatweare = models.TextField(max_length=102400, blank=False, verbose_name='what we are')
    whatwedo = models.TextField(max_length=102400, blank=False, verbose_name='what we do')
    whoweare = models.TextField(max_length=102400, blank=False, verbose_name='who we are')

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        db_table = 'about'

    def __str__(self):
        return "{}".format(self.id)
