from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard


class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            _('Actividades'),
            models=('api.CategoryItem', 'api.ActivityCategory', 'api.Actividad', 'api.Salon'),
            column=3,
            order=0,
            layout='inline'
        ))
        self.children.append(modules.ModelList(
            _('Publicaciones'),
            models=('api.Boletin', 'api.Guia', 'api.Podcast'),
            column=3,
            order=0,
            layout='stacked'
        ))
        self.children.append(modules.ModelList(
            _('Normatividad'),
            models=('api.Norma', 'api.Reglamento', 'api.Ley'),
            column=3,
            order=0,
            layout='inline'
        ))
