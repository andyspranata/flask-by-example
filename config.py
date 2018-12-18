#!/usr/bin/env python3

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  # generate using 'openssl rand -base64 32'
  SECRET_KEY = "EfXFld20yUXsgI/nSyj9R4XIgJYGl2g3jUckUvOpAR4=" 

class ProductionConfig(Config):
  DEBUG = False

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True