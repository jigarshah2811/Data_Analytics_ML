import pandas as pd

filename = "../resources/new_access.log"
log = pd.read_csv(filename, sep='\s+',
            usecols=(0, 3, 5, 6, 7, 9),
            names=['addr', 'req_date', 'request', 'status', 'size', 'browser'],
            error_bad_lines=False
)

print("Shape:", log.shape)
print("Head:", log.head(5))

log.req_date = pd.to_datetime(log.req_date, format='[%d/%b/%Y:%H:%M:%S')

date_based_log = log.set_index('req_date')
