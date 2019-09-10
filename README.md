# Backend Coding Challenge

Your job is to build a small data pipeline that simulates the ingestion of a product inventory from a point-of-sale system (POS) into iheartjane.

Specifically the data pipeline should read a list of POS products from `pos/products.json` and attempt to match each POS product against the iheartjane canonical database of products as represented by the sqlite3 file `db/jane.db`. Note that not all POS products exist in the iheartjane database. You have complete autonomy to process POS products however you see fit in order to optimize the lookup operation against the iheartjane database. You also have complete autonomy as to how the lookup operation is implemented.

Lastly the data pipeline should return a csv file that lists all ingested POS products along with the jane product id if the lookup was successful, i.e. `id` column in `products` table. If the lookup was not successful (because the logic needs to be further tuned or the product simply does not exist in the iheartjane database), no product id should be specified.

If you have any questions, feel free to contact your sponsor at Jane. Good luck and have fun!

### To rebuild the iheartjane database

The iheartjane database is already provided under `db/jane.db` so you should not have to rebuild it. However, here are the instructions to do so as a reference.

```
cd db
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
python seed.py
```
