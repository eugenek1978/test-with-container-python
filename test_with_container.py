import time
import mysql.connector

import testcontainers.compose

COMPOSE_PATH = './'
hostname = 'localhost'
username = 'root'
password = '111111'


def get_db_conn():
    """function returning the DB psycopg2 connection."""
    conn = mysql.connector.connect(host=hostname, port='3308' , user=username, passwd=password, charset='utf8')
    return conn

def setup_module():
    compose = testcontainers.compose.DockerCompose(COMPOSE_PATH)
    compose.start()
    time.sleep(20)
    return compose, get_db_conn()


def teardown_module(compose):
    compose.stop()


def test_db():
    compose = setup_module()
    # Test 1: Check DB accepts connections
    cur = compose[1].cursor()
    cur.execute("SELECT 'SUCCESS' FROM DUAL")
    # assert cur.fetchone()[0] == "foo", "Database is not running"
    print(cur.fetchone()[0])
    cur.close()
    teardown_module(compose[0])

