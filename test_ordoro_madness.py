"""Pytest to check connectivity with the gist.github repo

"""


import requests
import ordoro_madness

def test_gist_full_json():
  '''
    Test Full.json
  '''
  api_url = "https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/145698b6185d1109f7b4a8c1576a4e862b8b52f7/full.json"


  res = requests.get(api_url,
                     params={},
                     headers={},
                     verify=False)
  assert res.ok
  assert 'data' in res.json()

def test_ordoro_minimial_json():
  '''

  '''
  api_url = 'https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/543ad1119fae380acfe3268e51a5c421c4288cb7/minimal.json'
  res = requests.get(api_url,
                       params={},
                       headers={},
                       verify=False)
  data = res.json().get("data")
  assert res.ok
  assert data

def test_ordoro_madness_minimal():
  '''
  Test Ordoro Madness function
  '''
  api_url = 'https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/543ad1119fae380acfe3268e51a5c421c4288cb7/minimal.json'
  login_data = ordoro_madness.ordoro_madness(api_url)

  assert 'admin@nsa.com' in login_data.get("uniques")

def test_ordoro_madness_full():
  '''
  Test Ordoro Madness function
  '''
  api_url = "https://gist.githubusercontent.com/benweatherman/e25017016bed9625fc03/raw/145698b6185d1109f7b4a8c1576a4e862b8b52f7/full.json"
  login_data = ordoro_madness.ordoro_madness(api_url)

  assert login_data.get("uniques")


