# Topology with a tail:
# 2 --- 7
# |     |
# |     |
# 3 --- 5 --- 9 --- 11 --- 1

topo = { 1 : [11],
         2 : [3, 7],
         3 : [2, 5],
         5 : [3, 7, 9],
         7 : [2, 5],
         9 : [5, 11],
         11: [1, 9] }
ttl_limit = 5
drops = [2]
