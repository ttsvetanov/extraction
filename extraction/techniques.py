"This file contains techniques for extracting data from HTML pages."
import BeautifulSoup


class Technique(object):
    def __init__(self, extractor=None, *args, **kwargs):
        """
        Capture the extractor this technique is running within,
        if any.
        """
        self.extractor = extractor
        super(Technique, self).__init__(*args, **kwargs)


    def extract(html):
        "Extract data from a string representing an HTML document."
        return {'titles': [],
                'descriptions': [],
                'images': [],
                'urls': [],
                }


class FacebookOpengraphTags(Technique):
    """
    Extract info from html Facebook Opengraph meta tags.

    Facebook tags are ubiquitous on high quality sites, and tend to be higher quality
    than more manual discover techniques. Especially for picking high quality images,
    this is probably your best bet.

    Some example tags from `the Facebook opengraph docs <https://developers.facebook.com/docs/opengraphprotocol/>`::

        <meta property="og:title" content="The Rock"/>
        <meta property="og:type" content="movie"/>
        <meta property="og:url" content="http://www.imdb.com/title/tt0117500/"/>
        <meta property="og:image" content="http://ia.media-imdb.com/rock.jpg"/>
        <meta property="og:site_name" content="IMDb"/>
        <meta property="fb:admins" content="USER_ID"/>
        <meta property="og:description"
            content="A group of U.S. Marines, under command of
                     a renegade general, take over Alcatraz and
                     threaten San Francisco Bay with biological
                     weapons."/>

    There are a bunch of other opengraph tags, but they don't seem
    useful to extraction's intent at this point.
    """
    def extract(self, html):
        "Extract data from Facebook Opengraph tags."

        return {'titles': [],
                'descriptions': [],
                'images': [],
                'urls': [],
                }
