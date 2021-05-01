# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapydjangotestPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('championship'):  # if scraped data has a championship
            item.save()  # save it to database
            return item
        else:
            raise DropItem(f"Missing price in {item}")
