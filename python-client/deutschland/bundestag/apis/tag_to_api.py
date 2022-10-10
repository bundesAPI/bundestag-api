import typing_extensions
from deutschland.bundestag.apis.tags import TagValues
from deutschland.bundestag.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    "TagToApi",
    {
        TagValues.DEFAULT: DefaultApi,
    },
)

tag_to_api = TagToApi(
    {
        TagValues.DEFAULT: DefaultApi,
    }
)
