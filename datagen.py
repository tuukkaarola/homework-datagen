import csv
import sys
from datetime import date

if len(sys.argv) > 2:
    years = int(sys.argv[1])
    num_lines = int(sys.argv[2])
else: 
    years = 10
    num_lines = 100_000

print(f"Creating data with {years * num_lines} of rows")

with open('data.csv', mode='w', newline='') as data_file, open('ref.csv', mode='w', newline='') as ref_file:
    data_writer = csv.writer(data_file)
    ref_writer = csv.writer(ref_file)
    
    # Write the header
    data_writer.writerow(['id', 'type', 'value'])
    ref_writer.writerow(['id', 'ref_text'])
    
    ref = 0
    entry = 0
    for y in range(2014, 2014 + years):
        begins = date(y, 1, 1)
        created = date(y - 1, 1, 1)
        expires = date(y, 12, 31)

        # Write the lines
        for i in range(num_lines):
            data_writer.writerow([ref, "name", f"name_{y}_{i}"])
            data_writer.writerow([ref, "begins_at", begins])
            data_writer.writerow([ref, "created_at", created])
            data_writer.writerow([ref, "expires_at", expires])
            data_writer.writerow([ref, "ref_id", ref])

            ref_writer.writerow([ref, f"ref_{ref}_{y}_{i}"])

            if ref % 100_000 == 0:
                print(f"Done processing {ref} rows...")
    
            ref = ref + 1
            
print("Done.")