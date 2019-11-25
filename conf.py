import os, time
import logging
from http.client import HTTPConnection

os.environ['TZ'] = 'US/Pacific'

DEPLOYMENT_MODE_DEV = "development"
DEPLOYMENT_MODE_BETA = "beta"
DEPLOYMENT_MODE_PROD = "production"
DEPLOYMENT_MODE = os.environ.get('DEPLOYMENT_MODE', DEPLOYMENT_MODE_DEV)

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = ROOT_DIR

def full_path(filename):
    """ Assuming relative path always starts from the project root dir. """
    if not filename: return None
    if filename.startswith('/') or filename.startswith('~'):
        return os.path.realpath(filename)
    else:
        return os.path.join(ROOT_DIR, filename)

HTTPConnection.debuglevel = 0
LOGGING_DIR = os.path.join(ROOT_DIR, 'log')
LOGGING_LEVEL = logging.DEBUG if DEPLOYMENT_MODE == DEPLOYMENT_MODE_DEV else logging.INFO
logging.basicConfig(
    filename=os.path.join(LOGGING_DIR, 'default.log'), 
    format='%(asctime)s %(message)s', 
    datefmt='[%m/%d/%Y %I:%M:%S %p]',
    level=LOGGING_LEVEL,
)

DATA_DIR = os.path.join(ROOT_DIR, 'data')

DB_DBNAME = os.environ['RASDB_DBNAME']
DB_USER = os.environ['RASDB_USER']
DB_PASSWORD = os.environ['RASDB_PASSWORD']
DB_ECHO = False
if os.environ.get('RASDB_ADDRESS', None):
    DB_HOST = os.environ['RASDB_ADDRESS'].split(':')[0]
    DB_PORT = int(os.environ['RASDB_ADDRESS'].split(':')[1])
else:
    DB_HOST = os.environ['RASDB_HOST']
    DB_PORT = int(os.environ['RASDB_PORT'])

LOCATION_SCORECARD_HOMEPAGE = "https://location-scorecard.weworkers.io/"

# Walkscore.com configuration
WALKSCORE_APIKEY = '4005199d75c9a53504d14b5fdbc4459b'
WALKSCORE_WALK_SCORE_URL = 'http://api.walkscore.com/score'
WALKSCORE_TRANSIT_SCORE_URL = 'http://transit.walkscore.com/transit/score/'

# CARTO KEY
CARTO_API_KEY = "27afd263c93cb3800e06691fb8ad31c808572a69"

# GEOCODING KEYS
GMAPS_API_KEY = os.environ.get('GMAPS_API_KEY', None)
LOCATION_IQ_API_KEY = 'd077a0c8209119'

# Dealtrack Auth
DEALTRACK_GATEWAY_URL = os.environ.get('DEALTRACK_GATEWAY_URL', None)
DEALTRACK_GATEWAY_TOKEN = os.environ.get('GATEWAY_TOKEN', None)

# Filepaths to helper files for auto scoring.
HELPER_FPATH = os.path.join(ROOT_DIR, "data/model")
ALL_CARTO_FPATH = os.path.join(HELPER_FPATH, "location_scorecard_record_190819_dev.csv")
IMPUTED_CARTO_FPATH="../data/model/scoring_intermediate/input_with_carto_imputed.csv"
SMOOTHED_CARTO_FPATH="../data/model/scoring_intermediate/input_carto_smoothed.csv"
LOC_UTILS_FPATH="../src/model/location_scorecard_utils_transit_market0828.R"
R_UTILS_FPATH="../src/model/R_util.R"

COMPSTAK_FPATH_US="../data/model/merged_compstak.csv"

GREGSPEC_FPATH="../data/model/gregspec.csv"
DB_FEATURES_FPATH="../data/model/scoring_intermediate/input_with_db_features.csv"
# US
DB_FPATH_US="../data/model/h5/DB_US.h5"
DB_COMPSTAK_US="../data/model/db_features_compstak.csv"
CARTO_COMPSTAK_US="../data/model/arto_features_compstak_block_group_smoothed.csv"
MSA_FPATH="../data/model/zipcode_county_msa_dma.csv"

# CA
DB_FPATH_CA="../data/model/h5/DB_CAN_v2.h5"
DB_COMPSTAK_CA="../data/model/get_db_canada_20190514.csv"
CARTO_COMPSTAK_CA="../data/model/CA_compstak_carto_smoothed.csv"

DEFAULT_MODEL_VERSION='us_2.0.0'

STAGE = os.environ.get('STAGE', 'dev')

S3_BUCKET = os.environ.get('S3_BUCKET', 's3_bucket_default_name')

SFDC_ENDPOINT = "https://wework.lightning.force.com/"
SFDC_USERNAME = os.environ.get('SFDC_USERNAME', None)
SFDC_PASSWORD = os.environ.get('SFDC_PASSWORD', None)
SFDC_SECURITY_TOKEN = os.environ.get('SFDC_SECURITY_TOKEN', None)
