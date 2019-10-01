# Backend Coding Challenge

Your job is to build a small data pipeline that simulates the ingestion of a product
inventory from a point-of-sale system (POS), often times unclean and unstructured,
into iheartjane, where a structured and standardized list of products is maintained.

Specifically the data pipeline should read a list of POS products from
`pos/products.json` and attempt to match each POS product against the iheartjane
canonical database of products as represented by the sqlite3 file `db/jane.db`. Note
that not all POS products exist in the iheartjane database: some POS products exist
in the iheartjane database, others don't.

You have complete autonomy to process POS products however you see fit in order to
optimize the lookup operation to match POS products against iheartjane products. You
also have complete autonomy as to how the lookup operation is implemented.

Lastly the data pipeline should return a csv file that lists all ingested POS
products along with the jane product id if the lookup/match was successful, i.e.
`id` column in `products` table. If the lookup was not successful (because the logic
needs to be further tuned or the POS product simply does not exist in the iheartjane
database), no product id should be specified.

### Notes

- The POS product ids (`productId` key in `pos/products.json`) are POS specific and
thus have no relationship with the `id` column in `db/jane.db`. Do not try to match
POS products with iheartjane products using these fields. Instead you'll need to
leverage other POS fields such as `category` and `productName` to attempt to find a
strong match in the iheartjane database. Remember also that some POS products do
not have a match in the iheartjane database.
- We're looking for a modular and extensible architecture or pattern that can
easily integrate other POS systems and provide a foundation for a scalable
cloud-based solution. This as opposed to an ad-hoc script that does the job but
only that specific job, i.e. ingest the provided `pos/products.json` file. Therefore
pay particular attention to the design, code structure, techniques and tools you
use and don't spend too much time fine tuning low level code to match as many
products as possible.
- We use python and we'd love to see you use it too (only if you've use it in the
past).
- We do not expect you to use other major pieces of software such as pub/sub,
streaming or storage systems. Libraries that can easily be installed with a package
manager such as pip (for Python) are fine to use.
- Your solution should be able to be run from the command line. Please include
appropriate scripts and instructions for running your application and your tests,
if any.

If you have any questions, feel free to contact your sponsor at Jane. Good luck and
have fun!

### To rebuild the iheartjane database

The iheartjane database is already provided under `db/jane.db` so you should not
have to rebuild it. However, for reference, here are the instructions to do so.

```
cd db
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
python seed.py
```
