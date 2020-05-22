# Investigating_Airplane_Accidents
In this project, we worked with a dataset of airplane accident statistics to analyze patterns and look for any common threads. The dataset we have worked with contains 77,282 aviation accidents that occurred in the U.S., and the metadata associated with them. The data in our `AviationData.txt` file comes from the [National Transportation Safety Board (NTSB)](http://www.ntsb.gov/Pages/default.aspx) and is available for download [here](http://catalog.data.gov/dataset/aviation-data-and-documentation-from-the-ntsb-accident-database-system-05748/resource/4b1e95fe-91a7-4112-85fa-424d2672a906). The preview of file is below:

Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date | 20150908X74637 | Accident | CEN15LA402 | 09/08/2015 | Freeport, IL | United States | 42.246111 | -89.581945 | KFEP | albertus Airport | Non-Fatal | Substantial | Unknown | N24TL | CLARKE REGINALD W | DRAGONFLY MK | | | | Part 91: General Aviation | | Personal | | | 1 | | | VMC | TAKEOFF | Preliminary | 09/09/2015 |

As we can see, the file isn't in CSV format; it separates the fields with a pipe character (`|`) instead. Below is a description of some columns:

- `Event Id` - The unique id for the incident
- `Investigation Type` - The type of investigation the NTSB conducted
- `Event Date` - The date of the accident
- `Location` - Where the accident occurred
- `Country` - The country where the accident occurred
- `Latitude` - The latitude where the accident occurred
- `Longitude` - The longitude where the accident occurred
- `Injury Severity` - The severity of any injuries
- `Aircraft Damage` - The extent of the damage to the aircraft
- `Aircraft Category` - The type of aircraft
- `Make` - The make of the aircraft
- `Model` - The model of the aircraft
- `Number of Engines` - The number of engines on the plane
- `Air Carrier` - The carrier operating the aircraft
- `Total Fatal Injuries` - The number of fatal injuries
- `Total Serious Injuries` - The number of serious injuries
- `Total Minor Injuries` - The number of minor injuries
- `Total Uninjured` - The number of people who did not sustain injuries
- `Broad Phase of Flight` - The phase of flight during which the accident occurred
