from haystack import indexes
#引入你项目下的model（也就是你要将其作为检索关键词的models）
from games.models import Games

# model名 + Index作为类名
class GamesIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    # 对歌名、歌手、歌词进行搜索
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    zhuxi = indexes.CharField(model_attr='zhuxi')

    def get_model(self):
        return Games

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
