from django.db import models
from django.db.models import F
from django.utils.translation import gettext as _

# Create your models here.
class Shortener(models.Model):
    url = models.URLField(_("url"), max_length=500, help_text=_("help_url"))
    alias = models.SlugField(_("alias"), help_text=_("help_alias"))
    snippet = models.TextField(_("snippet"), blank=True, null=True, help_text=_("help_snippet"))
    count = models.PositiveIntegerField(_("count"), default=0, help_text=_("help_count"))
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    
    @classmethod
    def increment(self):
        return self.objects.update(count=F('count')+1)

    def get_url(self):
        return "{} ...".format(self.url[:50])
    get_url.short_description = _("url")

    def get_snippet(self):
        if self.snippet is '':
            return False
        return True
    get_snippet.short_description = _("snippet")
    get_snippet.boolean = True

    class Meta:
        verbose_name = _("shortener")
        verbose_name_plural = _("shorteners")

    def __str__(self):
        return self.url

class Statistic(models.Model):
    shortener = models.ForeignKey(Shortener, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.shortener

    def get_shortener(self):
        return "{} ...".format(str(self.shortener)[:50])
    get_shortener.short_description = _("shortener")

    class Meta:
        verbose_name = _("statistic")
        verbose_name_plural = _("statistics")

class Location(models.Model):
    locale = models.CharField(_("locale"), max_length=5)
    shortener = models.ForeignKey(Shortener, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.locale

    def get_shortener(self):
        return "{} ...".format(str(self.shortener)[:50])
    get_shortener.short_description = _("shortener")
    
    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

class Source(models.Model):
    reference = models.URLField(_("reference"), max_length=500)
    shortener = models.ForeignKey(Shortener, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.reference

    def get_shortener(self):
        return "{} ...".format(str(self.shortener)[:50])
    get_shortener.short_description = _("shortener")
    
    class Meta:
        verbose_name = _("source")
        verbose_name_plural = _("sources")