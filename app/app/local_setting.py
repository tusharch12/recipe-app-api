SECRET_KEY1 = 'django-insecure-syueyllf)'
SECRET_KEY2 = 'j09^1+41j3mgdb36mi#x9c2)_pb^bz_%g-xq#u5^&'

SECRET_KEY = SECRET_KEY1 + SECRET_KEY2


# Password validation Constant
class PVC:
    USE_ATTRIBUTE = '.UserAttributeSimilarityValidator'
    MINI_LEN_VAL = '.MinimumLengthValidator'
    COMM_PASS_VAL = '.CommonPasswordValidator'
    NUM_PASS_VAL = '.NumericPasswordValidator' 
