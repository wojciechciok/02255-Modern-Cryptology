from key_scheduler import KeyScheduler

# scheduler = KeyScheduler('000102030405060708090a0b0c0d0e0f')
scheduler = KeyScheduler('000102030405060708090a0b0c0d0e0f')
scheduler.get_next_key()
scheduler.get_next_key()
blocks = scheduler.get_next_key()
print(blocks)
