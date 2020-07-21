from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 439772041},
        'update': {'titulo': 'Atualização do Sistema Operacional', 'vimeo_id': 440417149}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
