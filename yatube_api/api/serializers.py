from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        if Follow.objects.filter(
            user__username=self.context['request'].user,
            following__username=attrs['following']
        ).exists():
            raise serializers.ValidationError(
                'Подписка на этого автора уже существует')
        return super().validate(attrs)

    class Meta:
        fields = ('user', 'following')
        model = Follow
