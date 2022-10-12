# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from deutschland.bundestag.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    BLUEPRINT_SERVLET_CONTENT_ARTICLE_ID_AS_APP_V2NEWSARTICLE_XML = (
        "/blueprint/servlet/content/{ARTICLE_ID}/asAppV2NewsarticleXml"
    )
    STATIC_APPDATA_PLENUM_V2_SPEAKER_XML = "/static/appdata/plenum/v2/speaker.xml"
    STATIC_APPDATA_PLENUM_V2_CONFERENCES_XML = (
        "/static/appdata/plenum/v2/conferences.xml"
    )
    XML_V2_AUSSCHUESSE_INDEX_XML = "/xml/v2/ausschuesse/index.xml"
    XML_V2_AUSSCHUESSE_AUSSCHUSS_ID_XML = "/xml/v2/ausschuesse/{AUSSCHUSS_ID}.xml"
    XML_V2_MDB_INDEX_XML = "/xml/v2/mdb/index.xml"
    XML_V2_MDB_BIOGRAFIEN_MDB_ID_XML = "/xml/v2/mdb/biografien/{MDB_ID}.xml"
    IPTV_PLAYER_MACROS__X_S144277506_BTTV_MOBILE_FEED_VOD_XML = (
        "/iptv/player/macros/_x_s-144277506/bttv/mobile/feed_vod.xml"
    )
