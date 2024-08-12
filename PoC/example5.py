import requests

# Voorbeeld van 
# ~~ Dummy URL: https://www.oddsportal.com/ajax-sport-country-tournament/sport/country/league/

# Deze arrays kunnen manueel onderhouden worden of er worden gebruik gemaakt van een API
request_parameters = {
    "Voetbal": {
        "Belgie": ["Jupiler Pro League", "Eerste klasse B"],
        "Nederland": ["Eredivisie", "Eerste Divisie"],
        "Engeland": ["Premier League", "Championship"],
    },
    "Hockey": {
        "België": ["Belfius Hockey League"],
        "Nederland": ["Hoofdklasse", "Promotieklasse"],
        "Duitsland": ["Bundesliga"],
    },
    "Tennis": {
        "Internationaal": ["ATP Tour", "WTA Tour"],
        "Verenigde Staten": ["US Open Series"],
        "Australie": ["Australian Open"],
    }
}

# Overlopen van alle url parameters
for sport, countries in request_parameters.items():
    for country, leagues in countries.items():
        for league in leagues:
            request_string = f"https://www.oddsportal.com/ajax-sport-country-tournament/{sport}/{country}/{league}/"
            
            r = requests.get(request_string)