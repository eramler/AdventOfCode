import pandas
import numpy

# Get and process input
path = r'2023/05/05_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=True)[0]

def SplitConvertInt(String: str) -> list[int]:
    elements = String.split()
    return [int(x) for x in elements]

# def ProcessDict(Dict: dict, SourceStart: int, TargetStart: int, Range: int):
#     for i in range(Range):
#         Dict[SourceStart + i] = TargetStart + i

def FindRanges(TargetStart: int, SourceStart: int, Range: int):
    SourceMin = SourceStart
    SourceMax = SourceStart + Range - 1
    TargetMin = TargetStart
    TargetMax = TargetStart + Range - 1
    return [SourceMin, SourceMax, TargetMin, TargetMax]

def SplitAndProcess(List: list, String: str):
    InputParams = SplitConvertInt(String)
    Ranges = FindRanges(InputParams[0], InputParams[1], InputParams[2])
    List.append(Ranges)

currentmap = ""
seeds = []
seed_soil = []
soil_ferti = []
ferti_water = []
water_light = []
light_temp = []
temp_humid = []
humid_loc = []
for i in range(len(raw_input)):
    row = raw_input[i]
    if row[-4:] == 'map:':
        currentmap = row[:-4].strip()
        continue
    match currentmap:
        case 'seed-to-soil':
            SplitAndProcess(seed_soil, row)
        case 'soil-to-fertilizer':
            SplitAndProcess(soil_ferti, row)
        case 'fertilizer-to-water':
            SplitAndProcess(ferti_water, row)
        case 'water-to-light':
            SplitAndProcess(water_light, row)
        case 'light-to-temperature':
            SplitAndProcess(light_temp, row)
        case 'temperature-to-humidity':
            SplitAndProcess(temp_humid, row)
        case 'humidity-to-location':
            SplitAndProcess(humid_loc, row)
        case _:
            seeds = SplitConvertInt(row[7:])

print(seed_soil)

# Define Functions
def CheckRanges(Value: int, Params: list[int]) -> bool:
    return Value >= Params[0] and Value <= Params[1]

def GetTargetValue(Value: int, Params: list[int]) -> int:
    return Params[2] + Value - Params[0]

def FindInMapping(Mapping: list[list[int]], Value: int) -> int:
    NewValue = Value
    for i in range(len(Mapping)):
        ThisRange = Mapping[i]
        ValueInRange = CheckRanges(Value, ThisRange)
        if ValueInRange:
            NewValue = GetTargetValue(Value, ThisRange)
    return NewValue

def SeedToLocation(seed: int) -> int:
    soil = FindInMapping(seed_soil, seed)
    ferti = FindInMapping(soil_ferti, soil)
    water = FindInMapping(ferti_water, ferti)
    light = FindInMapping(water_light, water)
    temp = FindInMapping(light_temp, light)
    humid = FindInMapping(temp_humid, temp)
    loc = FindInMapping(humid_loc, humid)
    return loc

locations = [SeedToLocation(seed) for seed in seeds]
print(min(locations))

