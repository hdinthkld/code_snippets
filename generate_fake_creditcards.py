from faker import Faker

# Run 'pip install faker' before trying to use script

fake = Faker()

with open('fake_ccs.txt', 'w') as ccwriter:
  for _ in range (0, 10000):
    ccwriter.write(fake.credit_card_full())
    ccwriter.write("------\n")

