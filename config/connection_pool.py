# connection_pool.py -- Web Service DB config
# fix: increased MAX_CONNECTIONS from 10 to 50
# Root cause: rb-0001 (2026-05-10) pool exhaustion at >moderate load

MAX_CONNECTIONS      = 50    # was 10
MIN_IDLE             = 5
STATEMENT_TIMEOUT_MS = 30_000
IDLE_TIMEOUT_MS      = 600_000
CONNECT_TIMEOUT_MS   = 5_000
