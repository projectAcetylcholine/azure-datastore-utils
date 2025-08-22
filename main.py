
import asyncio
from azure_datastore_utils import AsyncSearchClientDao, SearchClientDao

async def search_product_inventory():
    client = AsyncSearchClientDao('product_inventory', auth_strategy='Password')
    document_count = await client.get_document_count()
    print(document_count)
    await client.close()

async def search_net_sales():
    client = AsyncSearchClientDao('net_sales', auth_strategy='Password')
    document_count = await client.get_document_count()
    print(document_count)
    await client.close()

async def query_documents():
    client = SearchClientDao('product_inventory', auth_strategy='Password')
    results = client.query_index("*", query_filter="department eq 'appliance'")
    print(results)

async def query_collection():
    client = SearchClientDao('product_inventory', auth_strategy='Password')
    results = client.query_index("*", query_filter="department eq 'appliance'")
    print(results)

async def main():
    print("Running tests ...")
    await query_documents()

if __name__ == '__main__':
    asyncio.run(main())
