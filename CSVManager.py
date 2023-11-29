import csv
from pprint import pprint
from typing import List, Dict, Any


class CSVManager:
    def __init__(self):
        self.path = 'periodictable.csv'

    def read_file(self) -> list[list]:
        with open(self.path) as f:
            reader = csv.reader(f)
            return list(reader)

    def reformat_data(self, data: list[list]) -> list[dict[int, str]]:
        reformatted_data = []

        for el_id, row in enumerate(data, start=1):
            context_data = {
                'Atomic_number': row[0],
                'Symbol': row[1],
                'Element': row[2],
                'Origin_of_name': row[3],
                'Group': row[4],
                'Period': row[5],
                'Atomic_weight': row[6],
                'Density': row[7],
                'Melting_point': row[8],
                'Boiling_point': row[9],
                'Specific_heat_capacity': row[10],
                'Electronegativity': row[11],
                'Abundance_in_earth\'s_crust': row[12]
            }

            str_data = ''

            for el in context_data:
                str_data += f'{el.replace("_", " ")}: {context_data[el]}\n'

            reformatted_data.append({el_id: str_data})

        return reformatted_data

    def get_data_by_id(self, el_id: int) -> str:
        data = self.reformat_data(self.read_file())

        return data[el_id-1][el_id]