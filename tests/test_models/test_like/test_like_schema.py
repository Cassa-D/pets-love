from app.models.like_model import Like, LikeSchema


def test_schema_serialize_like():
    new_like = {
        'dog_id_give': 1,
        'dog_id_receive': 2,
        'dislike': False
    }

    like = Like(**new_like)

    like_schema = LikeSchema().dump(like)

    for key in new_like.keys():
        if key != 'dislike':
            assert like_schema[key] == new_like[key]
