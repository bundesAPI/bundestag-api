# Bundestag API

Bundestag: Live Informationen


## asAppV2NewsarticleXml

**URL:** https://www.bundestag.de/blueprint/servlet/content/{ARTICLE_ID}/asAppV2NewsarticleXml

 Artikel Details



## speaker.xml

**URL:** https://www.bundestag.de/static/appdata/plenum/v2/speaker.xml

Aktuelle Sprecher*in



## conferences.xml

**URL:** https://www.bundestag.de/static/appdata/plenum/v2/conferences.xml

Sitzungstag übersicht



## index.xml

**URL:** https://www.bundestag.de/xml/v2/ausschuesse/index.xml

Übersicht über die Ausschüsse



## {AUSSCHUSS_ID}.xml

**URL:** https://www.bundestag.dexml/v2/ausschuesse/{AUSSCHUSS_ID}.xml

Übersicht über die Ausschüsse



## index.xml

**URL:** https://www.bundestag.de/xml/v2/mdb/index.xml

Übersicht über alle MDBS



## {MDB_ID}.xml

**URL:** https://www.bundestag.de/xml/v2/mdb/biografien/{MDB_ID}.xml

Abruf Details eines MDBS



## feed_vod.xml

**URL:** http://webtv.bundestag.de/iptv/player/macros/_x_s-144277506/bttv/mobile/feed_vod.xml

Abruf eines Videos


## Beispiel

```bash
result=$(curl -m 60 https://www.bundestag.de/xml/v2/ausschuesse/index.xml)
```
