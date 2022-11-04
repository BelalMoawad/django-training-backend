from django.db import models
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Album(models.Model) :
    album_name = models.CharField(max_length = 30, default="New Album")
    creation_date = models.DateField(auto_now_add=True)
    releasing_date = models.DateField()
    album_cost = models.FloatField(blank = True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    approved = models.BooleanField(default=False, help_text = "Approve the album if its name is not explicit")

    def __str__(self) :
        return self.album_name

class Song(models.Model) :
    song_name = models.CharField(max_length = 30, default = "New Album")
    img = models.ImageField(upload_to = 'images/')
    img_thumbnail = ImageSpecField(source='img',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self) : 
        return self.song_name