from rest_framework import renderers

class Renderer(renderers.BaseRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        return data

class Image_PNG(Renderer):
    media_type = 'image/png'
    format = 'png'
