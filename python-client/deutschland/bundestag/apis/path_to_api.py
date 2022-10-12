import typing_extensions
from deutschland.bundestag.apis.paths.blueprint_servlet_content_article_id_as_app_v2_newsarticle_xml import (
    BlueprintServletContentARTICLEIDAsAppV2NewsarticleXml,
)
from deutschland.bundestag.apis.paths.iptv_player_macros__x_s_144277506_bttv_mobile_feed_vod_xml import (
    IptvPlayerMacrosXS144277506BttvMobileFeedVodXml,
)
from deutschland.bundestag.apis.paths.static_appdata_plenum_v2_conferences_xml import (
    StaticAppdataPlenumV2ConferencesXml,
)
from deutschland.bundestag.apis.paths.static_appdata_plenum_v2_speaker_xml import (
    StaticAppdataPlenumV2SpeakerXml,
)
from deutschland.bundestag.apis.paths.xml_v2_ausschuesse_ausschuss_id_xml import (
    XmlV2AusschuesseAUSSCHUSSIDXml,
)
from deutschland.bundestag.apis.paths.xml_v2_ausschuesse_index_xml import (
    XmlV2AusschuesseIndexXml,
)
from deutschland.bundestag.apis.paths.xml_v2_mdb_biografien_mdb_id_xml import (
    XmlV2MdbBiografienMDBIDXml,
)
from deutschland.bundestag.apis.paths.xml_v2_mdb_index_xml import XmlV2MdbIndexXml
from deutschland.bundestag.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.BLUEPRINT_SERVLET_CONTENT_ARTICLE_ID_AS_APP_V2NEWSARTICLE_XML: BlueprintServletContentARTICLEIDAsAppV2NewsarticleXml,
        PathValues.STATIC_APPDATA_PLENUM_V2_SPEAKER_XML: StaticAppdataPlenumV2SpeakerXml,
        PathValues.STATIC_APPDATA_PLENUM_V2_CONFERENCES_XML: StaticAppdataPlenumV2ConferencesXml,
        PathValues.XML_V2_AUSSCHUESSE_INDEX_XML: XmlV2AusschuesseIndexXml,
        PathValues.XML_V2_AUSSCHUESSE_AUSSCHUSS_ID_XML: XmlV2AusschuesseAUSSCHUSSIDXml,
        PathValues.XML_V2_MDB_INDEX_XML: XmlV2MdbIndexXml,
        PathValues.XML_V2_MDB_BIOGRAFIEN_MDB_ID_XML: XmlV2MdbBiografienMDBIDXml,
        PathValues.IPTV_PLAYER_MACROS__X_S144277506_BTTV_MOBILE_FEED_VOD_XML: IptvPlayerMacrosXS144277506BttvMobileFeedVodXml,
    },
)

path_to_api = PathToApi(
    {
        PathValues.BLUEPRINT_SERVLET_CONTENT_ARTICLE_ID_AS_APP_V2NEWSARTICLE_XML: BlueprintServletContentARTICLEIDAsAppV2NewsarticleXml,
        PathValues.STATIC_APPDATA_PLENUM_V2_SPEAKER_XML: StaticAppdataPlenumV2SpeakerXml,
        PathValues.STATIC_APPDATA_PLENUM_V2_CONFERENCES_XML: StaticAppdataPlenumV2ConferencesXml,
        PathValues.XML_V2_AUSSCHUESSE_INDEX_XML: XmlV2AusschuesseIndexXml,
        PathValues.XML_V2_AUSSCHUESSE_AUSSCHUSS_ID_XML: XmlV2AusschuesseAUSSCHUSSIDXml,
        PathValues.XML_V2_MDB_INDEX_XML: XmlV2MdbIndexXml,
        PathValues.XML_V2_MDB_BIOGRAFIEN_MDB_ID_XML: XmlV2MdbBiografienMDBIDXml,
        PathValues.IPTV_PLAYER_MACROS__X_S144277506_BTTV_MOBILE_FEED_VOD_XML: IptvPlayerMacrosXS144277506BttvMobileFeedVodXml,
    }
)
