"""London Heathrow Airport (LHR) destinations — May 2026."""

DESTINATIONS = {
    "LHR": {
        "name": "London Heathrow",
        "routes": {
            # UK & Ireland
            "ABZ": "Aberdeen",
            "BHD": "Belfast City",
            "DND": "Dundee",
            "DUB": "Dublin",
            "EDI": "Edinburgh",
            "GCI": "Guernsey",
            "GIB": "Gibraltar",
            "GLA": "Glasgow",
            "INV": "Inverness",
            "IOM": "Isle of Man",
            "JER": "Jersey",
            "KOI": "Kirkwall",
            "LDY": "Derry",
            "LSI": "Sumburgh",
            "MAN": "Manchester",
            "NCL": "Newcastle",
            "NOC": "Knock",
            "ORK": "Cork",
            "SNN": "Shannon",
            # Spain (Mainland)
            "AGP": "Malaga",
            "BCN": "Barcelona",
            "BIO": "Bilbao",
            "LCG": "A Coruna",
            "MAD": "Madrid",
            "SCQ": "Santiago de Compostela",
            "SVQ": "Seville",
            "VLC": "Valencia",
            # Balearic Islands
            "IBZ": "Ibiza",
            "PMI": "Palma de Majorca",
            # Italy
            "BDS": "Brindisi",
            "BLQ": "Bologna",
            "FCO": "Rome Fiumicino",
            "FLR": "Florence",
            "LIN": "Milan Linate",
            "MXP": "Milan Malpensa",
            "NAP": "Naples",
            "OLB": "Olbia",
            "PEG": "Perugia",
            "PMO": "Palermo",
            "PSA": "Pisa",
            "RMI": "Rimini",
            "VCE": "Venice Marco Polo",
            # France
            "CDG": "Paris Charles de Gaulle",
            "FSC": "Figari (Corsica)",
            "LYS": "Lyon",
            "MRS": "Marseille",
            "NCE": "Nice",
            "ORY": "Paris Orly",
            "TLS": "Toulouse",
            # Germany
            "BER": "Berlin",
            "DUS": "Dusseldorf",
            "FRA": "Frankfurt",
            "HAJ": "Hanover",
            "HAM": "Hamburg",
            "MUC": "Munich",
            "NUE": "Nuremberg",
            "STR": "Stuttgart",
            # Greece
            "ATH": "Athens",
            "CFU": "Corfu",
            "CHQ": "Chania",
            "EFL": "Kefalonia",
            "HER": "Heraklion (Crete)",
            "JMK": "Mykonos",
            "JTR": "Santorini",
            "PVK": "Preveza",
            "RHO": "Rhodes",
            "SKG": "Thessaloniki",
            "ZTH": "Zakynthos (Zante)",
            # Portugal & Azores
            "FAO": "Faro",
            "LIS": "Lisbon",
            "OPO": "Porto",
            "PDL": "Ponta Delgada (Azores)",
            # Turkey
            "DLM": "Dalaman",
            "IST": "Istanbul",
            # Poland
            "KRK": "Krakow",
            "WAW": "Warsaw",
            # Romania
            "OTP": "Bucharest",
            # Austria & Switzerland
            "BSL": "Basel",
            "GVA": "Geneva",
            "INN": "Innsbruck",
            "SZG": "Salzburg",
            "VIE": "Vienna",
            "ZRH": "Zurich",
            # Eastern Europe & Balkans
            "BEG": "Belgrade",
            "BUD": "Budapest",
            "DBV": "Dubrovnik",
            "LJU": "Ljubljana",
            "PRG": "Prague",
            "SOF": "Sofia",
            "SPU": "Split",
            "TIA": "Tirana",
            "TIV": "Tivat",
            "ZAG": "Zagreb",
            # Scandinavia & Nordics
            "ARN": "Stockholm",
            "BLL": "Billund",
            "CPH": "Copenhagen",
            "GOT": "Gothenburg",
            "HEL": "Helsinki",
            "KEF": "Reykjavik",
            "OSL": "Oslo",
            "TOS": "Tromso",
            # Benelux & Luxembourg
            "AMS": "Amsterdam",
            "BRU": "Brussels",
            "LUX": "Luxembourg",
            # Cyprus
            "LCA": "Larnaca",
            "PFO": "Paphos",
            # North Africa
            "ALG": "Algiers",
            "CMN": "Casablanca",
            "RAK": "Marrakech",
            "TUN": "Tunis",
            # Malta
            "MLA": "Malta",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
