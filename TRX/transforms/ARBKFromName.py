from maltego_trx.entities import Person
from maltego_trx.maltego import UIM_PARTIAL
from maltego_trx.transform import DiscoverableTransform


class ARBKFromName(DiscoverableTransform):
    """
    Lookup the name associated with a phone number.
    """

    @classmethod
    def create_entities(cls, request, response):
        names = request.Value

        try:
            names = cls.get_data(names)
            if names:
                for name in names:
                    response.addEntity(Person, name)
            else:
                response.addUIMessage("The names number given did not match any numbers in the CSV file")
        except IOError:
            response.addUIMessage("An error occurred reading the CSV file.", messageType=UIM_PARTIAL)

    @staticmethod
    def get_data(search_name):
        matching_businesses = []
        with open("/home/avdyl/FIEKMASTER/information-security/maltegodatatransformers/TRX/transforms/2018.csv") as f:
            for ln in f.readlines():
                # print(ln)
                try:
                    data = ln.split("|")
                    if search_name.strip() in data[6].strip():
                        matching_businesses.append(data)
                except:
                    pass
        return matching_businesses


if __name__ == "__main__":
    print(ARBKFromName.get_data("Lule Ahmedi"))