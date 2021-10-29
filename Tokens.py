import sys

# Subqueries by religion and language
CHRISTIANITY_EN = [
    '"christianity"',
    '"christians"',
    '("bible" OR "old testament" OR "new testament")',
    '("catholicity" OR "catholicism" OR "catholic church" OR "protestantism" OR "catholic" OR "catholics" OR "protestant" OR "protestants" OR "orthodox" OR "orthodoxes")',  # "eastern orthodox church", "orthodox catholic church"
]

ISLAM_EN = [
    '"islam"',
    '("muslim" OR "muslims" OR "moslem" OR "moslems" OR "islamic" OR "islamics")',
    '("quran" OR "qur\'an" OR "koran" OR "sunnah")',  # "hadith", "athar"
    '("sunni" OR "sunnism" OR "shia" OR "shi\'a" OR "shiism" OR "shi\'ism" OR "sunnis" OR "sunnite" OR "sunnites" OR "shias" OR "shi\'as" OR "shiite" OR "shi\'ite" OR "shiites" OR "shi\'ites")',
]

JUDAISM_EN = [
    '"judaism"',
    '("jew" OR "jews" OR "jewish" OR "jewishes" OR "jewry" OR "jewries")',
    '("tanach" OR "hebrew bible" OR "torah")',  # "midrash", "talmud"
    '("rabbanite" OR "rabbinic" OR "rabbinism" OR "rabbinicism" OR "rabbanites" OR "rabbi" OR "rabbis" OR "rabbinist" OR "rabbinists" OR "rabbinicist" OR "rabbinicists")',  # "karaite", "qaraite", "karaism", "qaraism", "karaites", "qaraites"
]

CHRISTIANITY_IT = [
    '"cristianesimo"',
    '"cristiani"',
    '("bibbia" OR "antico testamento" OR "nuovo testamento")',  # "vecchio testamento", "primo testamento", "antica alleanza", "nuova alleanza"
    '("cattolicità" OR "cattolicesimo" OR "chiesa cattolica" OR "protestantesimo" OR "cattolico" OR "cattolica" OR "cattolici" OR "cattoliche" OR "protestante" OR "protestanti" OR "ortodosso" OR "ortodossa" OR "ortodossi" OR "ortodosse")',  # "chiesa ortodossa orientale", "chiesa cristiana orientale", "chiesa cattolica ortodossa", "chiesa ortodossa d\'oriente", "chiesa cristiana d\'oriente"
]
ISLAM_IT = [
    '"islam"',
    '("musulmano" OR "musulmana" OR "mussulmano" OR "mussulmana" OR "musulmani" OR "musulmane" OR "mussulmani" OR "mussulmane" OR "islamico" OR "islamica" OR "islamici" OR "islamiche")',  # "maomettano", "maomettana", "maomettani", "maomettane"
    '("corano" OR "quran" OR "qur\'an" OR "koran" OR "sunna" OR "sunnah")',  # "hadith", "athar"
    '("sunnismo" OR "sciismo" OR "sunnita" OR "sunniti" OR "sciita" OR "sciiti")',
]
JUDAISM_IT = [
    '("ebraismo" OR "giudaismo")',
    '("ebreo" OR "ebrea" OR "ebrei" OR "ebree" OR "ebraico" OR "ebraica" OR "ebraici" OR "ebraiche")',
    '("tanakh" OR "tenakh" OR "bibbia ebraica" OR "torah" OR "torà")',  # "midrash", "talmud"
    '("rabbinico" OR "rabbinismo" OR "rabbino" OR "rabbina" OR "rabbini" OR "rabbine" OR "rabbinista" OR "rabbinisti" OR "rabbiniste")',  # "caraita", "karaita", "karaismo", "karaitismo", "caraismo", "caraitismo", "caraiti", "karaiti"
]

CHRISTIANITY_EN_ALL = " OR ".join(subquery for subquery in CHRISTIANITY_EN)
ISLAM_EN_ALL = " OR ".join(subquery for subquery in ISLAM_EN)
JUDAISM_EN_ALL = " OR ".join(subquery for subquery in JUDAISM_EN)
CHRISTIANITY_IT_ALL = " OR ".join(subquery for subquery in CHRISTIANITY_IT)
ISLAM_IT_ALL = " OR ".join(subquery for subquery in ISLAM_IT)
JUDAISM_IT_ALL = " OR ".join(subquery for subquery in JUDAISM_IT)
RELIGION_EN_ALL = " OR ".join(
    query for query in [CHRISTIANITY_EN_ALL, ISLAM_EN_ALL, JUDAISM_EN_ALL]
)
RELIGION_IT_ALL = " OR ".join(
    query for query in [CHRISTIANITY_IT_ALL, ISLAM_IT_ALL, JUDAISM_IT_ALL]
)

# Additional constraints
EXCL_RETWEETS = "-is:retweet"

class Topics:
    def make_query(self, lang_code, topic, category):
        # Create the language filter to append to the query
        if lang_code in ["en", "it"]:
            lang_filter = "lang:" + lang_code
        else:
            sys.exit("Language {} is not supported. Exiting.".format(lang_code))

        # Build the query string: case "christianity"
        if topic == "christianity":
            if lang_code == "en":
                if category == 0:
                    query = "({}) {} {}".format(
                        CHRISTIANITY_EN_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        CHRISTIANITY_EN[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            elif lang_code == "it":
                if category == 0:
                    query = "({}) {} {}".format(
                        CHRISTIANITY_IT_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        CHRISTIANITY_IT[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            else:
                sys.exit("Language {} is not supported. Exiting.".format(lang_code))

        # Build the query string: case "islam"
        elif topic == "islam":
            if lang_code == "en":
                if category == 0:
                    query = "({}) {} {}".format(
                        ISLAM_EN_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        ISLAM_EN[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            elif lang_code == "it":
                if category == 0:
                    query = "({}) {} {}".format(
                        ISLAM_IT_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        ISLAM_IT[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            else:
                sys.exit("Language {} is not supported. Exiting.".format(lang_code))

        # Build the query string: case "judaism"
        elif topic == "judaism":
            if lang_code == "en":
                if category == 0:
                    query = "({}) {} {}".format(
                        JUDAISM_EN_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        JUDAISM_EN[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            elif lang_code == "it":
                if category == 0:
                    query = "({}) {} {}".format(
                        JUDAISM_IT_ALL, lang_filter, EXCL_RETWEETS
                    )
                elif (category >= 1) and (category <= 4):
                    query = "({}) {} {}".format(
                        JUDAISM_IT[category], lang_filter, EXCL_RETWEETS
                    )
                else:
                    sys.exit("Category {} is not supported. Exiting.".format(category))
            else:
                sys.exit("Language {} is not supported. Exiting.".format(lang_code))

        # Build the query string: case "all" (i.e., "christianity" + "islam" + "judaism")
        elif topic == "all":
            # Categories are useless here
            if lang_code == "en":
                query = "({}) {} {}".format(RELIGION_EN_ALL, lang_filter, EXCL_RETWEETS)
            elif lang_code == "it":
                query = "({}) {} {}".format(RELIGION_IT_ALL, lang_filter, EXCL_RETWEETS)
            else:
                sys.exit("Language {} is not supported. Exiting.".format(lang_code))

        # Build the query string: case unsupported
        else:
            sys.exit("Topic {} is not supported. Exiting.".format(topic))

        return query
