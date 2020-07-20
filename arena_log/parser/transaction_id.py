transaction_ids = []
with open('resources/Logs/UTC_Log - 07-15-2020 00.15.57') as input:
    line = input.readline()
    if line.startswith('{ "transactionId"'):
        transaction_ids.append(line)

print()
