"""
1. sequential features (track order, previous event info)
2. lag features (previous track skipped?)
3. running features (running skip rate)
4. session-level summary features (session length, total session duration)
5. target-ready table for modeling
"""

import pandas as pd
