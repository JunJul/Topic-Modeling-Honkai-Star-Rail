import os
import serpapi
import pandas as pd
from key import SERPAPI_KEY

client = serpapi.Client(api_key=SERPAPI_KEY)

results = client.search(
        engine="google_play_product",
        product_id="com.HoYoverse.hkrpgoversea",
        store="apps",
        all_reviews=True,
        num=199
    )

data = results["reviews"]
hk_star_rail_df = pd.DataFrame(data)

count = 1

while 'serpapi_pagination' in results and (count <= 99):
    count += 1
    results = client.search(
        engine="google_play_product",
        product_id="com.HoYoverse.hkrpgoversea",
        store="apps",
        all_reviews=True,
        num=199,
        next_page_token=results["serpapi_pagination"]["next_page_token"]
    )

    data = results["reviews"]
    new_df = pd.DataFrame(data)
    hk_star_rail_df = pd.concat([hk_star_rail_df, new_df])

    print("Total Reveiws: {}".format(len(results["reviews"])))

print("done")

hk_star_rail_df.to_csv("Honkai-Star_Rail.csv", index=False)

