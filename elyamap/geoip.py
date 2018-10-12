def get_peers():
    return ['139.59.149.46']


def get_loc_by_ip(ip_list):
    # http://www.geoplugin.net/json.gp?ip=xx.xx.xx.xx
    # http://www.geoplugin.net/json.gp?ip=139.59.149.46

    # {
    #     "geoplugin_request": "139.59.149.46",
    #     "geoplugin_status": 206,
    #     "geoplugin_delay": "1ms",
    #     "geoplugin_credit": "Some of the returned data includes GeoLite data created by MaxMind, available from <a href='http:\/\/www.maxmind.com'>http:\/\/www.maxmind.com<\/a>.",
    #     "geoplugin_city": "",
    #     "geoplugin_region": "",
    #     "geoplugin_regionCode": "",
    #     "geoplugin_regionName": "",
    #     "geoplugin_areaCode": "",
    #     "geoplugin_dmaCode": "",
    #     "geoplugin_countryCode": "SG",
    #     "geoplugin_countryName": "Singapore",
    #     "geoplugin_inEU": 0,
    #     "geoplugin_euVATrate": false,
    #     "geoplugin_continentCode": "AS",
    #     "geoplugin_continentName": "Asia",
    #     "geoplugin_latitude": "1.3667",
    #     "geoplugin_longitude": "103.8",
    #     "geoplugin_locationAccuracyRadius": "50",
    #     "geoplugin_timezone": "Asia\/Singapore",
    #     "geoplugin_currencyCode": "SGD",
    #     "geoplugin_currencySymbol": "$",
    #     "geoplugin_currencySymbol_UTF8": "$",
    #     "geoplugin_currencyConverter": 1.3829
    # }
    return "1.3667", "103.8"
