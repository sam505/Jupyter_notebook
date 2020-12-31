import pandas as pd

df = pd.read_csv("/home/sammie/Python/Assignment_data_input.csv", header=None)


class AirportConveyorBelt:
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size

    def check_weight_and_size(self, under, approp, over, cabin):
        count = 0
        for i in self.weight:
            if i <= 7 and self.size[count] == 'Very Small':
                print(self.size[count])
                cabin.update_values(count)
            if 7 < i < 30 and (self.size[count] == 'Small' or self.size[count] == 'Normal'):
                under.update_values(count)
            if (i == 30) and (self.size[count] == 'Big' or self.size[count] == 'Normal'):
                approp.update_values(count)
            if (i > 30) and (self.size[count] == 'Big' or self.size[count] == 'Normal'):
                over.update_values(count)
            count += 1
        return count


class UpdateCSV:
    def __init__(self):
        self.name_new = []
        self.weight_new = []
        self.size_new = []
        self.temperature_new = []
        self.dry_cough_new = []
        self.sore_throat_new = []
        self.resp_problems_new = []
        self.data_frame = {0: self.name_new, 1: self.weight_new, 2: self.size_new, 3: self.temperature_new,
                           4: self.dry_cough_new, 5: self.sore_throat_new, 6: self.resp_problems_new}

    def update_values(self, count):
        self.name_new.append(df[0][count])
        self.weight_new.append(df[1][count])
        self.size_new.append(df[2][count])
        self.temperature_new.append(df[3][count])
        self.dry_cough_new.append(df[4][count])
        self.sore_throat_new.append(df[5][count])
        self.resp_problems_new.append(df[6][count])

    def under_weight(self):
        info = pd.DataFrame(self.data_frame)
        info.to_csv('Under_weight.csv', header=None, index=False)

    def appropriate_weight(self):
        info = pd.DataFrame(self.data_frame)
        info.to_csv('Appropriate_weight.csv', header=None, index=False)

    def over_weight(self):
        info = pd.DataFrame(self.data_frame)
        info.to_csv('Over_weight.csv', header=None, index=False)

    def cabin_luggage(self):
        info = pd.DataFrame(self.data_frame)
        info.to_csv('Cabin_luggage.csv', header=None, index=False)


conveyors = AirportConveyorBelt(name=df[0], weight=df[1], size=df[2])
uw = UpdateCSV()
aw = UpdateCSV()
ow = UpdateCSV()
cl = UpdateCSV()
conveyors.check_weight_and_size(uw, aw, ow, cl)
uw.under_weight()
aw.appropriate_weight()
ow.over_weight()
cl.cabin_luggage()
