from google.cloud import bigquery

# Initialize a BigQuery client
client = bigquery.Client()

# Specify the project ID, dataset ID, and table ID
project_id = "rs-nprd-dlk-ia-dev-aif-d3d9"
dataset_id = "deliver"
table_id = "persona__superscore_financ_ig_ffvv"

# Construct a reference to the table
table_ref = client.dataset(dataset_id, project=project_id).table(table_id)

# Fetch the table
table = client.get_table(table_ref)

# Print the schema of the table
for field in table.schema:
    print(f"{field.name}: {field.field_type}")