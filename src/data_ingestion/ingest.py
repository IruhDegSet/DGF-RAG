from typing import List, Dict 
import pandas as pd
import yaml
import os

from icecat import IceCatCatalog

with open('../config/config.yaml', 'r') as file:
    config: Dict = yaml.safe_load(file)

icecat_auth: List[str, str]= list(config['data_source']['icecat'].values())
data_dir: str= config['storage']['raw_data']

def get_icecat_daily(data_dir: str, auth: List[str, str], xml: str | None= None) -> None:
    
    if "product_xml" in os.listdir(data_dir):
        import shutil
        shutil.rmtree(f'{data_dir}/product_xml', ignore_errors=True)
    

    catalog= IceCatCatalog(data_dir=data_dir, auth=auth, xml= xml)
    
    catalog.add_product_details_parallel(connections=99)
    
