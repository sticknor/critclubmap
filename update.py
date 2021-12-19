import config

if __name__ == "__main__":
    from pyairtable import Table
    import googlemaps
    import json

    gmaps = googlemaps.Client(key=config.GOOGLE_MAPS_API_KEY)
    airtable = Table(
        config.AIRTABLE_API_KEY,
        config.AIRTABLE_BASE_ID,
        config.AIRTABLE_TABLE_NAME,
    )
    airtable_data = airtable.all()

    with config.MAP_DATA_PATH.open() as f:
        map_data = json.load(f)

    for row in airtable_data:
        place = row["fields"].get("Place")
        num_crit_clubbers = row["fields"].get("Amount")

        if place not in map_data:
            location = gmaps.geocode(address=place)
            map_data[place] = {
                "place": place,
                "location": location,
            }

        map_data[place]["num_crit_clubbers"] = num_crit_clubbers

    with config.MAP_DATA_PATH.open(mode="w") as f:
        json.dump(map_data, f)
