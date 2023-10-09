import json


class EasyRider:
    error_display = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
    total_errors = 0

    def __init__(self, bus_id, stop_id, stop_name, next_stop, stop_type, a_time):
        self.bus_id = bus_id
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.next_stop = next_stop
        self.stop_type = stop_type
        self.a_time = a_time

    def print1(self):
        #  print(self.bus_id, self.stop_id, self.stop_name, self.next_stop, self.stop_type, self.a_time)
        if isinstance(self.bus_id, int) is False:
            EasyRider.error_display['bus_id'] += 1
        if isinstance(self.stop_id, int) is False:
            EasyRider.error_display['stop_id'] += 1
        if isinstance(self.stop_name, str) is False:
            EasyRider.error_display['stop_name'] += 1
        if self.stop_name == '':
            EasyRider.error_display['stop_name'] += 1
        if isinstance(self.next_stop, int) is False:
            EasyRider.error_display['next_stop'] += 1
        if isinstance(self.stop_type, str) is True:
            if len(self.stop_type) > 1:
                EasyRider.error_display['stop_type'] += 1
        else:
            EasyRider.error_display['stop_type'] += 1
        if isinstance(self.a_time, str) is False:
            EasyRider.error_display['a_time'] += 1
        if self.a_time == '':
            EasyRider.error_display['a_time'] += 1
        return EasyRider.error_display

    def print2(self):
        for key, value in EasyRider.error_display.items():
            self.total_errors += value
        return self.total_errors

    @staticmethod
    def print3():
        for key, value in EasyRider.error_display.items():
            print(f'{key}: {value}')


ls_dict = json.loads(input())
#  print(bus_id_, stop_id_, stop_name_, next_stop_, stop_type_, a_time_)
for i in ls_dict:
    easy_bus = EasyRider(i['bus_id'], i['stop_id'], i['stop_name'], i['next_stop'], i['stop_type'], i['a_time'])
    easy_bus.print1()
print(f'Type and required field validation: {easy_bus.print2()} errors')
easy_bus.print3()
