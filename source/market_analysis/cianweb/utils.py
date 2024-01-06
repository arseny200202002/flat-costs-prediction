menu = [
    {'title': 'Collect data',   'url_name': 'parser'},
    {'title': 'About',          'url_name': 'home'},
    {'title': 'Visualization',  'url_name': 'visualize'},
    {'title': 'Train/Fit',      'url_name': 'train'},
]

class DataMixin():
    def get_user_context(self, *args, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context