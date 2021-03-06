EXEC_PROGRAM = 'hclustering'
DENSE_INPUT	 = 'D'
SPARSE_INPUT = 'S'

JACCARD_DISTANCE_TYPE = 'J'
EUCLID_DISTANCE_TYPE ='E'
MATRIX_DISTANCE_TYPE = 'M'
DIR_DISTANCE_TYPE = 'D'

SINGLE_LINKAGE_ALGORITHM = 'S'
COMPLETE_LINKAGE_ALGORITHM ='C'
AVG_LINKAGE_ALGORITHM = 'A'

MY_ALGORITHM = 'L'
MY_NUM_CLUSTER = 'K'
MY_THRESHOLD = 'T'
MY_HELP	= 'H'
MY_INPUT_FILE = 'I'
MY_DISTANCE_TYPE = 'D'
MY_OUTPUT_FILE = 'O'


BY_NUMBER = 0
BY_THRESHOLD = 1


SPARSE_MATRIX = 0       # myCLA.inputMatrixType
DENSE_MATRIX = 1       # myCLA.inputMatrixType 
EMPTY_MATRIX = 2       # myCLA.inputMatrixType (DEFAULT)

JACCARD_DISTANCE = 0
EUCLID_DISTANCE = 1
MATRIX_DISTANCE	= 2   # distance provided by a matrix file
DIR_DISTANCE = 3   # distance provided by a dir of files

SINGLE_LINKAGE = 0
COMPLETE_LINKAGE = 1
AVG_LINKAGE	= 2

DEFAULT_cutoffType = BY_NUMBER
DEFAULT_algorithmType = SINGLE_LINKAGE
DEFAULT_numCluster = 3
DEFAULT_threshold = 100000.0
DEFAULT_distanceType = JACCARD_DISTANCE
DEFAULT_inputMatrixType	= EMPTY_MATRIX

DEFAULT_STRING_LENGTH = 1024
FILENAME_LENGTH	= DEFAULT_STRING_LENGTH
EMPTY_STRING = ''

FEATURE_SIZE = 240007

MIN_DIST = 10000

DOT_PRODUCT = 0
JACCARD = 1