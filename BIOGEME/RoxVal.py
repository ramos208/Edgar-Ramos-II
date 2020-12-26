import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
from biogeme.expressions import Beta

# Read the data
df = pd.read_csv('data', '\t')
database = db.Database('aicce', df)
# The following statement allows you to use the names of the
# variable as Python variable.
globals().update(database.variables)

# Removing some observations

database.remove(SPCHOIC == 0)

# Parameters to be estimated
ASCA = Beta('ASCA', 0, None, None, 0)
ASCB = Beta('ASCB', 0, None, None, 0)
ASCC = Beta('ASCC', 0, None, None, 1)
ASCD = Beta('ASCD', 0, None, None, 0)
ASCE = Beta('ASCE', 0, None, None, 0)
ASCF = Beta('ASCF', 0, None, None, 0)
TIME = Beta('TIME', 0, None, None, 0)
CST = Beta('CST', 0, None, None, 0)
CAR = Beta('CAR', 0, None, None, 0)
CSTL = Beta('CSTL', 0, None, None, 0)
COMCOST = Beta('COMCOST', 0, None, None, 0)



# Definition of new variables


# Definition of the utility functions
V1 = ASCA + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CST * TOTCOST
V2 = ASCB + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CST * TOTCOST
V3 = ASCC + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CST * TOTCOST
V4 = ASCD + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CSTL * TOTCOST + \
     CAR * (NUM_CAR + NUM_VAN + NUM_SUV)
V5 = ASCE + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CSTL * TOTCOST
V6 = ASCF + \
     TIME * TOTTIME + \
     COMCOST * (COMFCOD*TOTCOST) + \
     CSTL * TOTCOST

# Associate utility functions with the numbering of alternatives
V = {1: V1,
     2: V2,
     3: V3,
     4: V4,
     5: V5,
     6: V6}

# Associate the availability conditions with the alternatives


# Definition of the model. This is the contribution of each
# observation to the log likelihood function.
logprob = models.loglogit(V, None, ALTIJ)

# Create the Biogeme object
biogeme = bio.BIOGEME(database, logprob)
biogeme.modelName = 'RoxVal'

# Estimate the parameters
results = biogeme.estimate()

# Get the results in a pandas table
pandasResults = results.getEstimatedParameters()
print(pandasResults)