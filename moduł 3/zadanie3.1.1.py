sklep = {
  "piekarnia": ["chleb", "bułki", "pączek"],
  "warzywniak": ["marchew", "seler", "rukola"]
}

x = 0
print("Lista zakupów")

for i in sklep:
  print(f"Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {', '.join([p.capitalize() for p in sklep[i]])}")
  x = x + len(sklep[i])

print(f"W sumie kupuję {x} produktów")
