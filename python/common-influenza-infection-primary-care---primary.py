# Chukwuma Iwundu, Clare MacRae, Eleftheria Vasileiou, 2024.

import sys, csv, re

codes = [{"code":"1118771000006112","system":"snomedct"},{"code":"843921000033117","system":"snomedct"},{"code":"1024921000006116","system":"snomedct"},{"code":"843921000033117","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('influenza-infection-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["common-influenza-infection-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["common-influenza-infection-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["common-influenza-infection-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
