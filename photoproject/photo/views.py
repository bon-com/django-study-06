from django.views.generic import TemplateView


class IndexView(TemplateView):
    """トップ画面表示"""

    template_name = "index.html"
