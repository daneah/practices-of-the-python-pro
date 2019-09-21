# Single import
from time import time
print(time())


# Different import
from datetime import time
print(time())


# Both imports at once
from time import time
from datetime import time
print(time())  # <1>


# Disambiguiation by importing whole modules
import time
import datetime
now = time.time()  # <1>
midnight = datetime.time()  # <2>


# Disambiguation via renaming
import datetime
from mycoollibrary import datetime as cooldatetime
