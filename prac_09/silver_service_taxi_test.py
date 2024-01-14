from silver_service_taxi import SilverServiceTaxi

sst = SilverServiceTaxi('Hummer', 100, 2)

sst.start_fare()
sst.drive(18)
print(sst)
